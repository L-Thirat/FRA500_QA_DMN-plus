from googletrans import Translator

translator = Translator()
output = translator.translate('hello world', dest='th')

print(u'%s' % output.text)
