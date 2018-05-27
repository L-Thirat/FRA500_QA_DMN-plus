# -*- coding: utf-8 -*-
import os
import google_translate
from pythainlp import word_tokenize
import codecs
from googletrans import Translator
from time import sleep

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def translate_txt(ln):
    # translator = google_translate.GoogleTranslator()
    # out = translator.translate(ln, "thai")
    try:
        translator = Translator()
        out = translator.translate(ln, dest='th')
    except:
        print("waiting next loop..")
        sleep(60) # Time in seconds.
        translator = Translator()
        out = translator.translate(ln, dest='th')
    if out:
        return u'%s'%out.text
    else:
        print("waiting next out..")
        translate_txt(ln)

def get_babi_raw(id, test_id,mode_f):
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
    path_in = '../data_translate/%s_%s.txt' % (babi_name,mode_f)
    path_out = '../data_translate/%s_%s_rewrite.txt' % (babi_name,mode_f)
    f = codecs.open(path_out, 'w',encoding='utf8')
    f_in = codecs.open(path_in, 'r',encoding='utf8')

    data = f_in.read().split(".")
    for i, line in enumerate(data):
        if"?" in line:
            line1 = "\t".join(line.split("\t")[:-1])
            print(line1)
            num = line1.split(" ")[0]
            # line1 = line1 + "\t" + ("".join(line.split("\t")[-1])).split(str(int(num)+1))[0] + "\n"
            # print(line1)
            if str(int(num)+1) in line:
                if "222" in line:
                    line1 = line1 + "\t" + "".join(("".join(line.split("\t")[-1])).split(str(int(num)+1))[:-1]) + "2\n"
                    if "222" in line1:
                        line1 = line1.replace("222","22")
                    line2 = str(int(num)+1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num)+1))[-1])[2:] + ".\n"
                elif "111" in line:
                    line1 = line1 + "\t" + "".join(("".join(line.split("\t")[-1])).split(str(int(num)+1))[:-1]) + "1\n"
                    if "111" in line1:
                        line1 = line1.replace("111","11")
                    line2 = str(int(num)+1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num)+1))[-1])[2:] + ".\n"
                elif "333" in line:
                    line1 = line1 + "\t" + "".join(("".join(line.split("\t")[-1])).split(str(int(num)+1))[:-1]) + "3\n"
                    if "333" in line1:
                        line1 = line1.replace("333","33")
                    # print(line1)
                    # asd
                    line2 = str(int(num)+1) + " " + (("".join(line.split("\t")[-1])).split(str(int(num)+1))[-1])[2:] + ".\n"
                else:
                    line1 = line1 + "\t" + "".join(("".join(line.split("\t")[-1])).split(str(int(num)+1))[:-1]) + "\n"
                    line2 = str(int(num)+1) + ("".join(line.split("\t")[-1])).split(str(int(num)+1))[-1] + ".\n"
            else:
                line1 = line1 + "\t" + "1".join(("".join(line.split("\t")[-1])).split("1")[:-1]) + "\n"
                line2 = "1" + ("".join(line.split("\t")[-1])).split("1")[-1] + ".\n"
            print(line1)
            print(line2)
            print("--------------")
            f.write(line1)
            f.write(line2)
        else:
            line1 = line + ".\n"
            print(line1)
            f.write(line1)

    # for i, line in enumerate(f_in):
    #     print(line)
    #     if not "?" in line:
    #         line = line[:-1] + ".\n"
    #     if len(line)>2:
    #         nlp_ploc = u"%s"%line
    #         nlp_ploc = nlp_ploc.replace(u" ?", u"?")
    #         nlp_ploc = nlp_ploc.replace(u"Mary  ", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"Sandra  ", u"แซนดรา")
    #         nlp_ploc = nlp_ploc.replace(u"Daniel  ", u"ดาเนียล")
    #         nlp_ploc = nlp_ploc.replace(u"John  ", u"จอร์น")
    #         nlp_ploc = nlp_ploc.replace(u"ดา เนียล", u"ดาเนียล")
    #         nlp_ploc = nlp_ploc.replace(u"ยอ ห์ น", u"จอห์น")
    #         nlp_ploc = nlp_ploc.replace(u"มา รี ย์", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"พระ แม่ มา รี", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"เจ ฟ", u"เจฟ")
    #         nlp_ploc = nlp_ploc.replace(u"ฟฟ์", u"เจฟ")
    #         nlp_ploc = nlp_ploc.replace(u"เจ ฟฟ์", u"เจฟ")
    #         nlp_ploc = nlp_ploc.replace(u"เฟ รด", u"เฟร็ด")
    #         nlp_ploc = nlp_ploc.replace(u"Fred", u"เฟร็ด")
    #         nlp_ploc = nlp_ploc.replace(u"Jeff", u"เจฟ")
    #         nlp_ploc = nlp_ploc.replace(u"Mary", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"แม รี", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"พระ แม่ แมรี่", u"แมรี่")
    #         nlp_ploc = nlp_ploc.replace(u"Bill", u"บิล")
    #         nlp_ploc = nlp_ploc.replace(u"  ", u"")
    #         nlp_ploc = nlp_ploc.replace(u"เจเจฟ", u"เจฟ")
            # f.write(nlp_ploc[:-1])
            # f.write("\n")
print(get_babi_raw("2","2","test"))
