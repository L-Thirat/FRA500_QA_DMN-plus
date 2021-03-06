# -*- coding: utf-8 -*-\

import codecs
from core_nlp import NLPCore
from static_data import babi_map

nlp_core = NLPCore()


def duplicate_training_set(id, test_id, mode_f, dup):
    """Generate new training set by duplicate and replace name

    :param id: dataset id
    :param test_id: test id
    :param mode_f: ["train","test"] mode
    :param dup: set of data replaced
    :return:
    """
    babi_name = babi_map[id]
    path_in = '../data_translate_thirat/%s_%s_rewrite.txt' % (babi_name, mode_f)
    path_out = '../data_translate_thirat/%s_%s_person_%s.txt' % (babi_name, mode_f, dup[0])
    f = codecs.open(path_out, 'w', encoding='utf8')
    f_in = codecs.open(path_in, 'r', encoding='utf8')

    original_name = [u"แซนดรา", u"แมรี่", u"จอห์น", u"ดาเนียล", u"จูลี่", u"บิล", u"เฟร็ด"]
    dict_val = {}
    for i, name in enumerate(original_name):
        dict_val[name] = dup[i]

    for i, line in enumerate(f_in):
        nlp_ploc = line
        nlp_ploc = nlp_core.transform_name(nlp_ploc)
        for val in dict_val.keys():
            nlp_ploc = nlp_ploc.replace(val, dict_val[val])

        f.write(nlp_ploc[:-1])
        f.write("\n")


if __name__ == "__main__":
    dup_name = [u"มาค", u"ติ๋ม", u"โจ", u"เจ", u"โม", u"โบว", u"เฟิร์น"]
    for d_name in range(0, len(dup_name)):
        new_dup_seq = dup_name
        temp = new_dup_seq[0]
        del new_dup_seq[0]
        new_dup_seq.append(temp)
    duplicate_training_set("2", "2", "train", new_dup_seq)
