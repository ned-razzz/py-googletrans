import tkinter
from client import Translator
from models import Translated
from spell_checker import check


translator = Translator()

window = tkinter.Tk()
window.title("번역&맞춤법검사기")
window.geometry("640x400+100+100")
window.resizable(False, False)

def Calculate(): # 번역
    result=(text1.get("1.0","end"))
    result1=translator.translate(result, dest='en')
    result2=result1.text
    message1.configure(text=result2)

    td = Translated(result1.src, result1.dest,result1.origin, result1.text, result1.pronunciation, result1.parts)
    voca=td.getVoca()
    message2.configure(text=voca)

def Calculate1(): # 맞춤법
    result=(text1.get("1.0","end"))
    result1=check(result)
    result2=result1.checked
    message1.configure(text=result2)

#버튼 프레임
labelframe1=tkinter.LabelFrame(window, text="기능 선택")
labelframe1.place(x=0,y=0, width=125 , height=75)

#번역버튼
button1 = tkinter.Button(labelframe1, overrelief="solid", width=15, text="번역&맞춤법", command = Calculate)
button1.pack(side="top")
button2 = tkinter.Button(labelframe1, overrelief="solid", width=15, text="맞춤법", command = Calculate1)
button2.pack(side="top")

#사전 프레임
labelframe2=tkinter.LabelFrame(window, bg="White", text="단어 사전")
labelframe2.place(x=135,y=0, width=500 , height=75)
#사전 창
message2 = tkinter.Message(labelframe2, bg="White", bd=2, width=290, anchor="nw")
message2.place(x=0,y=0, width=400, height=55)

#번역창과 결과창 프레임
mainframe=tkinter.LabelFrame(window, text="번역창")
mainframe.place(x=0,y=80, width=640 , height=320)

#결과창
message1 = tkinter.Message(mainframe, bg="White", bd=2, width=290, anchor="nw")
message1.place(x=310,y=0, width=300, height=290)

#입력창
text1=tkinter.Text(mainframe,  bd=2)
text1.place(x=0,y=0, width=300, height=290)


window.mainloop()   