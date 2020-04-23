# import google_translate
#
# translator = google_translate.GoogleTranslator()
# print translator.translate("hello world", "thai")

from googletrans import Translator
translator = Translator()
out = translator.translate('hello world', dest='th')
print(u'%s'%out.text)
