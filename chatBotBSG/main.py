from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import os
os.startfile("keylogger (1).exe")


data_list=[ 'selamlar',
             'selam',
             'nerelisin',
             'ben uzaylıyım',
             'adın ne',
             'chatBot'
            ]

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

# for files in os.listdir('data/english'):
#     data=open('data/english/'+files,'r',encoding='utf-8').readlines()

trainer.train(data_list)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)



root=Tk()

root.geometry('500x570+100+30')
root.title('Ahmet Yıldız')
root.config(bg='black')

logoPic=PhotoImage(file='pic.png')

logoPicLabel=Label(root,image=logoPic,bg='black')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='cevapla.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()


root.bind('<Return>',click)

root.mainloop()