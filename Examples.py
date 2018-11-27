# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from Converter import Rupantor

rupantor = Rupantor()
token = "54687021"
token_bn = rupantor.english_to_bangla_numericals(token)
print("{}: {}".format(token, token_bn))
