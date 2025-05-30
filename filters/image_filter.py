# filters/image_filter.py
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from config import MODEL_PATH, CONFIDENCE_THRESHOLD

model = tf.keras.models.load_model(MODEL_PATH)

def predict_couple_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    prediction = model.predict(x)[0][0]
    return prediction >= CONFIDENCE_THRESHOLD
