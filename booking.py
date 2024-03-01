from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

root = Tk()
root.title('BOOKMYSEAT')
root.iconbitmap('cinema.ico')
root.geometry('1940x1090')
img1 = PhotoImage(file="C:/Users/N I T R O 5/OneDrive/Pictures/back3.png")
Label(root, image=img1).place(x=0, y=0)

Label(root, background='white').place(x=0, y=0)
name1 = Label(root, text='BookMySeat', fg='maroon', font=('Arial,bold', 50))
name1.place(x=0, y=10)
######################################

box = Frame(root, width=300, height=800, bg='grey')
box.place(x=0, y=100)
heading = Button(box, text='Movies ', fg='blue', bg='grey', font=('Arial', 45))
heading.place(x=20, y=50)
heading = Button(box, text='Booking', fg='blue', bg='grey', font=('Arial', 45))
heading.place(x=20, y=200)


def logout():
    root.destroy()
    import logout


heading = Button(box, text='Logout  ', fg='blue', bg='grey', font=('Arial', 45), command=logout)
heading.place(x=20, y=370)


font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 13, 'bold')
font3 = ('Arial', 18, 'bold')


def add_to_treeview():
    tree.delete(*tree.get_children())
    tickets = database.get_tickets()

    for ticket in tickets:
        if ticket[2] > 0:
            tree.insert('', END, values=ticket)


def reservation(name, movie, quantity, price):
    customer_name = name
    movie_name = movie
    booked_quantity = quantity
    ticket_price = price
    total_price = ticket_price * booked_quantity


def book():
    customer_name = name_entry.get()
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose a ticket to book')
    elif not customer_name:
        messagebox.showerror('Error', 'Enter customer name')
    else:
        row = tree.item(selected_item)['values']
        movie_name = row[1]
        ticket_price = row[3]
        booked_quantity = int(variable1.get())
        if booked_quantity > row[2]:
            messagebox.showerror('Error', 'Not enough tickets.')
        else:
            database.update_ticket_quantity(row[0], booked_quantity)
            add_to_treeview()
            total_price = reservation(customer_name, movie_name, booked_quantity, ticket_price)
            with open('Tickets.txt', 'a') as file:
                file.write(f'Customer Name:{customer_name}\n')
                file.write(f'Movie Name:{movie_name}\n')
                file.write(f'Total Price:{total_price}$\n========\n')
            messagebox.showinfo('Success', 'Tickets are booked!')


name11 = Label(root, font=font3, text='Customer Name:', fg='white', bg='black')
name11.place(x=522, y=500)

name_entry = Entry(root, width=20, border=0, fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
name_entry.place(x=740, y=500)

name21 = Label(root, font=font3, text='No. of Tickets :', fg='white', bg='black')
name21.place(x=522, y=550)

name22 = Label(root, font=font3, text='Time :', fg='white', bg='black')
name22.place(x=522, y=590)

ticket_options = [str(i) for i in range(1, 6)]
variable1 = tk.StringVar(value=ticket_options[0])
bu2 = OptionMenu(root, variable1, *ticket_options)
bu2.config(width=18, border=0, fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
bu2.place(x=740, y=550)


time_options = ['10 a.m.', '1 p.m.','4 p.m.', '7 p.m.']
variable2 = tk.StringVar(value=time_options[0])
bu3 = OptionMenu(root, variable2, *time_options)
bu3.config(width=18, border=0, fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
bu3.place(x=740, y=590)

book_button = Button(root, command=book, font=font3, fg='white', bg='black', text='Book Tickets')
book_button.place(x=710, y=650)

style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='white', background='black', fieldbackground='black')
style.map('Treeview', background=[('selected', 'pink')])

tree = ttk.Treeview(root, height=15)
tree['columns'] = ('Ticket ID', 'Movie Name', 'Available Tickets', 'Ticket Price')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Ticket ID', anchor=tk.CENTER, width=100)
tree.column('Movie Name', anchor=tk.CENTER, width=250)
tree.column('Available Tickets', anchor=tk.CENTER, width=100)
tree.column('Ticket Price', anchor=tk.CENTER, width=100)

tree.heading('#0', text='', anchor=tk.CENTER)
tree.heading('Ticket ID', text='Ticket ID', anchor=tk.CENTER)
tree.heading('Movie Name', text='Movie Name', anchor=tk.CENTER)
tree.heading('Available Tickets', text='Available Tickets', anchor=tk.CENTER)
tree.heading('Ticket Price', text='Ticket Price', anchor=tk.CENTER)

tree.place(x=500, y=125)

add_to_treeview()

root.mainloop()
