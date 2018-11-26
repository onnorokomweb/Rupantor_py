# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from MapLoader import NUM_DICT, ETB_NUM_CON

"""
12,23,45,23,2

"""


class NumericConversion:
    def __init__(self):
        self.num_dict = NUM_DICT
        self.etb_num = ETB_NUM_CON

    def ETB(self, token):
        char_list = list(token)
        bn_char_list = []
        for char in char_list:
            try:
                bn_char_list.append(self.etb_num[char])
            except KeyError:
                bn_char_list.append("#")
        bn_token = "".join(bn_char_list)
        return bn_token

    def translate_right(self, bn_token):
        bn_right = bn_token.split(".")[1]
        bn_left = bn_token.split(".")[0]
        bn_temp = ["দশমিক"]
        for char in bn_right:
            try:
                bn_temp.append(self.num_dict[char])
            except KeyError:
                bn_temp.append("#")
        bn_right_translation = " ".join(bn_temp)
        return bn_left, bn_right_translation

    def quantify(self, bn_token_left):
        bn_token_rev = (str(bn_token_left))[::-1]
        bn_token_padded = str(bn_token_rev).ljust(10, "০")
        print(bn_token_padded)
        pass
