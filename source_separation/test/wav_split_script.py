#!/usr/bin/python
"""
 Test the RNN fos splitting a wav
"""

import source_separation.preprocess.dataIO as dataIO
import source_separation.preprocess.wav_fft as wav_fft
import testnet
import scipy
import numpy as np

X_test, Y_test = dataIO.test_set()

mix_stft = X_test[1]
mix_stft_en = scipy.real(X_test[1])
tar_stft = Y_test[1]
tar_stft_en = scipy.real(Y_test[1])
scale = np.mean(mix_stft_en)
mix_stft_en = mix_stft_en/scale
tar_stft_en = tar_stft_en/scale

rnn= testnet.retrievenn("results/model_rnn_relu_2_150_weights.h5", 2, 150, 'relu', mix_stft_en)

input, y = rnn. prepare_data(mix_stft_en, np.zeros(10))

pred_stft_en = rnn.predict(input)

mask_1 = pred_stft_en[:, :512] / mix_stft_en[:186]

pred_stft = mix_stft[:186]* mask_1

wav_fft.writeWAV("essai", pred_stft)

