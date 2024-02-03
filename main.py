import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
from file_helper import get_all_files, is_file
from image_normalization import divide_image, normalize_image
from ml import generate_model
from ui_helper import UIHelper
import tensorflow as tf

if not os.path.exists("./model.myLetters"):
    generate_model()


classes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

model = tf.keras.models.load_model('model.myLetters')


def predict():
    result_word = []
    image_path = UIHelper.image_prompt()
    if not is_file(image_path):
        UIHelper.img_error_prompt()
        return {"status": "error", "message": "Did not provide an image"}

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    divide_image(img)
    letter_images = get_all_files('./temp')

    for letter_img in letter_images:
        letter_img = normalize_image(letter_img)
        letter_img = np.expand_dims(letter_img, axis=0)
        prediction = model.predict(letter_img)
        result_class = np.argmax(prediction)
        result_word.append(classes[result_class - 1])

    result = "".join(result_word)
    print(result)
    return {"status": "success", "message": result}


UI = UIHelper(predict)
