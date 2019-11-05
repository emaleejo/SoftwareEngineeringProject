#!/usr/bin/env python3
from tkinter import *
# import tkinter
import webbrowser

tk = Tk()
tk.wm_attributes("-fullscreen", False)

ticket = []


def editMenus():
        tk2 = Tk()
        tk2.wm_attributes("-fullscreen", False)
        tk.withdraw()
        tk2.title("Edit Menu")
        Label1 = Label(tk2, text = "Choose menu to edit: ", font =('Arial',40), fg = 'black')
        Label1.pack(pady=50,padx=10)
        Button(tk2, text='Food Menu',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[foods.__call__(), tk2.withdraw()]).pack()
        Button(tk2, text='Drink Menu',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[drinks.__call__(),tk2.withdraw()]).pack()
        Button(tk2, text='Cancel',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tk2.withdraw(),tk.deiconify()]).pack()

def foods():
        tk3 = Tk()
        tk3.wm_attributes("-fullscreen", False)
        tk3.title("Food")
        Label(tk3, text = "Food Options:", font =('Arial',40), bg = 'white', fg = 'black').pack(pady=20)
        # pizzas
        Label(tk3, text = "Pizzas", font = ('Arial' ,26), bg='white', fg='black').pack(pady=10)
        pizzas = []
        p = ['Pepperoni', 'Bacon', 'Sausage', 'Spinach', 'Mushroom', 'Olives', 'Pineapple']
        
        for pick in p:
                x = IntVar(value=1)
                Checkbutton(tk3, text=pick, variable=x, font=('Arial', 26)).pack()
                Entry(tk3, bg='white').pack()
                pizzas.append(x)

        # pastas
        Label(tk3, text = "Pastas", font = ('Arial' ,26), bg='white', fg='black').pack(pady=10)
        pastas = []
        pasta = ['Pasta1']
        
        for pick in pasta:
                x = IntVar(value=1)
                Checkbutton(tk3, text=pick, variable=x, font=('Arial', 26)).pack()
                Entry(tk3, bg='white').pack()
                pastas.append(x)
        # Salads
        Label(tk3, text = "Salads", font = ('Arial' ,26), bg='white', fg='black').pack(pady=10)
        # salads = []
        # salads = ['Salad1']
        
        # for pick in salads:
        #         x = IntVar(value=1)
        #         Checkbutton(tk3, text=pick, variable=x, font=('Arial', 26)).pack()
        #         Entry(tk3, bg='white').pack()
        #         salads.append(x)

        Button(tk3, text='Back',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tk3.withdraw()]).pack(side=BOTTOM)
        tk3.mainloop()

def pizzas():
        tkP = Tk()
        tkP.wm_attributes("-fullscreen", False)
        vars = []
        # tk2.withdraw()
        Labelp = Label(tkP, text = "What would you like on your pizza?", font =('Arial',40), bg = 'white', fg = 'black')
        Labelp.pack(pady=100,padx=100)
        picks = ['Pepperoni', 'Bacon', 'Sausage', 'Spinach', 'Mushroom', 'Olives', 'Pineapple']
        for pick in picks:
                var = IntVar()
                chk = Checkbutton(tkP, text=pick, variable=var, font =('Arial' ,26)).pack()
                vars.append(var)

        # add = Button(tkP, text='Add to Order',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(), ticket.append("pizzas")]).pack()
        back4 = Button(tkP, text='Back',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw()]).pack()

def drinks():
        tkP = Tk()
        tkP.wm_attributes("-fullscreen", False)
        vars = []
        Labelp = Label(tkP, text = "What drinks would you like?", font =('Arial',40), bg = 'white', fg = 'black')
        Labelp.pack(pady=100,padx=100)
        picks = ['Dr. Pepper', 'Pepsi', 'Sausage', 'Mountain Dew', 'Strawberry Lemonade', 'Lemonade', 'Water']
        for pick in picks:
                var = IntVar()
                chk = Checkbutton(tkP, text=pick, variable=var, font =('Arial' ,26)).pack()
                vars.append(var)

        add = Button(tkP, text='Add to Order',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(), ticket.append("Pizza")]).pack()
        back4 = Button(tkP, text='Back',font =('Arial' ,26), width=20, height=3, fg='green', command=lambda:[tkP.withdraw(),tk.deiconify()]).pack()

def game():
        webbrowser.open_new("https://www.solitr.com")

def paycheck():
        tkpc = Tk()
        tkpc.wm_attributes("-fullscreen", False)
        Label(tkpc, text = "Your check:" ,font =('Arial',40), bg = 'white', fg = 'green').pack()
        Labelc = Label(tkpc, text = 
        "  Pizza                $8.00\n    Fetticine            $11.00\n  Cabernet(2)       $8.50\n\n\n  Tax:                  $2.27\n   Total:               $29.77", font =('Arial',40), bg = 'white', fg = 'black')
        Labelc.pack(pady=100,padx=100,)
        Label(tkpc, text = "Your server has been notified and a paper copy is on it's way." ,font =('Arial',40), bg = 'white', fg = 'green').pack()
        Button(tkpc, text="Exit", font=('Arial',26), command=lambda:[tkpc.withdraw(), tk.deiconify()]).pack()

def main(): 
        #tk = Tk() 
        tk.title('Customer Streamliner 9000 [ADMIN]') 
        # Taskbar / Menu 
        menu = Menu(tk)
        tk.config(menu=menu)
        # File > Exit
        file = Menu(menu) #File - Exit
        file.add_command(label="Exit", command=tk.destroy)

        #Logo added
        # frame = Frame(tk, width=800, height=600, background='white')
        # frame.pack_propagate(0)    
        # frame.pack()
        # # Logo that we created
        # img = PhotoImage(file='ivancicitalianv2.png')
        # pic = Label(frame, image=img)
        # pic.pack()

        #Buttons
        service = Button(tk, text='Edit Menu', width=20, height=3, font=('Arial',26), fg='green', command = editMenus)
        service.pack()
        order = Button(tk, text='View Tables' , width=20, height=3,font=('Arial' ,26),  fg='green', command = editMenus) 
        order.pack()
        check = Button(tk, text='Request Check', width=20, height=3, font=('Arial',26), fg='green', command = paycheck)
        check.pack()
        pay = Button(tk, text='Make Payment', width=20,height=3, font=('Arial',26), fg='green') 
        pay.pack()
        games = Button(tk, text='Games', width=20, height=3, font=('Arial' ,26), fg='green', command = game)
        games.pack()

        ("q", "quit")
        tk.mainloop()
        mainloop() 

if __name__ == '__main__':
        main()
