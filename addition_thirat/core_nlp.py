# coding=utf-8


class NLPCore:
    def __init__(self):
        pass

    @staticmethod
    def represent_int(s):
        """Check integer format

        :param s: string
        :return: True if string in integer format, False if not
        """
        try:
            int(s)
            return True
        except ValueError:
            return False

    def translate_txt(self,txt):
        """Translation pipeline

        :param txt: text
        :return: text translated
        """
        try:
            output = self.loop_translate(txt)
        except:
            print("waiting next loop..")
            sleep(60)  # Time in seconds.
            output = self.loop_translate(txt)
        if output:
            return u'%s' % output
        else:
            print("waiting next output..")
            translate_txt(txt)

    @staticmethod
    def loop_translate(txt):
        """Loop to translate

        :param txt: text
        :return: text translated
        """
        num = txt.split(" ")[0]
        output = "%s" % str(num)
        translator = Translator()
        if "?" in txt:
            sentence = " ".join(txt.split("?")[0].split(" ")[1:])
            output = output + " " + translator.translate(sentence, dest='th').text
            ans = txt.split("? \t")[1].split("\t")[0]
            output = output + "? \t" + translator.translate(ans, dest='th').text
            ending = txt.split("? \t")[1].split("\t")[1]
            output = output + "\t" + ending
        else:
            sentence = " ".join(txt.split(" ")[1:])
            output = output + " " + translator.translate(sentence, dest='th').text + "."
        return output

    @staticmethod
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

        nlp_ploc = nlp_ploc.replace(u"Mary  ", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"Sandra  ", u"แซนดรา")
        nlp_ploc = nlp_ploc.replace(u"Daniel  ", u"ดาเนียล")
        nlp_ploc = nlp_ploc.replace(u"John  ", u"จอร์น")
        nlp_ploc = nlp_ploc.replace(u"ดา เนียล", u"ดาเนียล")
        nlp_ploc = nlp_ploc.replace(u"ยอ ห์ น", u"จอห์น")
        nlp_ploc = nlp_ploc.replace(u"มา รี ย์", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"พระ แม่ มา รี", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"เจ ฟ", u"เจฟ")
        nlp_ploc = nlp_ploc.replace(u"ฟฟ์", u"เจฟ")
        nlp_ploc = nlp_ploc.replace(u"เจ ฟฟ์", u"เจฟ")
        nlp_ploc = nlp_ploc.replace(u"เฟ รด", u"เฟร็ด")
        nlp_ploc = nlp_ploc.replace(u"Fred", u"เฟร็ด")
        nlp_ploc = nlp_ploc.replace(u"Jeff", u"เจฟ")
        nlp_ploc = nlp_ploc.replace(u"Mary", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"แม รี", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"พระ แม่ แมรี่", u"แมรี่")
        nlp_ploc = nlp_ploc.replace(u"Bill", u"บิล")
        nlp_ploc = nlp_ploc.replace(u"Julie", u"จูลี่")
        nlp_ploc = nlp_ploc.replace(u"จู ลี", u"จูลี่")
        nlp_ploc = nlp_ploc.replace(u"  ", u"")
        nlp_ploc = nlp_ploc.replace(u"เจเจฟ", u"เจฟ")
        nlp_ploc = nlp_ploc.replace(u"??", u"?")

        return nlp_ploc

    @staticmethod
    def transform_name_training(nlp_ploc):
        # edit name
        nlp_ploc = nlp_ploc.replace(u"แซ น ด ร้า", u"แซนดรา")
        nlp_ploc = nlp_ploc.replace(u"ดา เนีย ล", u"ดาเนียล ")
        nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ออฟ ฟิต", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ที่ทำงาน", u"ออฟฟิศ ")
        nlp_ploc = nlp_ploc.replace(u"ก ลับ", u"กลับ")

        nlp_ploc = nlp_ploc.replace(u" \tที่", u" \tไม่")
        nlp_ploc = nlp_ploc.replace(u" \tบางที", u" \tอาจจะ")

        # name
        nlp_ploc = nlp_ploc.replace(u"แซนดรา", u"มาค")
        nlp_ploc = nlp_ploc.replace(u"แมรี่", u"ติ๋ม")
        nlp_ploc = nlp_ploc.replace(u"จอห์น", u"เจ")
        nlp_ploc = nlp_ploc.replace(u"ดาเนียล", u"โจ")
        nlp_ploc = nlp_ploc.replace(u"จูลี่", u"โม")
        nlp_ploc = nlp_ploc.replace(u"บิล", u"โบว")
        nlp_ploc = nlp_ploc.replace(u"เฟร็ด", u"เฟิร์น")

        # place
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
        nlp_ploc = nlp_ploc.replace(u"โรงภาพยนตร์", u"โรงหนัง")

        return nlp_ploc