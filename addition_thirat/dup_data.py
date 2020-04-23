# -*- coding: utf-8 -*-\

import os
import codecs
from time import sleep
from pythainlp import word_tokenize


def get_babi_raw(id, test_id, mode_f, dup):
    """create babi dataset in Thai language

    :param id: data id
    :param test_id: test id
    :param mode_f: ["train","test"] mode
    :param dup: name of duplicate data
    :return:
    """
    babi_map = {
        "1": "qa1_single-supporting-fact",
        "2": "qa2_two-supporting-facts",
        "3": "qa3_three-supporting-facts",
        "4": "qa4_two-arg-relations",
        "5": "qa5_three-arg-relations",
        "6": "qa6_yes-no-questions",
        "7": "qa7_counting",
        "8": "qa8_lists-sets",
        "9": "qa9_simple-negation",
        "10": "qa10_indefinite-knowledge",
        "11": "qa11_basic-coreference",
        "12": "qa12_conjunction",
        "13": "qa13_compound-coreference",
        "14": "qa14_time-reasoning",
        "15": "qa15_basic-deduction",
        "16": "qa16_basic-induction",
        "17": "qa17_positional-reasoning",
        "18": "qa18_size-reasoning",
        "19": "qa19_path-finding",
        "20": "qa20_agents-motivations",
        "MCTest": "MCTest",
        "19changed": "19changed",
        "joint": "all_shuffled",
        "sh1": "../shuffled/qa1_single-supporting-fact",
        "sh2": "../shuffled/qa2_two-supporting-facts",
        "sh3": "../shuffled/qa3_three-supporting-facts",
        "sh4": "../shuffled/qa4_two-arg-relations",
        "sh5": "../shuffled/qa5_three-arg-relations",
        "sh6": "../shuffled/qa6_yes-no-questions",
        "sh7": "../shuffled/qa7_counting",
        "sh8": "../shuffled/qa8_lists-sets",
        "sh9": "../shuffled/qa9_simple-negation",
        "sh10": "../shuffled/qa10_indefinite-knowledge",
        "sh11": "../shuffled/qa11_basic-coreference",
        "sh12": "../shuffled/qa12_conjunction",
        "sh13": "../shuffled/qa13_compound-coreference",
        "sh14": "../shuffled/qa14_time-reasoning",
        "sh15": "../shuffled/qa15_basic-deduction",
        "sh16": "../shuffled/qa16_basic-induction",
        "sh17": "../shuffled/qa17_positional-reasoning",
        "sh18": "../shuffled/qa18_size-reasoning",
        "sh19": "../shuffled/qa19_path-finding",
        "sh20": "../shuffled/qa20_agents-motivations",
    }
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
        nlp_ploc = transform_name(nlp_ploc)
        for val in dict_val.keys():
            nlp_ploc = nlp_ploc.replace(val, dict_val[val])

        f.write(nlp_ploc[:-1])
        f.write("\n")
        print(nlp_ploc)


def transform_name(nlp_ploc):
    nlp_ploc = nlp_ploc.replace(u"แซ น ด ร้า", u"แซนดรา")
    nlp_ploc = nlp_ploc.replace(u"ดา เนีย ล", u"ดาเนียล ")
    nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
    nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
    nlp_ploc = nlp_ploc.replace(u"สำนักงาน", u"ออฟฟิศ ")
    nlp_ploc = nlp_ploc.replace(u"ที่ทำงาน", u"ออฟฟิศ ")
    nlp_ploc = nlp_ploc.replace(u"ห้องครัว", u"ครัว ")
    nlp_ploc = nlp_ploc.replace(u"ก ลับ", u"กลับ")

    nlp_ploc = nlp_ploc.replace(u" \tที่", u" \tไม่")
    nlp_ploc = nlp_ploc.replace(u" \tบางที", u" \tอาจจะ")
    for i in range(0, len(nlp_ploc.split(" "))):
        nlp_ploc = nlp_ploc.replace(u"  ", u" ")
    nlp_ploc = nlp_ploc.replace(u" ?", u"?")
    nlp_ploc = nlp_ploc.replace(u" .", u".")
    return nlp_ploc


dup_name = [u"มาค", u"ติ๋ม", u"โจ", u"เจ", u"โม", u"โบว", u"เฟิร์น"]
for d_name in range(0, len(dup_name)):
    new_dup_seq = dup_name
    temp = new_dup_seq[0]
    del new_dup_seq[0]
    new_dup_seq.append(temp)
