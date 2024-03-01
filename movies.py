from tkinter import*
 
root=Tk()
root.title('BOOKMYSEAT')
root.iconbitmap('cinema.ico')
root.geometry('1990x1370')
img1=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root,image=img1).place(x=0,y=0)


img2=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/article37.png")
Label(root,image=img2).place(x=350,y=280)

img3=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/terii1.png")
Label(root,image=img3).place(x=650,y=280)

img4=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/dayarani1.png")
Label(root,image=img4).place(x=950,y=280)

img5=PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/gurkawarrior1.png")
Label(root,image=img5).place(x=1250,y=280)


nam=Label(root,text='Article 370',fg='black',font=('Arial,bold',20))
nam.place(x=420,y=600)
am=Label(root,text='ACTION,DRAMA,THRILLER',fg='grey',font=('Arial,bold',10))
am.place(x=380,y=680)


nam2=Label(root,text='Teri Baaton Mein Aisa',fg='black',font=('Arial,bold',20))
nam2.place(x=640,y=600)
nam3=Label(root,text=' Uljha Jiya',fg='black',font=('Arial,bold',20))
nam3.place(x=690,y=630)
am3=Label(root,text='DRAMA,ROMANCE',fg='grey',font=('Arial,bold',10))
am3.place(x=690,y=680)

nam4=Label(root,text='Dayarani',fg='black',font=('Arial,bold',20))
nam4.place(x=1020,y=600)
am4=Label(root,text='ROMANCE,LOVE',fg='grey',font=('Arial,bold',10))
am4.place(x=1020,y=680)


nam5=Label(root,text='Gurkha Warrior',fg='black',font=('Arial,bold',20))
nam5.place(x=1300,y=600)
am5=Label(root,text='WAR',fg='grey',font=('Arial,bold',10))
am5.place(x=1380,y=680)




Label(root,background='white').place(x=0,y=0)
name1=Label(root,text='BookMySeat',fg='maroon',font=('Arial,bold',50))
name1.place(x=0,y=10)
######################################
box=Frame(root,width=300,height=800,bg='grey')
box.place(x=0,y=100)
heading=Button(box,text='Movies ',fg='blue',bg='grey',font=('Arial',45))
heading.place(x=20,y=50)


def booking():
    root.destroy()
    import booking
heading=Button(box,text='Booking',fg='blue',bg='grey',font=('Arial',45),command=booking)
heading.place(x=20,y=200)

#########
def login1():
    root.destroy()
    import login1
heading2=Button(box,text='log',fg='blue',bg='grey',font=('Arial',20),command=login1)
heading2.place(x=20,y=650)
###########

def logout():
    root.destroy()
    import logout
heading=Button(box,text='Logout  ',fg='blue',bg='grey',font=('Arial',45),command=logout)
heading.place(x=20,y=370)
l1=Label(root,text='Now Showing',fg='black',background='white',font=('Arial',50))
l1.place(x=520,y=100)

# img = PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/tt.png")
# Label(root,image=img).place(x=20,y=100)

root.mainloop()

