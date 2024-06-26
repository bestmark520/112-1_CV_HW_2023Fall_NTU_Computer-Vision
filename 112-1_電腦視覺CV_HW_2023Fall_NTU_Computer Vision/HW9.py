import math
import cv2 as cv
import numpy as np
import os

output_directory = 'results'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def matrix_mul(m1, m2):
    row, col = m1.shape
    sum = 0
    for i in range(row):
        for j in range(col):
            sum = sum + m1[i, j] * m2[i, j]
    return sum


def main1(image, threshold):
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    robert_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            r1 = int(pad[i + 1, j + 1]) - int(pad[i, j])
            r2 = int(pad[i + 1, j - 1]) - int(pad[i, j])
            if (pow(r1, 2) + pow(r2, 2)) ** 0.5 >= threshold:
                robert_img[i - 1][j - 1] = 0
            else:
                robert_img[i - 1][j - 1] = 255
    return robert_img


def main2(image, threshold):
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    prewitt_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            r1 = -1 * (int(pad[i - 1, j - 1]) + int(pad[i - 1, j]) + int(pad[i - 1, j + 1])) + \
                 (int(pad[i + 1, j - 1]) + int(pad[i + 1, j]) + int(pad[i + 1, j + 1]))
            r2 = -1 * (int(pad[i - 1, j - 1]) + int(pad[i, j - 1]) + int(pad[i + 1, j - 1])) + \
                 (int(pad[i - 1, j + 1]) + int(pad[i, j + 1]) + int(pad[i + 1, j + 1]))
            if (pow(r1, 2) + pow(r2, 2)) ** 0.5 >= threshold:
                prewitt_img[i - 1][j - 1] = 0
            else:
                prewitt_img[i - 1][j - 1] = 255
    return prewitt_img


def main3(image, threshold):
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    sobel_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            r1 = -1 * (int(pad[i - 1, j - 1]) + 2 * int(pad[i - 1, j]) + int(pad[i - 1, j + 1])) + \
                 (int(pad[i + 1, j - 1]) + 2 * int(pad[i + 1, j]) + int(pad[i + 1, j + 1]))
            r2 = -1 * (int(pad[i - 1, j - 1]) + 2 * int(pad[i, j - 1]) + int(pad[i + 1, j - 1])) + \
                 (int(pad[i - 1, j + 1]) + 2 * int(pad[i, j + 1]) + int(pad[i + 1, j + 1]))
            if (pow(r1, 2) + pow(r2, 2)) ** 0.5 >= threshold:
                sobel_img[i - 1][j - 1] = 0
            else:
                sobel_img[i - 1][j - 1] = 255
    return sobel_img


def main4(image, threshold):
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    frei_and_chen_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            r1 = -1 * (int(pad[i - 1, j - 1]) + int(pad[i - 1, j]) * (2 ** 0.5) + int(pad[i - 1, j + 1])) + \
                 (int(pad[i + 1, j - 1]) + int(pad[i + 1, j]) * (2 ** 0.5) + int(pad[i + 1, j + 1]))
            r2 = -1 * (int(pad[i - 1, j - 1]) + int(pad[i, j - 1]) * (2 ** 0.5) + int(pad[i + 1, j - 1])) + \
                 (int(pad[i - 1, j + 1]) + int(pad[i, j + 1]) * (2 ** 0.5) + int(pad[i + 1, j + 1]))
            if (pow(r1, 2) + pow(r2, 2)) ** 0.5 >= threshold:
                frei_and_chen_img[i - 1][j - 1] = 0
            else:
                frei_and_chen_img[i - 1][j - 1] = 255
    return frei_and_chen_img


def main5(image, threshold):
    k0 = np.array(
        [[-3, -3, 5],
         [-3, 0, 5],
         [-3, -3, 5]])
    k1 = np.array(
        [[-3, 5, 5],
         [-3, 0, 5],
         [-3, -3, -3]])
    k2 = np.array(
        [[5, 5, 5],
         [-3, 0, -3],
         [-3, -3, -3]])
    k3 = np.array(
        [[5, 5, -3],
         [5, 0, -3],
         [-3, -3, -3]])
    k4 = np.array(
        [[5, -3, -3],
         [5, 0, -3],
         [5, -3, -3]])
    k5 = np.array(
        [[-3, -3, -3],
         [5, 0, -3],
         [5, 5, -3]])
    k6 = np.array(
        [[-3, -3, -3],
         [-3, 0, -3],
         [5, 5, 5]])
    k7 = np.array(
        [[-3, -3, -3],
         [-3, 0, 5],
         [-3, 5, 5]])
    kernels = [k0, k1, k2, k3, k4, k5, k6, k7]
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    krisch_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            max = 0
            flag = 0
            for kernel in kernels:
                r = np.sum(kernel * pad[i - 1: i + 2, j - 1: j + 2])
                if r > max:
                    max = r
                    if (max >= threshold):
                        flag = 1
                        break
            if max >= threshold or flag == 1:
                krisch_img[i - 1][j - 1] = 0
            else:
                krisch_img[i - 1][j - 1] = 255
    return krisch_img


