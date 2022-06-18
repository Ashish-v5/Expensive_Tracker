from tkinter import *
from tkinter import ttk
from tkcalendar import *
import sqlite3

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
    Label(frame, text = "Your Transactions", width= rootWidth, height = 3, anchor=CENTER, bg='pink',bd=4).pack()
    searchFrame = Frame(frame, padx = 10, pady=10)
    searchFrame.pack(fill=BOTH, expand = True)
    searchFrame.grid_columnconfigure(0, weight=1)
    searchFrame.grid_columnconfigure(1, weight=1)
    searchFrame.grid_columnconfigure(2, weight=1)
    searchFrame.grid_columnconfigure(3, weight=1)
    Label(searchFrame, text = "From").grid(row = 0, column = 1)
    startDate_E = DateEntry(searchFrame, width=20, bd=3,date_pattern='dd/mm/yyyy')
    startDate_E.grid(row=0, column=2)
    Label(searchFrame, text = "To").grid(row = 1, column = 1)
    endDate_E = DateEntry(searchFrame, width=20,bd=3,date_pattern='dd/mm/yyyy')
    endDate_E.grid(row=1, column=2)
    conn=sqlite3.connect("ExpenseTracker.db")
    
    def search():
        for widget in dataFrame.winfo_children():
            widget.destroy()
        a = startDate_E.get()
        b = endDate_E.get()
        # Label(dataFrame, )
        cursor = conn.execute("SELECT * FROM Expense where edate >= '%s' and edate <= '%s'"%(a,b))
        #cursor = conn.execute("SELECT * FROM Expense where edate='22/11/2019' or edate='20/11/2019' or edate='21/11/2019' or edate='01/11/2019'")
        i = 0
        for r in cursor:
            if r[3] == 'expense':
                Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=0)
                Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=1)
                Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red',relief='solid',pady=3).grid(row=i,column=2)
                i+=1
            else:
                Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=0)
                Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i,column=1)
                Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3).grid(row=i,column=2)
                i+=1
        #Label(dataFrame, text = "%s - (%s) :"%(a,b),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3).grid(row=i+1,column=0)
   
    Button(searchFrame, text="Search", width=10, command = search).grid(row = 2, column = 2)
    dataFrame = Frame(frame, padx = 10, pady=10)
    dataFrame.pack(fill = BOTH, expand = True)
    dataFrame.grid_columnconfigure(0, weight=1)
    dataFrame.grid_columnconfigure(1, weight=2)
    dataFrame.grid_columnconfigure(2, weight=2)
 
    #database 
    
    cursor=conn.execute("SELECT * FROM Expense WHERE edate='22/11/2019' and type='expense'")
    i = 0
    for r in cursor:
        Label(dataFrame, text="%s"%(r[5]), width=20,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=0)
        Label(dataFrame, text = "%s - (%s) :"%(r[1],r[2]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red',pady=3).grid(row=i,column=1)
        Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red',relief='solid',pady=3).grid(row=i,column=2)
        i+=1



    # for row in range(100):
    #     if row%2 == 0:
    #         Label(dataFrame, text="Tag %s expenses" % (row+1), width = 50, height = 3, borderwidth="1", relief="solid",bg='red').grid(row = row, column = 1)
    #         # t="this is the second column for row %s" %(row+1)
    #         # Label(dataFrame, text=t,height = 3,bg='red').grid(row=row, column=1)
    #     else:
    #         Label(dataFrame, text="Tag %s" % (row+1), width = 50, height = 3, borderwidth="1", relief="solid",bg='green').grid(row = row, column = 1)
    #         # t="this is the second column for row %s" %(row+1)
    #         # Label(dataFrame, text=t,height = 3,bg='green').grid(row=row, column=1)
populate(frame)

root.mainloop()