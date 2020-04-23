# -*- coding: utf-8 -*-

import codecs
from static_data import babi_map
from core_nlp import NLPCore

nlp_core = NLPCore()


def cleaning_thai_dataset(id, test_id, mode_f):
    """Cleaning Thai dataset

    :param id: data id
    :param test_id: test id
    :param mode_f: ["train","test"] mode
    :return: None
    """
    babi_name = babi_map[id]
    path_in = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    path_out = '../data_translate_thirat/%s_%s_person_place.txt' % (babi_name, mode_f)
    f = codecs.open(path_out, 'w', encoding='utf8')
    f_in = codecs.open(path_in, 'r', encoding='utf8')

    for i, line in enumerate(f_in):
        nlp_ploc = line
        nlp_ploc = nlp_ploc

        for i in range(0, len(nlp_ploc.split(" "))):
            nlp_ploc = nlp_ploc.replace(u"  ", u" ")
        nlp_ploc = nlp_ploc.replace(u" ?", u"?")
        nlp_ploc = nlp_ploc.replace(u" .", u".")
        nlp_ploc = nlp_core.transform_name_training(nlp_ploc)

        f.write(nlp_ploc[:-1])
        f.write("\n")


print(cleaning_thai_dataset("10", "10", "test"))
