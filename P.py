# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from Converter import NumericConversion

token = "20132104.2035"
numeric_conversion = NumericConversion()

bn_token = numeric_conversion.ETB(token)
bn_left, bn_right_trans = numeric_conversion.translate_right(bn_token)
print(bn_right_trans)
tokens = numeric_conversion.quantify(bn_left)
be_left_trans = numeric_conversion.translate_left_two(tokens)
print(be_left_trans)

