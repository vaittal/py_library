from tkinter import *
class Button_two():
    def __init__(self):
        root2 = Tk()

        root2.title('ADD BOOKS WINDOW')
        root2.resizable(False,False)
        root2.geometry('650x650+600+200')

        #frames
        frame2 = Frame(root2, height=650, bg='#32a883')
        frame2.pack(fill=X)

        #labels
        l11 = Label(frame2, text='NAME OF BOOK:', font='arial 12 bold', bg='#32a883',
                   fg='black')
        l11.place(x=100, y=50)
        l22 = Label(frame2, text='AUTHOR NAME:', font='arial 12 bold', bg='#32a883',
                   fg='black')
        l22.place(x=100, y=100)
        l33= Label(frame2, text='YEAR OF PUBLISHING:', font='arial 12 bold', bg='#32a883',
                   fg='black')
        l33.place(x=100, y=150)



        #button

        b11 = Button(frame2, text='APPEND', font='arial 12 bold', bg='white',
                    fg='black')
        b11.place(x=150, y=450)

        b22 = Button(frame2, text='BACK',font='arial 12 bold', bg='white',fg='black'
                     ,command=root2.destroy)
        b22.place(x=400, y=450)

        #entry
        e11 = Entry(frame2)
        e11.place(x=400, y=50)
        e22 = Entry(frame2)
        e22.place(x=400, y=100)
        e33 = Entry(frame2)
        e33.place(x=400, y=150)

        root2.mainloop()

