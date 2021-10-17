import cv2
import glob
import os
import csv

path_data = os.getcwd()
print(path_data)
path_data += '\data'
print(path_data)

with open('RGBValue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['B', 'G', 'R', 'Label'])
    for file in glob.glob(path_data+'\*.jpg'):
        print(file)
        a_or_o = file.replace(path_data, '')[1]
        img = cv2.imread(file)
        h, w, d = img.shape
        num_pixel = h*w
        b_sum, g_sum, r_sum = 0, 0, 0
        for y in range(h):
            for x in range(w):
                c = img[y, x]
                b_sum += c[0]
                g_sum += c[1]
                r_sum += c[2]
        b_ave = b_sum / num_pixel
        g_ave = g_sum / num_pixel
        r_ave = r_sum / num_pixel
        print('B: ', b_ave, 'G: ', g_ave, 'R: ', r_ave)
        writer.writerow([b_ave, g_ave, r_ave, a_or_o])

    
    

