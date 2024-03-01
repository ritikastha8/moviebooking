import sqlite3

def update_ticket_quantity(ticket_id, booked_quantity):
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Tickets SET ticket_quantity = ticket_quantity - ? WHERE ticket_id = ?', (booked_quantity, ticket_id))
    conn.commit()
    conn.close()




def create_table():
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
                   ticket_id TEXT PRIMARY KEY,
                   movie_name TEXT,
                   ticket_quantity INTEGER,
                   ticket_price INTEGER)''')
    conn.commit()
    conn.close()

def insert_Tickets():
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()
    Tickets_data=[
        ('T1','Article 370',30,250),
        ('T2','Teri Baaton Mein Aisa Uljha Jiya',20,360),
        ('T3','Dayarani',18,340),
        ('T4','Gurkha Warrior',8,240)
    ]


    cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id,movie_name,ticket_quantity,ticket_price)VALUES(?,?,?,?)',Tickets_data)

    conn.commit()
    conn.close()


def get_tickets():
    conn=sqlite3.connect('Reservation.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets=cursor.fetchall()
    conn.close()

    return tickets










