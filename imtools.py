#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
def get_imlist(path, extention):
    """ pathに指定されたディレクトリの全てのjpgファイル名をリストに返す """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(extention)]

def imresize(im, sz):
    """PILを使って画像配列のサイズを変更する"""
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))
