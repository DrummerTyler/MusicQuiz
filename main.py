#import modules
from tkinter import *
from PIL import Image, ImageTk

class MainClass(object):

    #variables
    logged_in = False


    #functions
    def play_click(self):

        if self.logged_in == False:
            self.login_click()
        elif self.logged_in == True:

            # window setup
            gw = Toplevel()
            gw.configure(background='#1F2833', height=700, width=1000)
            gw.resizable(0, 0)

    def login(self):

        supplied_username = self.username_txt.get()
        supplied_password = self.password_txt.get()

        with open('db.txt', 'r') as file:
            for line in file:
                username, password = line.split(',')
                # Check the username against the one supplied
                if username == supplied_username:
                    if password == supplied_password:
                        self.logged_in = True
                        self.play_click()
                    else:
                        tg = Toplevel()
                        tg.title('Try Again')
                        tg.configure(background='red')
                        tg.resizable(0, 0)

                        label = Label(tg, text='Password Does Not Match Username', bg='red', fg='black', font='non 25 bold')
                        label.pack()

                        login = Button(tg, text='Try Again', bg='grey', fg='black', font='non 25 bold', command=self.login_click())
                        login.pack()

                else:
                    tg = Toplevel()
                    tg.title('Try Again')
                    tg.configure(background='red')
                    tg.resizable(0, 0)

                    label = Label(tg, text='Username Does Not Exist', bg='red', fg='black', font='non 25 bold')
                    label.pack()

                    login = Button(tg, text='Try Again', bg='grey', fg='black', font='non 25 bold', command=self.login_click())
                    login.pack()


    def register(self):
        username = self.username_txt.get()
        password = self.password_txt.get()

        if username and password == '':
            tg = Toplevel()
            tg.title('Try Again')
            tg.configure(background='red')
            tg.resizable(0, 0)

            label = Label(tg, text='Please Complete All Fields', bg='red', fg='black', font='non 25 bold')
            label.pack()

            login = Button(tg, text='Try Again', bg='grey', fg='black', font='non 25 bold', command=self.register_click())
            login.pack()
        else:
            file = open('db.txt', 'a')
            file.write(username)
            file.write(',')
            file.write(password)
            file.write('\n')
            file.close()

            suc = Toplevel()
            suc.title('Account Created')
            suc.configure(background='green2')
            suc.resizable(0, 0)

            label = Label(suc, text='Account Created', bg='green2', fg='black', font='non 25 bold')
            label.pack()

            login = Button(suc, text='Login', bg='grey', fg='black', font='non 25 bold', command=self.login_click)
            login.pack()

    def register_click(self):
        # window setup
        lw = Toplevel()
        lw.title('TylerR - Music Quiz - Register')
        lw.configure(background='#1F2833', height=700, width=1000)
        lw.resizable(0, 0)

        # load the image
        load_register_title = Image.open('register_title.jpg')
        load_login_button = Image.open('login_button.jpg')
        load_register = Image.open('register.jpg')
        # render the image
        render_register_title = ImageTk.PhotoImage(load_register_title)
        render_login_button = ImageTk.PhotoImage(load_login_button)
        render_register = ImageTk.PhotoImage(load_register)

        # set labels
        register_title = Label(lw, image=render_register_title, bd=-2)
        register_title.image = render_register_title

        username = Label(lw, text='Username: ', bg='#1F2833', fg='white', font='none 25 bold')
        username.place(x=450, y=350)

        self.username_txt = Entry(lw, bg='#C5C6C7', width=25)
        self.username_txt.place(x=455, y=400)

        password = Label(lw, text='Password: ', bg='#1F2833', fg='white', font='none 25 bold')
        password.place(x=450, y=450)

        self.password_txt = Entry(lw, bg='#C5C6C7', width=25)
        self.password_txt.place(x=455, y=500)

        register_button = Button(lw, image=render_register, bg='#1F2833', borderwidth=10, command=self.register)
        register_button.image = render_register

        login_button = Button(lw, image=render_login_button, bg='#1F2833', borderwidth=10, command=self.login_click)
        login_button.image = render_login_button


        # place the images
        register_title.place(x=0, y=0)
        register_button.place(x=450, y=525)
        login_button.place(x=450, y=600)

    def login_click(self):
        # window setup
        lw = Toplevel()
        lw.title('TylerR - Music Quiz - Login')
        lw.configure(background='#1F2833', height=700, width=1000)
        lw.resizable(0, 0)

        # load the image
        load_login_title = Image.open('login_title.jpg')
        load_register = Image.open('register.jpg')
        load_login_button = Image.open('login_button.jpg')
        # render the image
        render_login_title = ImageTk.PhotoImage(load_login_title)
        render_register = ImageTk.PhotoImage(load_register)
        render_login_button = ImageTk.PhotoImage(load_login_button)

        # set labels
        login_title = Label(lw, image=render_login_title, bd=-2)
        login_title.image = render_login_title

        username = Label(lw, text='Username: ', bg='#1F2833', fg='white', font='none 25 bold')
        username.place(x=450, y=350)

        usernametxt = Entry(lw, bg='#C5C6C7', width=25)
        usernametxt.place(x=455, y=400)

        password = Label(lw, text='Password: ', bg='#1F2833', fg='white', font='none 25 bold')
        password.place(x=450, y=450)

        passwordtxt = Entry(lw, bg='#C5C6C7', width=25)
        passwordtxt.place(x=455, y=500)

        login_button = Button(lw, image=render_login_button, bg='#1F2833', borderwidth=10, command=self.login)
        login_button.image = render_login_button

        register_button = Button(lw, image=render_register, bg='#1F2833', borderwidth=10, command=self.register_click)
        register_button.image = render_register


        # place the images
        login_title.place(x=0, y=0)
        login_button.place(x=450, y=525)
        register_button.place(x=450, y=600)

    def mainwindow(self):
        #window setup
        window = Tk()
        window.title('TylerR - Music Quiz - Menu')
        window.configure(background='#1F2833', height=700, width=1000)
        window.resizable(0, 0)

        #load the image
        load_title = Image.open('music quiz.jpeg')
        load_play = Image.open('play.jpg')
        load_login = Image.open('login.jpg')
        #render the image
        render_title = ImageTk.PhotoImage(load_title)
        render_play = ImageTk.PhotoImage(load_play)
        render_login = ImageTk.PhotoImage(load_login)


        #set labels
        title = Label(window, image=render_title, bd=-2)
        title.image = render_title

        play_button = Button(window, image=render_play, bg='#1F2833', borderwidth=10, command=self.play_click)
        play_button.image = render_play

        login_button = Button(window, image=render_login, bg='#1F2833', borderwidth=10, command=self.login_click)
        login_button.image = render_login


        #place the images
        title.place(x=0, y=0)
        play_button.place(x=100, y=400)
        login_button.place(x=600, y=400)


        #run the window
        window.mainloop()

MainClass().mainwindow()