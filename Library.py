from tkinter import *
from button_one import Button_one
from button_two import Button_two
class Application(object):
    def __init__(self,master):
        self.master = master

        #frames
        self.top = Frame(master,height=250,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master,height=300,bg='#32a6a8')
        self.bottom.pack(fill=X)

        #top frame
        self.top_image = PhotoImage(file='icons/books.png')
        self.top_image_label = Label(self.top,image= self.top_image,bg = 'white')
        self.top_image_label.place(x=60,y=20)

        #bottom frame

        self.label_one = Label(self.bottom,text='WELCOME TO SUMPY LIBRARY',font='arial 15 bold'
                                 ,bg='#32a6a8',fg='black')
        self.label_one.place(x=200,y=10)

        #button_one to search book
        self.button_one =Button(self.bottom,text='SEARCH BOOK',font='arial 15 bold',fg='black'
                                ,bg='#32a84e',command=self.Btn_one)
        self.button_one.place(x=250,y=80)

        #button_two to add book
        self.button_two = Button(self.bottom, text='ADD BOOK', font='arial 15 bold', fg='black'
                                 , bg='#32a84e',command=self.btn_two)
        self.button_two.place(x=268, y=180)

    def Btn_one(self):
        search = Button_one()

    def btn_two(self):
        add = Button_two()






def main():
    root = Tk()
    app = Application(root)
    root.title("Sumpy Library")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()


if __name__ == '__main__':
    main()


