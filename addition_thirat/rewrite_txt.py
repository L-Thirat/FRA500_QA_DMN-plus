# -*- coding: utf-8 -*-

import os
import google_translate
import codecs
from googletrans import Translator
from pythainlp import word_tokenize
from time import sleep
from core_nlp import translate_txt
from static_data import babi_map


def get_babi_raw(id, test_id, mode_f):
    babi_name = babi_map[id]
    path_in = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    path_out = '../data_translate_thirat/%s_%s_rewrite.txt' % (babi_name, mode_f)
    f = codecs.open(path_out, 'w', encoding='utf8')
    f_in = codecs.open(path_in, 'r', encoding='utf8')

    data = f_in.read().split(".")
    for i, line in enumerate(data):
        if "?" in line:
            line1 = "\t".join(line.split("\t")[:-1])
            num = line1.split(" ")[0]
            if str(int(num) + 1) in line:
                if "222" in line:
                    line1 = line1 + "\t" + "".join(
                        ("".join(line.split("\t")[-1])).split(str(int(num) + 1))[:-1]) + "2\n"
                    if "222" in line1:
                        line1 = line1.replace("222", "22")
                    line2 = str(int(num) + 1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num) + 1))[-1])[
                                                      2:] + ".\n"
                elif "111" in line:
                    line1 = line1 + "\t" + "".join(
                        ("".join(line.split("\t")[-1])).split(str(int(num) + 1))[:-1]) + "1\n"
                    if "111" in line1:
                        line1 = line1.replace("111", "11")
                    line2 = str(int(num) + 1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num) + 1))[-1])[
                                                      2:] + ".\n"
                elif "333" in line:
                    line1 = line1 + "\t" + "".join(
                        ("".join(line.split("\t")[-1])).split(str(int(num) + 1))[:-1]) + "3\n"
                    if "333" in line1:
                        line1 = line1.replace("333", "33")
                    line2 = str(int(num) + 1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num) + 1))[-1])[
                                                      2:] + ".\n"
                else:
                    line1 = line1 + "\t" + "".join(("".join(line.split("\t")[-1])).split(str(int(num) + 1))[:-1]) + "\n"
                    line2 = str(int(num) + 1) + ("".join(line.split("\t")[-1])).split(str(int(num) + 1))[-1] + ".\n"
            else:
                line1 = line1 + "\t" + "1".join(("".join(line.split("\t")[-1])).split("1")[:-1]) + "\n"
                line2 = "1" + ("".join(line.split("\t")[-1])).split("1")[-1] + ".\n"
            f.write(line1)
            f.write(line2)
        else:
            line1 = line + ".\n"
            f.write(line1)


print(get_babi_raw("2", "2", "test"))
