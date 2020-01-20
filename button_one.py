from tkinter import *

class Button_one():
    def __init__(self):
        root1 =Tk()
        root1.geometry('650x650+600+200')
        root1.resizable(False,False)
        root1.title('SEARCH WINDOW')

        #frames
        frame1 = Frame(root1, height = 650, bg = '#a83238')
        frame1.pack(fill=X)

        #lables
        l1 =Label(frame1,text='NAME OF BOOK:',font='arial 15 bold',bg='#a83238',
                  fg='black')
        l1.place(x=100,y=50)
        l2 =Label(frame1,text='AUTHOR NAME:',font='arial 15 bold',bg='#a83238',
                  fg='black')
        l2.place(x=100,y=150)
        l3 =Label(frame1,text='YEAR OF PUBLISHING:',font='arial 15 bold',bg='#a83238',
                  fg='black')
        l3.place(x=100,y=250)

        #entries
        e1 = Entry(frame1)
        e1.place(x=400,y=50)
        e2 = Entry(frame1)
        e2.place(x=400,y=150)
        e3 = Entry(frame1)
        e3.place(x=400,y=250)

        #button
        b1 =Button(frame1,text='SUBMIT',font='arial 15 bold',bg='white',
                  fg='black')
        b1.place(x=150,y=400)
        b22 = Button(frame1, text='BACK', font='arial 15 bold', bg='white', fg='black'
                     ,command=root1.destroy)
        b22.place(x=400, y=400)

        root1.mainloop()




