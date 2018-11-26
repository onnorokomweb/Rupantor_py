# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from Converter import NumericConversion

token = "1234.235"
numeric_conversion = NumericConversion()
bn_token = numeric_conversion.ETB(token)
bn_left, bn_right_trans = numeric_conversion.translate_right(bn_token)
print (bn_right_trans)
numeric_conversion.quantify(bn_left)
