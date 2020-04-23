# -*- coding: utf-8 -*-
import os
import google_translate
import codecs
from googletrans import Translator
from time import sleep
from static_data import babi_map
from pythainlp import word_tokenize
from core_nlp.NLPCore import transform_name, translate_txt


def get_babi_raw(id, test_id, mode_f):
    babi_name = babi_map[id]
    path_train = '../data/en-10k/%s_%s.txt' % (babi_name, mode_f)
    path_out = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    f = codecs.open(path_out, 'w', encoding='utf8')
    for i, line in enumerate(open(path_train)):
        text = translate_txt(line[:-2])
        proc = word_tokenize(text, engine='newmm')
        if '?' in line:
            if represent_int(proc[0]):
                if represent_int(proc[-1]):
                    nlp_ploc = (''.join(proc[:2])) + (' '.join(proc[2:-4])) + " \t" + proc[-3] + "\t" + \
                               line.split("\t")[-1]
                else:
                    nlp_ploc = (''.join(proc[:2])) + (' '.join(proc[2:-2])) + " \t" + proc[-1] + "\t" + \
                               line.split("\t")[-1]
            else:
                if represent_int(proc[-1]):
                    if "?" not in proc:
                        nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[:-4])) + "? \t" + proc[-3] + "\t" + \
                                   line.split("\t")[-1]
                    else:
                        nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[:-4])) + " \t" + proc[-3] + "\t" + \
                                   line.split("\t")[-1]
                else:
                    if "?" not in proc:
                        nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[:-2])) + "? \t" + proc[-1] + "\t" + \
                                   line.split("\t")[-1]
                    else:
                        nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[:-2])) + " \t" + proc[-1] + "\t" + \
                                   line.split("\t")[-1]
        else:
            if represent_int(proc[0]):
                print(' '.join(proc[2:]))
                nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[2:])) + "."
            else:
                nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc)) + "."
        if "\n" in nlp_ploc:
            nlp_ploc = nlp_ploc[:-1]

        nlp_ploc = transform_name(nlp_ploc)

        f.write(nlp_ploc)
        f.write('\n')


print(get_babi_raw("10", "10", "train"))
