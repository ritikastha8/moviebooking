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






######################################
box=Frame(root,width=500,height=500,bg='grey')
box.place(x=480,y=250)

heading=Label(box,text='RESET PASSWORD',fg='blue',bg='grey',font=('Arial',39))
heading.place(x=2,y=10)


#####
def enter(e):
    enter1.delete(0,'end')
def leave(e):
    name=enter1.get()
    if name=='':
        enter1.insert(0,'ENTER YOUR USERNAME')
enter1=Entry(box,width=30,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
enter1.place(x=60,y=100)
enter1.insert(0,'ENTER YOUR USERNAME')
enter1.bind('<FocusIn>',enter)
enter1.bind('<FocusOut>',leave)
Frame(box,width=400,height=2,bg='black').place(x=60,y=142)



#####
question=Label(box,text="Q1. What is your favourite colour?",fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
question.place(x=30,y=180)
en=Entry(box,width=25,border=0,fg='white',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
en.place(x=30,y=225)
Frame(box,width=390,height=2,bg='black').place(x=30,y=260)






#######
def enter(e):
    newpassword.delete(0,'end')
def leave(e):
    name=newpassword.get()
    if name=='':
        newpassword.insert(0,'Password')

newpassword=Entry(box,width=20,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
newpassword.place(x=30,y=296)
newpassword.insert(0,'New Password')
newpassword.bind('<FocusIn>',enter)
newpassword.bind('<FocusOut>',leave)
Frame(box,width=318,height=2,bg='black').place(x=30,y=330)


# ####

def enter(e):
    confirmpassword.delete(0,'end')
def leave(e):
    name1=confirmpassword.get()
    if name1=='':
        confirmpassword.insert(0,'Confirm Password')

confirmpassword=Entry(box,width=20,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
confirmpassword.place(x=30,y=364)
confirmpassword.insert(0,'Confirm Password')
confirmpassword.bind('<FocusIn>',enter)
confirmpassword.bind('<FocusOut>',leave)
Frame(box,width=318,height=2,bg='black').place(x=30,y=400)

#####
check_button=Checkbutton(box,bg='grey')
check_button.place(x=360,y=308)
show=Label(box,text='Show',fg='black',bg='grey',font=('Arial',15))
show.place(x=385,y=308)

check_button=Checkbutton(box,bg='grey')
check_button.place(x=360,y=378)
show=Label(box,text='Show',fg='black',bg='grey',font=('Arial',15))
show.place(x=385,y=378)



####
def login1():
    root.destroy()
    import login1




Button(box,width=10,text='CONFIRM',bg='blue',fg='white',border=0,font=('Microsoft YaHei UI Light',18),command=login1).place(x=160,y=434)


#######################################




root.mainloop()






    

