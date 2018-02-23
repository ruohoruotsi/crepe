from __future__ import print_function


# open the file and read the data
import sys

if len(sys.argv) < 2:
    print("usage: %s wav_file_path [output_tsv_file_path]" % sys.argv[0], file=sys.stderr)
    sys.exit(-1)

filename = sys.argv[1]

from scipy.io import wavfile
from resampy import resample

try:
    srate, data = wavfile.read(filename)
    if len(data.shape) == 2:
        data = data[:, 0]
    if srate != 16000:
        data = resample(data, srate, 16000)
except:
    print("could not read %s" % filename)
    sys.exit(-1)


# build the CNN model
from keras.layers import *
from keras.models import Model

layers = [1, 2, 3, 4, 5, 6]
filters = [1024, 128, 128, 128, 256, 512]
widths = [512, 64, 64, 64, 64, 64]
strides = [(4, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]

x = Input(shape=(1024, 1, 1), dtype='float32')
y = x

for layer, filters, width, strides in zip(layers, filters, widths, strides):
    y = BatchNormalization(name="conv%d-BN" % layer)(y)
    y = Conv2D(filters, (width, 1), strides=strides, padding='same', activation='relu', name="conv%d" % layer)(y)
    y = MaxPooling2D(pool_size=(2, 1), strides=None, padding='valid', name="conv%d-maxpool" % layer)(y)
    y = Dropout(0.25, name="conv%d-dropout" % layer)(y)

y = Permute((2, 1, 3), name="transpose")(y)
y = Flatten(name="flatten")(y)
y = Dense(360, activation='sigmoid', name="classifier")(y)

model = Model(inputs=x, outputs=y)
model.load_weights("crepe.h5")
model.compile('adam', 'binary_crossentropy')


# transform the WAV data to frames
import numpy as np
from numpy.lib.stride_tricks import as_strided

data = data.astype(np.float32)

hop_length = int(srate / 100)
n_frames = 1 + int((len(data) - 1024) / hop_length)
frames = as_strided(data, shape=(1024, n_frames), strides=(data.itemsize, hop_length * data.itemsize))
frames = frames.transpose().reshape((n_frames, 1024, 1, 1))


# run prediction and convert the frequency bin weights to Hz
prediction = model.predict(frames, verbose=1)
cents_mapping = np.expand_dims(np.linspace(0, 7180, 360) + 1997.3794084376191, axis=0)
prediction_cents = np.sum(cents_mapping * prediction, axis=1) / np.sum(prediction, axis=1)
prediction_hz = 10 * (2 ** (prediction_cents / 1200))
prediction_hz[np.isnan(prediction_hz)] = 0

# write prediction as TSV
outfile = len(sys.argv) > 2 and sys.argv[2] or filename + ".f0.tsv"
with open(outfile, 'w') as out:
    for i, freq in enumerate(prediction_hz):
        print("%.2f\t%.3f" % (i * 0.01, freq), file=out)
