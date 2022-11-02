import string
import numpy as np

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import LSTM, Input, TimeDistributed, Dense, Activation, RepeatVector, Embedding
from keras.optimizers import adam_v2
from keras.losses import sparse_categorical_crossentropy

def encoder(
        x_train: np.ndarray,
        y_train: np.ndarray,
        x_val,
        y_val,
        batch_size: int = 10,
        n_epochs: int = 100
        ):
    input_sequence = Input(shape=(x_train[1],))
    embedding = Embedding(input_dim=x_train[0], output_dim=128,)(input_sequence)
    encoder = LSTM(64, return_sequences=False)(embedding)
    r_vec = RepeatVector(y_train[1])(encoder)
    decoder = LSTM(64, return_sequences=True, dropout=0.2)(r_vec)
    logits = TimeDistributed(Dense(y_train[0]))(decoder)
    enc_dec_model = Model(input_sequence, Activation('softmax')(logits))
    enc_dec_model.compile(loss=sparse_categorical_crossentropy,
              optimizer=adam_v2.Adam(1e-3),
              metrics=['accuracy'])
    return cls(enc_dec_model)