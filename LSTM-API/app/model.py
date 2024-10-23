import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('models/lstm_model.h5')

def predict(features):
    features_array = np.array(features).reshape((1, 1, len(features)))
    prediction = model.predict(features_array)
    return float(prediction[0][0])




# import tensorflow as tf

# model = tf.keras.models.load_model('/models/lstm_model.h5')

# def predict(features):
#     prediction = model.predict([features])
#     return prediction