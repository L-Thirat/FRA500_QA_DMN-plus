# -*- coding: utf-8 -*-

from pythainlp import word_tokenize
import codecs
from static_data import babi_map
from core_nlp import NLPCore

nlp_core = NLPCore()


def translate_data_2factor(id, test_id, mode_f):
    babi_name = babi_map[id]
    path_train = '../data/en-10k/%s_%s.txt' % (babi_name, mode_f)
    path_output = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    f = codecs.open(path_output, 'w', encoding='utf8')
    for i, line in enumerate(open(path_train)):
        text = nlp_core.translate_txt(line[:-1])
        nlp_ploc = " ".join(word_tokenize(text, engine='newmm'))
        nlp_ploc = nlp_core.transform_name(nlp_ploc)

        f.write(nlp_ploc)
        f.write('\n')


if __name__ == "__main__":
    print(translate_data_2factor("3", "3", "train"))
