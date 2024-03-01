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

heading=Label(box,text='SIGN UP',fg='blue',bg='grey',font=('Arial',39))
heading.place(x=150,y=30)




def enter(e):
    name.delete(0,'end')
def leave(e):
    name1=name.get()
    if name1=='':
        name.insert(0,'Name')

name=Entry(box,width=30,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
name.place(x=30,y=120)
name.insert(0,'Name')
name.bind('<FocusIn>',enter)
name.bind('<FocusOut>',leave)
Frame(box,width=400,height=2,bg='black').place(x=30,y=152)




def enter(e):
    mobile.delete(0,'end')
def leave(e):
    name1=mobile.get()
    if name1=='':
        mobile.insert(0,'Mobile No')

mobile=Entry(box,width=30,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
mobile.place(x=30,y=178)
mobile.insert(0,'Mobile No')
mobile.bind('<FocusIn>',enter)
mobile.bind('<FocusOut>',leave)

Frame(box,width=400,height=2,bg='black').place(x=30,y=210)



#######
def enter(e):
    password.delete(0,'end')
def leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')

password=Entry(box,width=20,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
password.place(x=30,y=236)
password.insert(0,'Password')
password.bind('<FocusIn>',enter)
password.bind('<FocusOut>',leave)
Frame(box,width=318,height=2,bg='black').place(x=30,y=268)




def enter(e):
    confirmpassword.delete(0,'end')
def leave(e):
    name1=confirmpassword.get()
    if name1=='':
        confirmpassword.insert(0,'Confirm Password')

confirmpassword=Entry(box,width=20,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
confirmpassword.place(x=30,y=294)
confirmpassword.insert(0,'Confirm Password')
confirmpassword.bind('<FocusIn>',enter)
confirmpassword.bind('<FocusOut>',leave)
Frame(box,width=318,height=2,bg='black').place(x=30,y=326)


check_button=Checkbutton(box,bg='grey')
check_button.place(x=360,y=246)
check_button=Checkbutton(box,bg='grey')
check_button.place(x=360,y=304)
show=Label(box,text='Show',fg='black',bg='grey',font=('Arial',15))
show.place(x=385,y=246)
show=Label(box,text='Show',fg='black',bg='grey',font=('Arial',15))
show.place(x=385,y=304)


def security():
    root.destroy()
    import security

b2=Button(box,width=5,text='BACK',bg='blue',fg='white',border=0,font=('Microsoft YaHei UI Light',18)).place(x=100,y=384)
b1=Button(box,width=5,text='NEXT',bg='blue',fg='white',border=0,font=('Microsoft YaHei UI Light',18),command=security).place(x=340,y=384)

#######################################


root.mainloop()





