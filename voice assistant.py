############## import modules ###############
from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

############### audio engine ###############
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

############### search function ###############
def search():
    data=json.load(open('dictionary.json'))
    # print(data)
    word=wordEntry.get()
    word=word.lower()
    # print(word)
    if word in data:
        meaning=data[word]
        print(meaning)
        textArea.delete(1.0,END)
        for item in meaning:
            textArea.insert(END,u'\u2022'+item+'\n')

    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word, data.keys())[0]
        res=messagebox.askyesno('confirm',f'Did you mean {close_match} instead')
        if res==True:
            wordEntry.delete(0,END)
            wordEntry.insert(END,close_match)
            meaning=data[close_match]
            textArea.delete(1.0,END)
            for item in meaning:
                textArea.insert(END,u'\u2022'+item+'\n\n')

        else:
            messagebox.showerror('Error',"The word doesn't exit!! Please double check it!!")
            wordEntry.delete(0,END)
            textArea.delete(1.0,END)

    else:
        messagebox.showinfo('Information',"The word doesn't exist")
        wordEntry.delete(0,END)
        textArea.delete(1.0,END)

############### clear function ###############
def clear():
    wordEntry.delete(0,END)
    textArea.delete(1.0,END)

############### exit function ###############
def iexit():
    res=messagebox.askyesno('Confirm','Do you want to exit??')
    if res==True:
        root.destroy()
    else:
        pass
    

############### wordaudio function ###############
def wordaudio():
    engine.say(wordEntry.get())
    engine.runAndWait()

############### meaning function ###############
def meaningaudio():
    engine.say(textArea.get(1.0,END))
    engine.runAndWait()


#################### GUI phase ####################
root=Tk()
root.geometry('1000x626+100+30')
root.title('Talking Dictionary')
root.resizable(False,False)
root.config(bg='black')

entryHeadingLabel=Label(root,text='Enter Word',font=('arial',29,'bold'),bg='black',fg='lightpink')
entryHeadingLabel.place(x=360,y=20)

wordEntry= Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=8,relief=GROOVE)
wordEntry.place(x=290,y=80)

searchIcon=PhotoImage(file='loupe.png')
searchButton=Button(root,image=searchIcon,bd=0,bg='black',cursor='hand2',activebackground='black',command=search)
searchButton.place(x=380,y=150)

micIcon=PhotoImage(file='mic.png')
micButton=Button(root,image=micIcon,bd=0,bg='black',cursor='hand2',activebackground='black',command=wordaudio)
micButton.place(x=480,y=153)

entryHeadingLabel=Label(root,text='Meaning',font=('arial',29,'bold'),bg='black',fg='lightpink')
entryHeadingLabel.place(x=380,y=240)

textArea=Text(root,width=37,height=8,font=('arial',18),bd=8, relief=GROOVE)
textArea.place(x=220,y=300)

audioIcon=PhotoImage(file='sound.png')
audioButton=Button(root,image=audioIcon,bd=0,bg='black',cursor='hand2',activebackground='black',command=meaningaudio)
audioButton.place(x=320,y=555)

clearIcon=PhotoImage(file='cross.png')
clearButton=Button(root,image=clearIcon,bd=0,bg='black',cursor='hand2',activebackground='black',command=clear)
clearButton.place(x=430,y=555)

exitIcon=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitIcon,bd=0,bg='black',cursor='hand2',activebackground='black',command=iexit)
exitButton.place(x=540,y=555)

############### press enter ###############
def enter_function(event):
    searchButton.invoke()
root.bind('<Return>',enter_function)

root.mainloop()