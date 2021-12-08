from googletrans.client import Translator

translator = Translator()

string = "너는 괴물이야!"

trans=translator.translate(string, dest='en')

res = trans.text
voca = trans.getVoca()

print(res)
print(voca)