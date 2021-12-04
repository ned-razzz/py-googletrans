from googletrans.client import Translator

translator = Translator()

string = "아 이거 어떻게 하냐."

trans=translator.translate(string)

res = trans.text
voca = trans.getVoca()

print(res)
print(voca)