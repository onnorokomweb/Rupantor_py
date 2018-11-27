# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import os
import codecs
import json

base_path = os.path.dirname(__name__)
Dict_Path = os.path.abspath(os.path.join(base_path, 'res/helper.json'))

char_map = json.load(codecs.open(Dict_Path, "r", "utf-8"))
NUM_DICT_LEFT = char_map["num_dict_left"]
NUM_DICT_RIGHT = char_map["num_dict_right"]
ETB_NUM_CON = char_map["etb_num"]
POSITONAL_DICT = char_map["positional_dict"]
