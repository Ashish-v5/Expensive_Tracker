from tkinter import *
from tkinter import ttk
import sqlite3
conn=sqlite3.connect("ExpenseTracker.db")

root = Tk()
root.title("Transaction Page")
root.geometry("600x600")

canvas = Canvas(root, borderwidth=0)
frame = Frame(canvas)
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas_frame = canvas.create_window((0,0), anchor="nw")
canvas.itemconfigure(canvas_frame, window = frame)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def FrameWidth(event):
    canvas_width = event.width
    canvas.itemconfig(canvas_frame, width = canvas_width)

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
canvas.bind('<Configure>', lambda event: FrameWidth(event))

rootWidth = root.winfo_screenwidth()
def populate(frame):
    frameTab = Frame(frame)
    frameTab.pack(side="top", fill = "both", expand = True)
    frameTab.grid_columnconfigure(0,weight=1)
    frameTab.grid_columnconfigure(1,weight=1)
    frameTab.grid_columnconfigure(2,weight=1)
    frameTab.grid_columnconfigure(3,weight=1)
    Button(frameTab, text = "Home", relief="solid", width= 10, bd = 1).grid(row = 0, column = 0)
    Button(frameTab, text = "Transaction", relief="solid", width= 13, bd = 1).grid(row = 0, column = 1)
    Button(frameTab, text = "Expense Summary", relief="solid", width= 20, bd = 1).grid(row = 0, column = 2)
    Button(frameTab, text = "Item Budget", relief="solid", width= 15, bd = 1).grid(row = 0, column = 3)
    Label(frame, text = "This Month's Expense", width= rootWidth, height = 3, anchor=CENTER, bg='deep sky blue',bd=4, pady=5).pack()
    expenseFrame = Frame(frame, padx = 10, pady=10)
    expenseFrame.pack(fill = BOTH, expand = True)
    expenseFrame.grid_columnconfigure(0, weight=1)
    expenseFrame.grid_columnconfigure(1, weight=1)
    Label(expenseFrame, text = 'Expense',bg='orange red', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid').grid(row=0, column = 0)
    Label(expenseFrame, text = 'Rs 4000',bg='orange red', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid').grid(row=0, column = 1)

    #database
    i=1
    cursor = conn.execute("SELECT * FROM Expense WHERE type='expense'")
    for r in cursor:
        Label(expenseFrame, text = "%s"%r[2],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='firebrick1').grid(row=i,column=0)
        Label(expenseFrame, text = "%s"%r[4],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='firebrick1').grid(row=i,column=1)
        i+=1
    
    
    Label(expenseFrame, text = 'Income', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='green2').grid(row=i, column = 0)
    Label(expenseFrame, text = 'Rs 14000', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='green2').grid(row=i, column = 1)
    i+=1

    cursor = conn.execute("SELECT * FROM Expense WHERE type='income'")

    for r in cursor:
        Label(expenseFrame, text = "%s"%r[2],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='SpringGreen2').grid(row=i,column=0)
        Label(expenseFrame, text = "%s"%r[4],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid',bg='SpringGreen2').grid(row=i,column=1)
        i+=1
    # for i in range(11, 151, 1):
    #     Label(expenseFrame, text = 'Salary',fg = 'Green',pady=3).grid(row = i, column = 0)
    #     Label(expenseFrame, text = 'Rs 400',fg = 'black',pady=3).grid(row = i, column = 1)
populate(frame)

root.mainloop()