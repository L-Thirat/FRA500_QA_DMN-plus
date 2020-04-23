# -*- coding: utf-8 -*-

import os
import google_translate
from pythainlp import word_tokenize
import codecs
from googletrans import Translator
from time import sleep
from static_data import babi_map
from core_nlp import loop_translate, transform_name


def get_babi_raw(id, test_id, mode_f):
    babi_name = babi_map[id]
    path_train = '../data/en-10k/%s_%s.txt' % (babi_name, mode_f)
    path_output = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    f = codecs.open(path_output, 'w', encoding='utf8')
    for i, line in enumerate(open(path_train)):
        text = translate_txt(line[:-1])
        nlp_ploc = " ".join(word_tokenize(text, engine='newmm'))
        nlp_ploc = transform_name(nlp_ploc)

        f.write(nlp_ploc)
        f.write('\n')


print(get_babi_raw("3", "3", "train"))
