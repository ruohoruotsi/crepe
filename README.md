CREPE Pitch Tracker
===================

This is a pre-trained model for ICASSP 2018 submission <CREPE: Convolutional Representation for Pitch Estimation>.

The following script will generate a pitch estimation from the input audio and save to a TSV file:

```bash
$ python crepe.py audio_file.wav audio_file.f0.tsv
```

## Caveats

- The script requires `keras`, `numpy`, and `h5py` to be installed.
- This is a model pre-trained on MedleyDB-STEM-Synth dataset [1], which contains vocal and instrumental sounds. Therefore this will work best for the similar audio signals.
- Prediction will be significantly faster if Keras (and thus the corresponding backend) is configured to run on GPU.
- This model does not predict the existence of voicing, which is a separate problem. The output corresponding to the silent portion of audio will be arbitrary.



[1] J. Salamon et al.  An Analysis/Synthesis Framework for Automatic F0 Annotation of Multitrack Datasets in *Proceedings of ISMIR Conference 2017*
