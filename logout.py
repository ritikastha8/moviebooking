from tkinter import*
 
root=Tk()
root.title('BOOKMYSEAT')
root.iconbitmap('cinema.ico')
root.geometry('1920x1080')
img1=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root,image=img1).place(x=0,y=0)
# img1=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root,background='white').place(x=0,y=0)
name1=Label(root,text='BookMySeat',fg='maroon',font=('Arial,bold',50))
name1.place(x=0,y=10)
######################################
box=Frame(root,width=300,height=800,bg='grey')
box.place(x=0,y=100)
heading=Button(box,text='Movies ',fg='blue',bg='grey',font=('Arial',45))
heading.place(x=20,y=50)
heading=Button(box,text='Booking',fg='blue',bg='grey',font=('Arial',45))
heading.place(x=20,y=200)
heading=Button(box,text='Logout  ',fg='blue',bg='grey',font=('Arial',45))
heading.place(x=20,y=370)

box1=Frame(root,width=700,height=300,bg='white')
box1.place(x=450,y=150)

def login1():
    root.destroy()
    import login1
ok=Label(box1,text=' Do you want to logout?  ',fg='black',bg='white',font=('Arial',45))
ok.place(x=30,y=10)
ok1=Button(box1,text='Yes',fg='white',bg='blue',font=('Arial',40),command=login1)
ok1.place(x=90,y=100)


ok2=Button(box1,text='No',fg='white',bg='blue',font=('Arial',40))
ok2.place(x=370,y=100)

root.mainloop()