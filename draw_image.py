# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import imtools
import os
from PIL import Image

def read_target(url_csv, signal_target):
    # df = pd.read_csv(url_csv, header=3, index_col='timeunit: ps')
    df = pd.read_csv(url_csv, header=3, dtype=str)
    return df[" {0}".format(signal_target)][1:]

def skip_list(list_target, num):
    return list_target[::num]

def write_txt(url_outfile, df):
   df.to_csv(url_outfile, index=False) 

def hex_dec(df):
    df = list(map(lambda x: int(x, 16), df)) 
    return df

def detect_trigger(df):
    df = list(map(lambda x: int(x), df)) 
    num_flag = []
    for num in range(len(df)):
            if df[num] == 1:
                num_flag.append(num)
                print(num)
    return num_flag

def draw_image(filename, wrfname):
    image_res = 200 * 200
    imagebit = read_target(filename, "camcap:camcap_1|data_in_R[7..0]")
    imagebit = hex_dec(imagebit)
    trigger  = read_target(filename, "camcap:camcap_1|trig_0_R")
    start_flag = detect_trigger(trigger)
    if len(start_flag) == 0:
        print("can't find flag\nexit.........")
        exit(1)

    frame = imagebit[start_flag[0] + 1:start_flag[0] + image_res + 1]
    frame = np.array(frame)
    frame = frame.reshape((200, 200))
    print(frame)
    pilout = Image.fromarray(np.uint8(frame))
    pilout.save(wrfname)

# def cap_imageSequences(filename, wrfname):
    

if __name__ == '__main__':
    filelist = imtools.get_imlist('../stp_log/', 'csv')
    dir_path, fname = os.path.split(filelist[-1])
    name, ext = os.path.splitext(fname)
    wrfname = dir_path + "/image/" + name + ".jpg"
    print(wrfname)
    draw_image(filelist[-1], wrfname)