def main6(image, threshold):
    r0 = np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]])
    r1 = np.array(
        [[0, 1, 2],
         [-1, 0, 1],
         [-2, -1, 0]])
    r2 = np.array(
        [[1, 2, 1],
         [0, 0, 0],
         [-1, -2, -1]])
    r3 = np.array(
        [[2, 1, 0],
         [1, 0, -1],
         [0, -1, -2]])
    r4 = np.array(
        [[1, 0, -1],
         [2, 0, -2],
         [1, 0, -1]])
    r5 = np.array(
        [[0, -1, -2],
         [1, 0, -1],
         [2, 1, 0]])
    r6 = np.array(
        [[-1, -2, -1],
         [0, 0, 0],
         [1, 2, 1]])
    r7 = np.array(
        [[-2, -1, 0],
         [-1, 0, 1],
         [0, 1, 2]])
    kernels = [r0, r1, r2, r3, r4, r5, r6, r7]
    pad = cv.copyMakeBorder(image, 1, 1, 1, 1, cv.BORDER_REPLICATE)  # pad_around
    robinson_img = image.copy()
    row, col = image.shape
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            max = 0
            flag = 0
            for kernel in kernels:
                r = np.sum(kernel * pad[i - 1: i + 2, j - 1: j + 2])
                if r > max:
                    max = r
                    if (max >= threshold):
                        flag = 1
                        break
            if max >= threshold or flag == 1:
                robinson_img[i - 1][j - 1] = 0
            else:
                robinson_img[i - 1][j - 1] = 255
    return robinson_img


def main7(image, threshold):
    n0 = np.array([
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [0, 0, 0, 0, 0],
        [-100, -100, -100, -100, -100],
        [-100, -100, -100, -100, -100], ])
    n1 = np.array([
        [100, 100, 100, 100, 100],
        [100, 100, 100, 78, -32],
        [100, 92, 0, -92, -100],
        [32, -78, -100, -100, -100],
        [-100, -100, -100, -100, -100]])
    n2 = np.array([
        [100, 100, 100, 32, -100],
        [100, 100, 92, -78, -100],
        [100, 100, 0, -100, -100],
        [100, 78, -92, -100, -100],
        [100, -32, -100, -100, -100]])
    n3 = np.array([
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100]])
    n4 = np.array([
        [-100, 32, 100, 100, 100],
        [-100, -78, 92, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, -92, 78, 100],
        [-100, -100, -100, -32, 100]])
    n5 = np.array([
        [100, 100, 100, 100, 100],
        [-32, 78, 100, 100, 100],
        [-100, -92, 0, 92, 100],
        [-100, -100, -100, -78, 32],
        [-100, -100, -100, -100, -100]])
    kernels = [n0, n1, n2, n3, n4, n5]
    pad = cv.copyMakeBorder(image, 2, 2, 2, 2, cv.BORDER_REPLICATE)  # pad_around
    nevatia_img = image.copy()
    row, col = image.shape
    for i in range(2, row + 2):
        for j in range(2, col + 2):
            max = 0
            flag = 0
            for kernel in kernels:
                r = np.sum(kernel * pad[i - 2: i + 3, j - 2: j + 3])
                if r > max:
                    max = r
                    if (max >= threshold):
                        flag = 1
                        break
            if max >= threshold or flag == 1:
                nevatia_img[i - 2][j - 2] = 0
            else:
                nevatia_img[i - 2][j - 2] = 255
    return nevatia_img


img = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
robert_img = main1(img, 12)
prewitt_img = main2(img, 24)
sobel_img = main3(img, 38)
frei_and_chen_img = main4(img, 30)
krisch_img = main5(img, 135)
robinson_img = main6(img, 43)
nevatia_img = main7(img, 12500)

cv.imwrite('results/HW9_part(a)_image_robert.jpg', robert_img) #這樣寫才可以一次存全部的照片
cv.imwrite('results/HW9_part(b)_image_prewitt.jpg', prewitt_img)
cv.imwrite('results/HW9_part(c)_image_sobel.jpg', sobel_img)
cv.imwrite('results/HW9_part(d)_image_frei_and_chen.jpg', frei_and_chen_img)
cv.imwrite('results/HW9_part(e)_image_krisch.jpg', krisch_img)
cv.imwrite('results/HW9_part(f)_image_robinson.jpg', robinson_img)
cv.imwrite('results/HW9_part(g)_image_nevatia.jpg', nevatia_img)

cv.imshow('robert', robert_img)
cv.imshow('prewitt', prewitt_img)
cv.imshow('sobel', sobel_img)
cv.imshow('frei_and_chen', frei_and_chen_img)
cv.imshow('krisch', krisch_img)
cv.imshow('robinson', robinson_img)
cv.imshow('nevatia', nevatia_img)
cv.waitKey(0)