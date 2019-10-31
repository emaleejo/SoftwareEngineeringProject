
from tkinter import *
tk = Tk()

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

def orders():
        tk2 = Tk()
        tk.withdraw()
        tk2.title("Order")
        Label1 = Label(tk2, text = "What menu would you like to order from?", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        Label1.pack(pady=10,padx=10)
        food = Button(tk2, text='Food',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[foods.__call__(), tk2.withdraw()]).pack()
        drink = Button(tk2, text='Drink',font =('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        back = Button(tk2, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tk2.withdraw(),tk.deiconify()]).pack()

def foods():
        tk3 = Tk()
        tk3.title("Food")
        Label1 = Label(tk3, text = "Select an option", font =('Caviar Dreams',40), bg = 'white', fg = 'black')
        pizza = Button(tk3, text = "Pizza", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[pizzas.__call__(), tk3.withdraw()]).pack()
        pasta = Button(tk3, text = "Pasta", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        salad = Button(tk3, text = "Salad", font = ('Caviar Dreams' ,26), width=20, height=3, fg='green').pack()
        back2 = Button(tk3, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tk3.withdraw(),tk2.deiconify()]).pack()

def pizzas():
        tkP = Tk()
        opt = Checkbar(tkP, ['Pepperoni', 'Bacon', 'Sausage', 'Spinach', 'Mushroom', 'Olives'])
        opt.pack(side=TOP,  fill=X)
        back2 = Button(tkP, text='Back',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(),tk3.deiconify()]).pack()

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
        service = Button(tk, text='Request Service', width=20, height=3, font =('Caviar Dreams',26), fg='green')
        service.pack(side=LEFT)
        order = Button(tk, text='Order',font =('Caviar Dreams' ,26), width=20, height=3, fg='green', command = orders) 
        order.pack(side = LEFT)
        check = Button(tk, text='Request Check', width=20, height=3, font =('Caviar Dreams',26), fg='green')
        check.pack(side=RIGHT)
        pay = Button(tk, text='Make Payment', width=20,height=3, font =('Caviar Dreams',26), fg='green') 
        pay.pack(side=RIGHT)
        games = Button(tk, text='Games', width=20, height=3, font =('Caviar Dreams' ,26), fg='green')
        games.pack(side=LEFT)

        tk.mainloop()
        mainloop() 

if __name__ == '__main__':
        main()
