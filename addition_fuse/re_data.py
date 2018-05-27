# -*- coding: utf-8 -*-
import os
# import google_translate
from pythainlp import word_tokenize
import codecs
# from googletrans import Translator
from time import sleep

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#
# def translate_txt(ln):
#     # translator = google_translate.GoogleTranslator()
#     # out = translator.translate(ln, "thai")
#     try:
#         translator = Translator()
#         out = translator.translate(ln, dest='th')
#     except:
#         print("waiting next loop..")
#         sleep(60) # Time in seconds.
#         translator = Translator()
#         out = translator.translate(ln, dest='th')
#     if out:
#         return u'%s'%out.text
#     else:
#         print("waiting next out..")
#         translate_txt(ln)

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
    path_out = '../data_translate/%s_%s_person_place.txt' % (babi_name,mode_f)
    f = codecs.open(path_out, 'w',encoding='utf8')
    f_in = codecs.open(path_in, 'r',encoding='utf8')
    # for i, line in enumerate(f_in):
        # print(line)
    # asd
    # data = f_in.read().split("\n")
    for i, line in enumerate(f_in):
        nlp_ploc = line
        #edit name
        nlp_ploc = nlp_ploc.replace(u"แซ น ด ร้า", u"แซนดรา")
        nlp_ploc = nlp_ploc.replace(u"ดา เนีย ล", u"ดาเนียล ")
        nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ที่ทำงาน", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ก ลับ", u"กลับ")

        nlp_ploc = nlp_ploc.replace(u" \tที่",u" \tไม่")
        nlp_ploc = nlp_ploc.replace(u" \tบางที",u" \tอาจจะ")
        #name
        nlp_ploc = nlp_ploc.replace(u"แซนดรา", u"มาค")
        nlp_ploc = nlp_ploc.replace(u"แมรี่", u"ติ๋ม")
        nlp_ploc = nlp_ploc.replace(u"จอห์น", u"เจ")
        nlp_ploc = nlp_ploc.replace(u"ดาเนียล", u"โจ")
        nlp_ploc = nlp_ploc.replace(u"จูลี่", u"โม")
        nlp_ploc = nlp_ploc.replace(u"บิล", u"โบว")
        nlp_ploc = nlp_ploc.replace(u"เฟร็ด", u"เฟิร์น")

        #verb
        # nlp_ploc = nlp_ploc.replace(u"เดิน ", u"บิน ")
        # nlp_ploc = nlp_ploc.replace(u"ไป ", u"ไปยัง ")
        # nlp_ploc = nlp_ploc.replace(u"เดินทาง", u"พุ่งตรง")
        # nlp_ploc = nlp_ploc.replace(u"เข้าไป", u"แวะไป")
        # nlp_ploc = nlp_ploc.replace(u"กลับไป", u"หลบ")
        # nlp_ploc = nlp_ploc.replace(u"ย้าย", u"หนี")
        # nlp_ploc = nlp_ploc.replace(u"เสด็จ", u"มุ่ง")

        # nlp_ploc = nlp_ploc.replace(u"เดิน", u"")
        # nlp_ploc = nlp_ploc.replace(u"เดินทาง", u"")
        # nlp_ploc = nlp_ploc.replace(u"เข้า", u"")
        # nlp_ploc = nlp_ploc.replace(u"กลับ", u"")
        # nlp_ploc = nlp_ploc.replace(u"ย้าย", u"")
        # nlp_ploc = nlp_ploc.replace(u"เสด็จ", u"")
        # nlp_ploc = nlp_ploc.replace(u"ที่", u"")
        # nlp_ploc = nlp_ploc.replace(u"ยัง", u"")
        # nlp_ploc = nlp_ploc.replace(u"กับ", u"")
        # nlp_ploc = nlp_ploc.replace(u"ขึ้น", u"")
        # nlp_ploc = nlp_ploc.replace(u"ไว้", u"")
        # nlp_ploc = nlp_ploc.replace(u"นั่น", u"")
        # nlp_ploc = nlp_ploc.replace(u"แก่", u"")
        # nlp_ploc = nlp_ploc.replace(u"ลง", u"")
        # nlp_ploc = nlp_ploc.replace(u"ท อดนม", u"วาง นม")
        # nlp_ploc = nlp_ploc.replace(u"รับ", u"")
        # nlp_ploc = nlp_ploc.replace(u"น้ำนม", u"นม")

        #place
        nlp_ploc = nlp_ploc.replace(u"ห้องโถง", u"ภูเก็ต")
        nlp_ploc = nlp_ploc.replace(u"ห้องน้ำ", u"สงขลา")
        nlp_ploc = nlp_ploc.replace(u"ห้องอาบน้ำ", u"พะเยา")
        nlp_ploc = nlp_ploc.replace(u"ห้องครัว", u"สตูล")
        nlp_ploc = nlp_ploc.replace(u"ครัว", u"สตูล")
        nlp_ploc = nlp_ploc.replace(u"สวน", u"เชียงใหม่")
        nlp_ploc = nlp_ploc.replace(u"ออฟฟิศ", u"เชียงราย")
        nlp_ploc = nlp_ploc.replace(u"สำนักงาน", u"เชียงราย")
        nlp_ploc = nlp_ploc.replace(u"ห้องนอน", u"อุบล")
        nlp_ploc = nlp_ploc.replace(u"ลาน", u"กรุงเทพ")
        nlp_ploc = nlp_ploc.replace(u"โรงเรียน", u"ตรัง")
        nlp_ploc = nlp_ploc.replace(u"สวนสาธารณะ", u"เชียงใหม่")
        # nlp_ploc = nlp_ploc.replace(u"โรงหนัง", u"ตรัง")
        nlp_ploc = nlp_ploc.replace(u"โรงภาพยนตร์", u"โรงหนัง")


        # from pythainlp.corpus import stopwords
        print(nlp_ploc)
        # words = [u"ที่",u"พุ่งตรง",u"แวะ",u"หนี"]
        # exp = [u"มา"]
        # for word in words:
        #     # print(word)
        #     if word not in exp:
        #         nlp_ploc = nlp_ploc.replace(word,u"")
        for i in range (0,len(nlp_ploc.split(" "))):
            nlp_ploc = nlp_ploc.replace(u"  ", u" ")
        nlp_ploc = nlp_ploc.replace(u" ?", u"?")
        nlp_ploc = nlp_ploc.replace(u" .", u".")
        print(nlp_ploc)

        # if "?" in nlp_ploc:
        #     f.write(nlp_ploc)
        #
        # else:
        f.write(nlp_ploc[:-1])
        f.write("\n")
        print(nlp_ploc)
print(get_babi_raw("10","10","test"))
