
from tkinter import *
import webbrowser
tk = Tk()
tk.wm_attributes("-fullscreen", True)

ticket = []

def requests():
        tkr = Tk()
        tkr.wm_attributes("-fullscreen", True)
        Labelr = Label(tkr, text = "Your server has been notified and will be by shortly.", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        Labelr.pack(pady=400,padx=10)
        backr = Button(tk3, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tkr.withdraw(),tk.deiconify()]).pack()

def orders():
        tk2 = Tk()
        tk2.wm_attributes("-fullscreen", True)
        tk.withdraw()
        tk2.title("Order")
        Label1 = Label(tk2, text = "What menu would you like to order from?", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        Label1.pack(pady=200,padx=10)
        food = Button(tk2, text='Food',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[foods.__call__(), tk2.withdraw()]).pack()
        drink = Button(tk2, text='Drink',font =('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        back = Button(tk2, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tk2.withdraw(),tk.deiconify()]).pack()

def foods():
        tk3 = Tk()
        tk3.wm_attributes("-fullscreen", True)
        tk3.title("Food")
        Label1 = Label(tk3, text = "Select an option", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        pizza = Button(tk3, text = "Pizza", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[pizzas(), tk3.withdraw()]).pack()
        pasta = Button(tk3, text = "Pasta", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        salad = Button(tk3, text = "Salad", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        back2 = Button(tk3, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tk3.withdraw(),tk.deiconify()]).pack()

def pizzas():
        tkP = Tk()
        tkP.wm_attributes("-fullscreen", True)
        vars = []
        Labelp = Label(tkP, text = "What would you like on your pizza?", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        Labelp.pack(pady=100,padx=100)
        picks = ['Pepperoni', 'Bacon', 'Sausage', 'Spinach', 'Mushroom', 'Olives', 'Pineapple']
        for pick in picks:
                var = IntVar()
                chk = Checkbutton(tkP, text=pick, variable=var, font =('Caviar Dreams' ,26)).pack()
                vars.append(var)

        add = Button(tkP, text='Add to Order',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(), ticket.append("Pizza")]).pack()
        back4 = Button(tkP, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(),tk.deiconify()]).pack()

def game():
        webbrowser.open_new("https://www.solitr.com")

def paycheck():
        tkpc = Tk()
        tkpc.wm_attributes("-fullscreen", True)
        Labelc = Label(tkpc, text = "Pizza               $8.00\nFetticine               $11.00\nCabernet(2)             $8.50\nTax:           $2.27\nTotal:              $29.77", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        Labelc.pack(pady=100,padx=100, side=LEFT)

def main(): 
        #tk = Tk() 
        tk.title('Customer Streamliner 9000') 
        # Taskbar / Menu 
        menu = Menu(tk)
        tk.config(menu=menu)
        # File > Exit
        file = Menu(menu) #File - Exit
        file.add_command(label="Exit", command=tk.destroy)

        #Logo added
        frame = Frame(tk, width=800, height=600, background='white')
        frame.pack_propagate(0)    
        frame.pack()
        # Logo that we created
        img = PhotoImage(file='ivancicitalianv2.png')
        pic = Label(frame, image=img)
        pic.pack()

        #Buttons
        service = Button(tk, text='Request Service', width=20, height=3, font =('Caviar Dreams',26), fg='green', command = requests)
        service.pack(side=LEFT)
        order = Button(tk, text='Order',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command = orders) 
        order.pack(side = LEFT)
        check = Button(tk, text='Request Check', width=20, height=3, font =('Caviar Dreams',26), fg='green', command = paycheck)
        check.pack(side=RIGHT)
        pay = Button(tk, text='Make Payment', width=20,height=3, font =('Caviar Dreams',26), fg='green') 
        pay.pack(side=RIGHT)
        games = Button(tk, text='Games', width=20, height=3, font =('Caviar Dreams' ,26), fg='green', command = game)
        games.pack(side=LEFT)

        tk.mainloop()
        mainloop() 

if __name__ == '__main__':
        main()
