CREPE Pitch Tracker
===================

CREPE is a monophonic pitch tracker based on a deep convolutional neural network operating directly on the time-domain waveform input. CREPE is state-of-the-art (as of early 2018), outperfoming popular pitch trackers such as pYIN and SWIPE:

<img src=https://user-images.githubusercontent.com/3009670/36563051-ee6a69a0-17e6-11e8-8d7b-9a37d16ee7ad.png width=500>

Further details are provided in the following paper:

[CREPE: A Convolutional Representation for Pitch Estimation](https://arxiv.org/abs/1802.06182)<br/>
Jong Wook Kim, Justin Salamon, Peter Li, Juan Pablo Bello.<br/>
Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), April 2018.

We kindly request that academic publications making use of CREPE cite the aforementioned paper.

## Using CREPE
CREPE requires the following python dependencies:
- `numpy` & `scipy`
- `keras` (only tested with the TensorFlow backend)
- `h5py`

This repository includes a pre-trained version of the CREPE model for easy use. To estimate the pitch of `audio_file.wav` and save the output to `audio_file.f0.tsv` as tab separated values, run:

```bash
$ python crepe.py audio_file.wav audio_file.f0.tsv
```

Currently we do not support importing CREPE as a python module, though this functionality may be added in a future version.

## Please note

- The current version only supports wav files as input.
- While in principle the code should run with any Keras backend, it has only been tested with the TensorFlow backend. The model was trained using Keras 2.1.3 and TensorFlow 1.5.0.
- The pre-trained model included was trained on the MDB-STEM-Synth dataset [1], which contains vocal and instrumental recordings. It is therefore expected to work best on this type of audio signals.
- Prediction is significantly faster if Keras (and the corresponding backend) is configured to run on GPU.
- The current pre-trained model does not perform voicing activity detection (VAD), meaning it will return a continuous series of frequency values, including for sections of the recording where there is no pitch or silence. The output for such unpitched/silent segments will be arbitrary.


## References

[1] J. Salamon et al.  "An Analysis/Synthesis Framework for Automatic F0 Annotation of Multitrack Datasets."  *Proceedings of the International Society for Music Information Retrieval (ISMIR) Conference*. 2017.
