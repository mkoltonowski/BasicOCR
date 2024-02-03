import cv2
from file_helper import clear_folder
import numpy as np


def divide_image(img):
    clear_folder('./temp')
    _, threshold = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda contour: cv2.boundingRect(contour)[0])
    margin = 4  #margines żeby model nie dostawał szału przy próbkowaniu liter wchodzących na krawędź obrazu

    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)

            x_margin = max(0, x - margin)
            y_margin = max(0, y - margin)
            w_margin = min(img.shape[1] - x_margin, w + 2 * margin)
            h_margin = min(img.shape[0] - y_margin, h + 2 * margin)

            letter = img[y_margin:y_margin + h_margin, x_margin:x_margin + w_margin]

            cv2.imwrite(f'./temp/{i}.png', letter)


def normalize_image(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = cv2.bitwise_not(img)
    img = cv2.resize(img, (28, 28))
    img = img / 255
    return img
