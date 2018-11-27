# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from Converter import Rupantor

rupantor = Rupantor()
en_number = "25478.2366"

'''
Conversion in Words in Bangla From English Decimals

'''

token_bn = rupantor.ETB_Words(en_number)
print("{}: {}".format(en_number, token_bn))

'''
Convert to English

'''

bn_number = rupantor.ETB_Numericals(en_number)
print("{} : {}".format(en_number, bn_number))
