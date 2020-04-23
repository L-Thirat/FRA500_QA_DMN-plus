# -*-coding: utf-8 -*-

"""
care only the word in list with LexTO : Longest word
usage : cut(word) return กินข้าว|ยัง
"""

import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class WordSegmentation:
    """Word Segmentation"""
    def __init__(self):
        f_name_read = "data_generate/wordbank/mylibrary.txt"
        f_word_read = codecs.open(f_name_read, 'r', encoding='utf8')
        str_f = f_word_read.read()
        sort_list = (sorted(str_f.split('\n'), key=len))
        self.sort_list = self.reverse_list(sort_list)

    @staticmethod
    def reverse_list(lst):
        """Reverse item in list

        :param lst: list items
        :return: list reversed
        """
        reverse_list = []
        for item in reversed(lst):
            reverse_list.append(item)
        return reverse_list

    @staticmethod
    def re_order_word(origin_item, new_item):
        """Reorder of word
        
        :param origin_item: Original item
        :param new_item: Item generated
        :return: 
        """
        temp_order = []
        new_item_word_order = []
        for item in new_item:
            temp_order.append(origin_item.index(item))

        for i in sorted(temp_order):
            for item in new_item:
                if origin_item.index(item) == i:
                    new_item_word_order.append(item)
                    try:
                        check_eng = True
                        for stri in (origin_item[3 * i:3 * temp_order[((sorted(temp_order)).index(i)) + 1]]):
                            if (ord(stri) > ord('a') and ord(stri) < ord('z')) or \
                                    (ord(stri) > ord('A') and ord(stri) < ord('Z')):
                                check_eng = False
                        if check_eng:
                            new_item_word_order.append(
                                (origin_item[3 * i:3 * temp_order[((sorted(temp_order)).index(i)) + 1]]).replace(item, ''))
                    except:
                        pass
        return new_item_word_order

    def cut(self, word):
        """Word Segment function

        :param word: Word
        :return: Word segmented
        """
        temp_word = []
        copy_word = word
        for ch in self.sort_list:
            if ch[:-3] in word[:-1]:
                word = word.replace(ch, "-")
                temp_word.append(ch)
        cut_theword = self.re_order_word(copy_word, temp_word)
        output = '|'.join(cut_theword)
        output = output.replace('||', "|")
        return output


if __name__ == "__main__":
    print(WordSegmentation().cut(u"กินข้าวยัง"))
