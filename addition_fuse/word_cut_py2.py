#-*-coding: utf-8 -*-
'''
care only the word in list with LexTO : Longest word
usage : cut(word) return กินข้าว|ยัง
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
class cut_cut:
    def __init__(self):
        f_name_read = "data_generate/wordbank/mylibrary.txt"
        f_word_read = codecs.open(f_name_read, 'r',encoding='utf8')
        str_f = f_word_read.read()
        sort_list = (sorted(str_f.split('\n'), key=len))
        self.sort_list = self.reverse_list(sort_list)
        # self.temp_word = []

    def reverse_list(self,inp):
        temp=[]
        for i in reversed(inp):
            temp.append(i)
        return temp

    def re_order_word(self,orig,new):
        # print orig
        temp_order = []
        new_word_order = []
        print orig
        for item in new:
            print(item)
            asd
            temp_order.append(orig.index(item))
        # print (temp_order)
        # print (sorted(temp_order))
        for i in sorted(temp_order):
            for item in new:
                if orig.index(item)==i:
                    new_word_order.append(item)
                    try:
                        check_eng = True
                        # print orig[0*3:3*3]
                        # print (orig[i*3:3*temp_order[((sorted(temp_order)).index(i))+1]]).replace(item,'')
                        for stri in (orig[3*i:3*temp_order[((sorted(temp_order)).index(i))+1]]):
                            if (ord(stri)>ord('a') and ord(stri)<ord('z')) or\
                                    (ord(stri)>ord('A') and ord(stri)<ord('Z')):
                                check_eng = False
                        if check_eng:
                            new_word_order.append((orig[3*i:3*temp_order[((sorted(temp_order)).index(i))+1]]).replace(item,''))
                    except:pass
        #print(new_word_order)
        return new_word_order

    def cut(self,word):
        temp_word = []
        copy_word = word
        for ch in self.sort_list:
            # print(ch,word)
            if ch[:-3] in word[:-1]:
                # print(ch,word)
                word = word.replace(ch,"-")
                temp_word.append(ch)
        # print(temp_word)
        # asd
        cut_theword = self.re_order_word(copy_word,temp_word)
        output = '|'.join(cut_theword)
        output = output.replace('||',"|")
        return output

    # def cut_export_file(input_f,output_f):
    #     f_name_read=input_f
    #     f_word_read = codecs.open(f_name_read, 'r')
    #     str_f = f_word_read.read()


## test ##
if __name__ == "__main__":
    print (cut_cut().cut(u"กินข้าวยัง"))
