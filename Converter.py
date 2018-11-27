# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 11/27/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from MapLoader import NUM_DICT_RIGHT, ETB_NUM_CON, NUM_DICT_LEFT, POSITONAL_DICT


class NumericConversion:
    def __init__(self):
        self.num_dict_right = NUM_DICT_RIGHT
        self.etb_num = ETB_NUM_CON
        self.positional_dictionary = POSITONAL_DICT
        self.num_dict_left = NUM_DICT_LEFT

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
        try:
            bn_right = bn_token.split(".")[1]
        except IndexError:
            return bn_token, ""
        bn_left = bn_token.split(".")[0]
        bn_temp = ["দশমিক"]
        for char in bn_right:
            try:
                bn_temp.append(self.num_dict_right[char])
            except KeyError:
                bn_temp.append("#")
        bn_right_translation = " ".join(bn_temp)
        return bn_left, bn_right_translation

    def quantify(self, bn_token_left):
        bn_token_rev = (str(bn_token_left))[::-1]
        bn_token_rev_padded = str(bn_token_rev).ljust(16, "০")

        slicers = [2, 1, 2, 2, 2, 1, 2, 2, 2]

        tokens = []
        for index, slicer in enumerate(slicers):
            temp = bn_token_rev_padded[:slicer]
            temp_rev = str(temp)[::-1]
            bn_token_rev_padded = bn_token_rev_padded[slicer:]
            tokens.append(temp_rev)

        return tokens

    def translate_left(self, tokens):
        temp = []
        for index, token in enumerate(tokens):
            if (token == "০০" or token == "০") and (index == 4 or index == 8):
                token_tr = "{}".format(self.positional_dictionary[str(index)])
                temp.append(token_tr)
            else:
                if token == "০০" or token == "০":
                    pass
                else:
                    token_tr = "{} {} ".format(self.num_dict_left[token], self.positional_dictionary[str(index)])
                    temp.append(token_tr)
        temp_rev = temp[::-1]
        be_tr_left = "".join(temp_rev)
        return be_tr_left

    def translate_left_two(self, tokens):
        rev_tokens = tokens[::-1]

        pointer = None
        temp = []
        for index, token in enumerate(rev_tokens):
            if token in self.num_dict_left.keys():
                pointer = index
                break

        clean_tokens = rev_tokens[pointer:]
        clean_tokens_rev = clean_tokens[::-1]

        for indxx, token in enumerate(clean_tokens_rev):
            if token == "০০" or token == "০":
                pass
            else:
                token_tr = "{} {} ".format(self.num_dict_left[token], self.positional_dictionary[str(indxx)])
                temp.append(token_tr)
        temp_rev = temp[::-1]
        be_tr_left = "".join(temp_rev)

        return (be_tr_left)


class Rupantor:
    def __init__(self):
        pass

    @staticmethod
    def english_to_bangla_numericals(token):
        numeric_conversion = NumericConversion()
        bn_token = numeric_conversion.ETB(token)
        bn_left, bn_right_trans = numeric_conversion.translate_right(bn_token)

        tokens = numeric_conversion.quantify(bn_left)
        be_left_trans = numeric_conversion.translate_left_two(tokens)

        total_conversion = "{}{}".format(be_left_trans, bn_right_trans)
        return total_conversion
