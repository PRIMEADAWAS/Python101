from googletrans import Translator
translator = Translator()
# out = translator.translate('안녕하세요.', dest='en')
out = translator.translate('안녕하세요.', dest='en')
# out = translator.detect('안녕하세요.')
print(out)
print(out.text)
