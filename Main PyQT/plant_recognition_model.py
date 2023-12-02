import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

class PlantRecognition:
    def __init__(self):
        model_url = "https://tfhub.dev/google/imagenet/inception_v3/classification/4"
        self.model = tf.keras.Sequential([hub.KerasLayer(model_url)])

        labels_path = tf.keras.utils.get_file('ImageNetLabels.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
        with open(labels_path, 'r') as f:
            self.labels = f.read().splitlines()

    def load_and_preprocess_image(self, image_path):
        img = Image.open(image_path).resize((299, 299))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        img_array /= 255.0
        return img_array

    def predict_plant(self, image_path):
        img_array = self.load_and_preprocess_image(image_path)
        predictions = self.model.predict(img_array)
        predicted_class = self.labels[np.argmax(predictions)]
        return predicted_class
