
from tkinter import *
tk = Tk()

def orders():
        tk2 = Tk()
        tk.withdraw()
        tk2.title("Order")
        Label1 = Label(tk2, text = "What menu would you like to order from?", font =('Arial Black',40), bg = 'white', fg = 'black')
        Label1.pack(pady=10,padx=10)
        food = Button(tk2, text='Food',font =('Arial',26), width=20, fg='green').pack()
        drink = Button(tk2, text='Drink',font =('Arial',26), width=20, fg='green') #Take screenshots button
        drink.pack()
        back = Button(tk2, text='Back',font =('Arial',26), width=20, fg='green', command = backbutton) #Take screenshots button
        back.pack()

def backbutton():
        tk2.withdraw()
        tk.show()

def main(): 
        #tk = Tk() 
        tk.title('Customer Streamliner 9000') 
        # Taskbar / Menu 
        menu = Menu(tk)
        tk.config(menu=menu)
        # File > Exit
        file = Menu(menu) #File - Exit
        file.add_command(label="Exit", command=tk.destroy)

        #Label Logo
        Label1 = Label(tk, text = "Ivancic's Italian", font =('Arial Black',40), bg = 'white', fg = 'black')
        Label1.pack(pady=10,padx=10)

        #Logo added
        frame = Frame(tk, width=600, height=200, background='white')
        frame.pack_propagate(0)    
        frame.pack()
        # Logo that we created
        #img = PhotoImage(file='sfacast.png')
        #pic = Label(frame, image=img)
        #pic.pack()

        #Buttons
        service = Button(tk, text='Request Service', width=20, font =('Arial',26), fg='green')
        service.pack()
        order = Button(tk, text='Order',font =('Arial',26), width=20, fg='green', command = orders) 
        order.pack()
        check = Button(tk, text='Request Check', width=20, font =('Arial',26), fg='green')
        check.pack()
        pay = Button(tk, text='Make Payment', width=20, font =('Arial',26), fg='green') 
        pay.pack()
        games = Button(tk, text='Games', width=20, font =('Arial',26), fg='green')
        games.pack()

        tk.mainloop()
        mainloop() 

if __name__ == '__main__':
        main()
