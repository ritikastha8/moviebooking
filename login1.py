from tkinter import*
from tkinter import messagebox
 
root=Tk()
root.title('BOOKMYSEAT')
root.iconbitmap('cinema.ico')
root.geometry('1920x1080')
img1=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root,image=img1).place(x=0,y=0)




    
    
img2 = PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/ticketlogo.png")
Label(root,image=img2).place(x=620,y=10)
name1=Label(root,text='BookMySeat',fg='black',font=('Lucida Calligraphy',30))
name1.place(x=580,y=180)

box=Frame(root,width=500,height=500,bg='grey')
box.place(x=480,y=250)



heading=Label(box,text='SIGN IN',fg='blue',bg='grey',font=('Arial',39))
heading.place(x=170,y=30)

def enter(e):
    user.delete(0,'end')
def leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(box,width=30,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
user.place(x=30,y=140)
user.insert(0,'Username')
user.bind('<FocusIn>',enter)
user.bind('<FocusOut>',leave)
Frame(box,width=400,height=2,bg='black').place(x=30,y=182)


def enter(e):
    password.delete(0,'end')
def leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')
    


    
password=Entry(box,width=20,border=0,fg='black',bg='grey',font=('Microsoft YaHei UI Light',20,'bold'))
password.place(x=30,y=240)
password.insert(0,'Password')
password.bind('<FocusIn>',enter)
password.bind('<FocusOut>',leave)
Frame(box,width=318,height=2,bg='black').place(x=30,y=282)



check_button=Checkbutton(box,bg='grey')
check_button.place(x=360,y=255)



show=Label(box,text='Show',fg='black',bg='grey',font=('Arial',15))
show.place(x=385,y=250)


def Reset():
    root.destroy()
    import Reset



forgot=Button(box,width=16,text='Forgot Password?',fg='white',border=0,bg='grey',font=('Microsoft YaHei UI Light',14,'bold'),command=Reset)
forgot.place(x=260,y=290)
Frame(box,width=178,height=2,bg='white').place(x=270,y=318)



def movies():
    
     if not user.get() or not password.get():
           messagebox.showerror('Error', 'Please enter your username and password')
   
           
     elif user.get()=='Ritika' and password.get()=='1234':
             root.destroy()
             import movies
     elif user.get()=='Ritika' and password.get()=='program':
          root.destroy()
          import movies
   
     else:
        messagebox.showerror('Error', 'Invalid username or password!')



Button(box,width=28,text='Login',bg='blue',fg='white',border=0,font=('Microsoft YaHei UI Light',18),command=movies).place(x=40,y=350)

     


label=Label(box,text="Don't have an account?",fg='black',bg='grey',font=('Microsoft YaHei UI Light',13))
label.place(x=125,y=410)

def Register():
    root.destroy()
    import Register

register1=Button(box,width=6,text='Sign up',border=0,fg='blue',font=('Microsoft YaHei UI Light',13),bg='grey',command=Register)
register1.place(x=310,y=406)



#######################################


root.mainloop()





