# -*- coding: utf-8 -*-

import codecs
from static_data import babi_map
from pythainlp import word_tokenize
from core_nlp import NLPCore

nlp_core = NLPCore()


def translate_data(id, test_id, mode_f):
    """Translate data

    :param id: dataset id
    :param test_id: test id
    :param mode_f: ["train","test"] mode
    :return: data translated
    """
    babi_name = babi_map[id]
    path_train = '../data/en-10k/%s_%s.txt' % (babi_name, mode_f)
    path_out = '../data_translate_thirat/%s_%s.txt' % (babi_name, mode_f)
    f = codecs.open(path_out, 'w', encoding='utf8')
    for i, line in enumerate(open(path_train)):
        text = nlp_core.translate_txt(line[:-2])
        proc = word_tokenize(text, engine='newmm')
        if '?' in line:
            if nlp_core.represent_int(proc[0]):
                if nlp_core.represent_int(proc[-1]):
                    nlp_ploc = (''.join(proc[:2])) + (' '.join(proc[2:-4])) + " \t" + proc[-3] + "\t" + \
                               line.split("\t")[-1]
                else:
                    nlp_ploc = (''.join(proc[:2])) + (' '.join(proc[2:-2])) + " \t" + proc[-1] + "\t" + \
                               line.split("\t")[-1]
            else:
                if nlp_core.represent_int(proc[-1]):
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
            if nlp_core.represent_int(proc[0]):
                nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc[2:])) + "."
            else:
                nlp_ploc = line.split(" ")[0] + " " + (' '.join(proc)) + "."
        if "\n" in nlp_ploc:
            nlp_ploc = nlp_ploc[:-1]

        nlp_ploc = nlp_core.transform_name(nlp_ploc)

        f.write(nlp_ploc)
        f.write('\n')


if __name__ == "__main__":
    print(translate_data("10", "10", "train"))
