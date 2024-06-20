from tkinter import *

exp = ""

def input(num):
    global exp
    exp = exp + str(num)
    eq.set(exp)

def Result():
    try: 
        global exp
        total = str(eval(exp))
        
        eq.set(total)
        exp = ""
    except:
        eq.set("error")
        exp = ""

def clear_input():
    global exp
    exp = ""
    eq.set("")    

def delete():
    global exp
    exp = exp[:-1]
    eq.set(exp)

if __name__ == "__main__":
    win = Tk()
    win.config(bg="black")
    win.title("Pandey's Calculator")
    win.option_add('*font','lucida 15 bold')
    win.geometry("432x482")
    eq = StringVar()

display = Entry(win, relief=RIDGE, textvariable=eq, justify='right',bd=40)

display.grid(columnspan=10, ipadx=45)

butn1 = Button(win, text = '1', fg = 'brown', 
                 command=lambda: input(1)  ,bd=5, height=3, width=6)
butn1.grid(row=1 ,column =0)

butn2 = Button(win, text = '2', fg = 'brown', 
                 command=lambda: input(2)  ,bd=5, height=3, width=6)
butn2.grid(row=1 ,column =1)

butn3 = Button(win, text = '3', fg = 'brown', 
                 command=lambda: input(3)  ,bd=5, height=3, width=6)
butn3.grid(row=1 ,column =2)

delete = Button(win, text = 'x', fg = 'brown', 
                 command= delete, bd=5, height=3, width=6)   
delete.grid(row=1 ,column =3)

butn4 = Button(win, text = '4', fg = 'brown',
                 command=lambda: input(4)  ,bd=5, height=3, width=6)
butn4.grid(row=2 ,column =0)

butn5 = Button(win, text = '5', fg = 'brown', 
                 command=lambda: input(5)  ,bd=5, height=3, width=6)
butn5.grid(row=2 ,column =1)

butn6 = Button(win, text = '6', fg = 'brown',
                 command=lambda: input(6)  ,bd=5, height=3, width=6)
butn6.grid(row=2 ,column =2)

minus = Button(win, text = '-', fg = 'brown', 
                 command=lambda: input("-")  ,bd=5, height=3, width=6)
minus.grid(row=2 ,column =3)

butn7 = Button(win, text = '7', fg = 'brown',
                 command=lambda: input(7)  ,bd=5, height=3, width=6)
butn7.grid(row=3 ,column =0)

butn8 = Button(win, text = '8', fg = 'brown', 
                 command=lambda: input(8)  ,bd=5, height=3, width=6)
butn8.grid(row=3 ,column =1)

butn9 = Button(win, text = '9', fg = 'brown',
                 command=lambda: input(9)  ,bd=5, height=3, width=6)
butn9.grid(row=3 ,column =2)

plus = Button(win, text = '+', fg = 'brown', 
                command=lambda: input("+")  ,bd=5, height=3, width=6)
plus.grid(row=3 ,column =3)    

butn0 = Button(win, text = '0', fg = 'brown',
                   command=lambda:input(0)  ,bd=5, height=3, width=6) 
butn0.grid(row=4 ,column =0)

butn00 = Button(win, text = '00', fg = 'brown', 
                 command=lambda :input("00")  ,bd=5, height=3, width=6) 
butn00.grid(row=4 ,column =1)

butn000 = Button(win, text = '000', fg = 'brown', 
                 command= lambda :input("000")  ,bd=5, height=3, width=6) 
butn000.grid(row=4 ,column =2)

multilpy = Button(win, text = '*', fg = 'brown', 
                   command=lambda: input("*")  ,bd=5, height=3, width=6)
multilpy.grid(row=4 ,column =3) 

clear = Button(win, text = 'C', fg = 'brown', 
                 command= clear_input, bd=5, height=3, width=6)   
clear.grid(row=5 ,column =0)

point = Button(win, text = '.', fg = 'brown', 
                 command= lambda:  input(".") ,bd=5, height=3, width=6)
point.grid(row=5 ,column =1)

divide = Button(win, text = '/', fg = 'brown',
                 command=lambda: input("/")  ,bd=5, height=3, width=6)
divide.grid(row=5 ,column =2) 

equal = Button(win, text = '=', fg = 'brown', 
                 command= Result, bd=5, height=3, width=6)
equal.grid(row=5 ,column =3)






win.mainloop()





