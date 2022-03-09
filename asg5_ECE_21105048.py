from tkinter import *


#                                             Question 1
print("                                       Question 1\n")

root=Tk()
root.title("GST CALCULATOR")                                                           # Windows Title
root.minsize(width=600,height=300)                                                     # Windows Size

original_cost=Label(root,text="Enter original cost:")
original_cost.grid(row=0,column=0,pady=30)

entry_OC=Entry(root,textvariable=IntVar())                                             # Original Cost
entry_OC.grid(row=0,column=1,pady=30)

net_cost=Label(root,text="Enter Net cost:")
net_cost.grid(row=1,column=0,pady=30)

entry_NC=Entry(root,textvariable=IntVar())                                             # Net Price
entry_NC.grid(row=1,column=1,pady=30)

def gstrate():
    
    original_cost=int(entry_NC.get())
    net_cost=int(entry_OC.get())
    
    gstrate=(original_cost-net_cost)*100/original_cost                                 # Formula to calculate GST
    
    gst=Label(root,text="The gst rate is: "+str(gstrate)+"%")
    gst.grid(row=6,column=0,pady=20)

submit=Button(root,text="Submit",command=gstrate)                                      # Button to call funtion to calculate GST
submit.grid(row=4,pady=50)

root.mainloop()









import calendar
win=Tk()
win.title("calendar")
win.minsize(width=1600,height=800)
lbl=Label(win,text='Enter YEAR: ')
lbl.grid(row=0,column=0)

year=Entry(win,textvariable=IntVar())
year.grid(row=0,column=1)

def Calendar():
    Year=int(year.get())
    cal=calendar.calendar(Year,c=10)
    labl=Label(win,text=cal)
    labl.grid()
scrlbar=Scrollbar(win)
scrlbar.grid(columnspan=10)
go=Button(win,text="GO!",command=Calendar)
go.grid(row=2)

win.mainloop()
