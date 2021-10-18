import cv2
import glob
import os
import csv

path_data = os.getcwd()
input_path = path_data + '\data'
output_path = path_data + '\cutdata'

for file in glob.glob(input_path+'\*.jpg'):
    img = cv2.imread(file)
    h, w, d = img.shape
    filename = file.replace(input_path, '')
    cut_indexes = {'top': 0, 'under': 0, 'left': 0, 'right': 0}
    # top
    for y in range(h):
        b_sum, g_sum, r_sum = 0, 0, 0
        for x in range(w):
            c = img[y, x]
            b_sum += c[0]
            g_sum += c[1]
            r_sum += c[2]
        b_ave = b_sum / w
        g_ave = g_sum / w
        r_ave = r_sum / w
        if r_ave-5 >= b_ave and r_ave-5 >= g_ave and r_ave >= 50:
            break
        else:
            cut_indexes['top'] = y
    # under
    cut_indexes['under'] = h
    for y in range(h):
        b_sum, g_sum, r_sum = 0, 0, 0
        for x in range(w):
            c = img[y, x]
            b_sum += c[0]
            g_sum += c[1]
            r_sum += c[2]
        b_ave = b_sum / w
        g_ave = g_sum / w
        r_ave = r_sum / w
        if r_ave-5 >= b_ave and r_ave-5 >= g_ave and r_ave >= 50:
            break
        else:
            cut_indexes['under'] = h-y-1
    # left
    for x in range(w):
        b_sum, g_sum, r_sum = 0, 0, 0
        for y in range(h):
            c = img[y, x]
            b_sum += c[0]
            g_sum += c[1]
            r_sum += c[2]
        b_ave = b_sum / h
        g_ave = g_sum / h
        r_ave = r_sum / h
        if r_ave-5 >= b_ave and r_ave-5 >= g_ave and r_ave >= 50:
            break
        else:
            cut_indexes['left'] = x

    # right
    cut_indexes['right'] = w
    for x in range(w):
        b_sum, g_sum, r_sum = 0, 0, 0
        for y in range(h):
            c = img[y, x]
            b_sum += c[0]
            g_sum += c[1]
            r_sum += c[2]
        b_ave = b_sum / h
        g_ave = g_sum / h
        r_ave = r_sum / h
        if r_ave-5 >= b_ave and r_ave-5 >= g_ave and r_ave >= 50:
            break
        else:
            cut_indexes['right'] = w-x-1
    print(h, w)
    print(cut_indexes)
    cut_image = img[cut_indexes['top']:cut_indexes['under'], cut_indexes['left']:cut_indexes['right']]

    print(output_path+filename)
    cv2.imwrite(output_path+filename, cut_image)


