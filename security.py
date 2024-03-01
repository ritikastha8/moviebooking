from tkinter import*
 
root=Tk()
root.title('BOOKMYSEAT')
root.iconbitmap('cinema.ico')
root.geometry('1990x1370')
img1=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root,image=img1).place(x=0,y=0)


img2 = PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/ticketlogo.png")
Label(root,image=img2).place(x=620,y=10)
name1=Label(root,text='BookMySeat',fg='black',font=('Lucida Calligraphy',30))
name1.place(x=580,y=180)
# root.resizable(False,False)

box=Frame(root,width=500,height=500,bg='grey')
box.place(x=480,y=250)



heading=Label(box,text='SIGN UP',fg='blue',bg='grey',font=('Arial',39))
heading.place(x=140,y=20)

heading=Label(box,text='Security Questions',fg='black',bg='grey',font=('Arial',29))
heading.place(x=90,y=90)
Frame(box,width=335,height=3,bg='black').place(x=90,y=140)



####
question=Label(box,text="Q1. What is your favourite colour?",fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
question.place(x=30,y=180)

en=Entry(box,width=25,border=0,fg='white',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
en.place(x=70,y=225)
Frame(box,width=390,height=5,bg='black').place(x=70,y=260)





Question2=Label(box,text='Q2. What is your favourite food?',fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
Question2.place(x=30,y=300)

en2=Entry(box,width=25,border=0,fg='white',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
en2.place(x=70,y=345)
Frame(box,width=390,height=5,bg='black').place(x=70,y=380)


def login1():
    root.destroy()
    import login1


signup=Button(box,width=10,text='SIGN UP',bg='blue',fg='white',border=0,font=('Microsoft YaHei UI Light',18),command=login1)
signup.place(x=300,y=420)




#######################################


root.mainloop()

