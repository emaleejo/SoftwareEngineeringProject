#Oren Cummings

from tkinter import *

root = Tk()
root.attributes("-fullscreen", True)
frmMain = Frame(root, bg="green")
frmTable = Frame(root)
frmSingle = Frame(root)
frmColors = Frame(root)

#Sets up weights on rows and columns for all frames
frmMain.grid(row=0, column=0, sticky="NESW")
frmMain.grid_rowconfigure(0, weight=1)
frmMain.grid_columnconfigure(0, weight=1)
frmMain.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frmTable.grid_rowconfigure(0, weight=2)
frmTable.grid_rowconfigure(1, weight=2)
frmTable.grid_rowconfigure(2, weight=1)
for i in range(4):
    frmTable.grid_columnconfigure(i, weight=1)

frmSingle.grid_rowconfigure(0, weight=1)
frmSingle.grid_rowconfigure(1, weight=2)
frmSingle.grid_rowconfigure(2, weight=2)
for i in range(3):
    frmSingle.grid_columnconfigure(i, weight=1)

frmColors.grid_rowconfigure(0, weight=1)
frmColors.grid_rowconfigure(1, weight=2)
frmColors.grid_rowconfigure(2, weight=2)
for i in range(3):
    frmColors.grid_columnconfigure(i, weight=1)

#Called when user clicks to see tables
def showTables():
    frmMain.grid_forget()
    frmTable.grid(row=0, column=0, sticky="NESW")

#Creates buttons for main form
newbut = Button(frmMain, text="Reservations", bg="red")
newbut.grid(row=0, sticky="NESW", padx=50, pady=50)

tablesBut = Button(frmMain, text="Tables", command=showTables, bg="red")
tablesBut.grid(row =0, column=1, sticky="NESW", padx=50, pady=50)

#Sets up different table buttons
button_list = []
for b in range(8):
    tblNum = b + 1
    button_list.append(Button(frmTable, text="Table "+str(tblNum), bg="green"))
    button_list[b].bind("<Button-1>", lambda event, arg=b: tableClicked(event, arg))
    if b < 4:
        button_list[b].grid(row = 0, column=b, sticky="NESW", padx=50, pady=50)
    else:
        button_list[b].grid(row = 1, column=b-4, sticky="NESW", padx=50, pady=50)
btnBack = Button(frmTable, text="Back", bg="grey")
btnBack.grid(row=2, columnspan=4, sticky="NESW", padx=50, pady=50)
btnBack.bind("<Button-1>", lambda event, cur=frmTable, pre=frmMain: back(event, cur, pre))


#Sets up some buttons on Table option screen
btnStatus = Button(frmSingle, text="Table Status", bg="pink")
btnStatus.grid(row=1, sticky="NESW", padx=50, pady=50)
btnTemp = Button(frmSingle, text="Enter Order", bg="pink")
btnTemp.grid(row=1, column=1, sticky="NESW", padx=50, pady=50)
btnTemp = Button(frmSingle, text="Check Options", bg="pink")
btnTemp.grid(row=1, column=2, sticky="NESW", padx=50, pady=50)
btnTemp = Button(frmSingle, text="POS", bg="pink")
btnTemp.grid(row=2, sticky="NESW", padx=50, pady=50)
btnTemp = Button(frmSingle, text="Print Check", bg="pink")
btnTemp.grid(row=2, column=1, sticky="NESW", padx=50, pady=50)
btnBack = Button(frmSingle, text="Back", bg="grey")
btnBack.grid(row=2, column=2, sticky="NESW", padx=50, pady=50)
btnBack.bind("<Button-1>", lambda event, cur=frmSingle, pre=frmTable: back(event, cur, pre))



#Sets up option buttons for tables
btnColor_list = []
btnColor_list.append(Button(frmColors, text="Available", bg="Green"))
btnColor_list.append(Button(frmColors, text="Seated", bg="yellow"))
btnColor_list.append(Button(frmColors, text="Waiting", bg="blue"))
btnColor_list.append(Button(frmColors, text="Ticket", bg="purple"))
btnColor_list.append(Button(frmColors, text="Dirty", bg="red"))
for i in range(5):
    if i < 3:
        btnColor_list[i].grid(row = 1, column=i, sticky="NESW", padx=50, pady=50)
    else:
        btnColor_list[i].grid(row=2, column=i - 3, sticky="NESW", padx=50, pady=50)
btnBack = Button(frmColors, text="Back", bg="grey")
btnBack.grid(row=2, column=2, sticky="NESW", padx=50, pady=50)
btnBack.bind("<Button-1>", lambda event, cur=frmColors, pre=frmSingle: back(event, cur, pre))



strLbl = StringVar()
lblTbl = Label(frmSingle, textvariable=strLbl)
lblTbl.grid(row=0, columnspan=4)
#When a certain table is clicked
def tableClicked(event, arg):
    frmTable.grid_forget()
    strLbl.set("Table "+ str(arg+1))
    frmSingle.grid(row=0, column=0, sticky="NESW")
    btnStatus.bind("<Button-1>", lambda event, tbl=arg: tableStatus(event, tbl))


lblTbl = Label(frmColors, textvariable=strLbl)
lblTbl.grid(row=0, columnspan=4)
#Shows the avalaible statuses to choose from
def tableStatus(event, tbl):
    frmSingle.grid_forget()
    frmColors.grid(row=0, column=0, sticky="NESW")
    for i in range(len(btnColor_list)):
        btnColor_list[i].bind("<Button-1>", lambda event, tbl=tbl, status=i: statusChanged(event, tbl, status))


#When a table status button is clicked
def statusChanged(event, tbl, status):
    color = "";
    if status == 0:
        color="green"
    elif status == 1:
        color="yellow"
    elif status == 2:
        color="blue"
    elif status == 3:
        color="purple"
    else:
        color="red"

    button_list[tbl].configure(bg=color)
    back(event, frmColors, frmSingle)

#When a back button is pressed
def back(event, cur, pre):
    cur.grid_forget()
    pre.grid(row=0, column=0, sticky="NESW")

root.mainloop()