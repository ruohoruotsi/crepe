CREPE Pitch Tracker
===================

This is a pre-trained model for the ICASSP 2018 paper [(arxiv)](https://arxiv.org/abs/1802.06182):

> Jong Wook Kim, Justin Salamon, Peter Li, Juan Pablo Bello. "CREPE: Convolutional Representation for Pitch Estimation." *Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*. 2018.

The following script will generate a pitch estimation from the input audio and save to a TSV file:

```bash
$ python crepe.py audio_file.wav audio_file.f0.tsv
```

## Caveats

- The script requires Python packages `keras`, `numpy`, `resampy`, and `h5py` to be installed
- The code should run with any Keras backends in theory, but it was only tested with the TensorFlow backend; Keras 2.1.3 and TensorFlow 1.5.0 was used during development.
- This is a model pre-trained on MDB-STEM-Synth dataset [1], which contains vocal and instrumental sounds. Therefore this will work best for the similar audio signals.
- Prediction will be significantly faster if Keras (and thus the corresponding backend) is configured to run on GPU.
- This model does not predict the existence of voicing, which is a separate problem. The output corresponding to the silent portion of audio will be arbitrary.



[1] J. Salamon et al.  "An Analysis/Synthesis Framework for Automatic F0 Annotation of Multitrack Datasets."  *Proceedings of the International Society for Music Information Retrieval (ISMIR) Conference*. 2017.
