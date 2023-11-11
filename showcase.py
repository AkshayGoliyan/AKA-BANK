from tkinter import*
from tkinter import messagebox, font
from PIL import ImageTk, Image 

account = "11223344"
pin = "1234"
baln= 120000

def login():
    global account, pin, baln
    def lgn2ops():
        if i1.get()==account and i2.get()==pin:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            gui.destroy()
            options()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
            
        
    gui=Tk()

    gui.geometry("1300x731+100+30")
    gui.resizable(width="False", height="False")
    gui.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BG1.png"))
    bk=Label(gui,image=bckgrnd)
    bk.place(x=0,y=0)

    l1=Label(gui, text="Enter Account Number*", font="BOLD",bg="#5b92c2")
    l1.place(x=500,y=235)
    i1=Entry(gui, font=("Trebuchet MS","40"), fg="DARKBLUE", bg="#8CC8FD")
    i1.place(x=500,y=260, width=400, height=55)

    l2=Label(gui, text="Enter PIN Number*",font="BOLD",bg="#5b92c2")
    l2.place(x=500,y=360)
    i2=Entry(gui, font=("Trebuchet MS","40"), fg="DARKBLUE", bg="#8CC8FD")
    i2.place(x=500,y=385, width=200, height=55)


    btnimg=ImageTk.PhotoImage(Image.open("D:\AKA BANK\login.png"))
    bt1=Button(gui, image=btnimg, command=lgn2ops)
        
    bt1.place(x=700,y=500)


    gui.mainloop()
        
        
def options():
    
    def ops2lgn():
        gui1.destroy()
        login()
        
        
    def ops2vbal():
        gui1.destroy()
        vbalance()
        
    def ops2dep():
        gui1.destroy()
        deposite()
        
    def ops2wdr():
        gui1.destroy()
        withdrawl()
        
    def ops2pin():
        gui1.destroy()
        pinge()
        
    def ops2fc():
        gui1.destroy()
        fcash()
        
    gui1=Tk()

    gui1.geometry("1300x730+100+30")
    gui1.resizable(width="False", height="False")
    gui1.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BG2.png"))
    bk=Label(gui1,image=bckgrnd)
    bk.place(x=0,y=0)

    btnimg2=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Balance_1_177x106.png"))
    bt16=Button(gui1, image=btnimg2, command=ops2vbal)
    bt16.place(x=500,y=225)

    btnimg3=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Deposit.png"))
    bt17=Button(gui1, image=btnimg3, command=ops2dep)
    bt17.place(x=980,y=225)

    btnimg4=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Withdrawal_177x106.png"))
    bt18=Button(gui1, image=btnimg4, command=ops2wdr)
    bt18.place(x=510,y=480)

    btnimg5=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Pin_177x106.png"))
    bt19=Button(gui1, image=btnimg5, command=ops2pin)
    bt19.place(x=744.5,y=350)

    btnimg6=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Fast_Cash_177x106.png"))
    bt20=Button(gui1, image=btnimg6, command=ops2fc)
    bt20.place(x=980,y=480)

    btnimg7=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt21=Button(gui1, image=btnimg7, command=ops2lgn)
    bt21.place(x=1153.5,y=666)
    gui1.mainloop()
    
def vbalance():
    global account, pin, baln
    def vbal2ops():
        gui.destroy()
        options()
    
    def vbal2login():
        gui.destroy()
        login()

    gui=Tk()

    gui.geometry("1300x730+100+30")
    gui.resizable(height="False", width="False")

    gui.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\\AKA BANK\\bal_1300x731.png"))
    bk=Label(gui,image=bckgrnd)
    bk.place(x=0,y=0)

    lb1=Label( gui, text="Your Account Balance is :" , bg="#5b92c2", font=('BOLD'))
    lb1.place(x=700, y=300)
    
    lb2=Text(gui,font=("Trebuchet MS","40"), fg="RED", bg="#5b92c2")
    lb2.place(x=650,y=350, height=80, width=300)
    lb2.insert(END, baln)


    btnimg8=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BACK.png"))
    bt22=Button(gui, image=btnimg8, command=vbal2ops)
    bt22.place(x=479,y=666)

    btnimg9=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt23=Button(gui, image=btnimg9, command=vbal2login)
    bt23.place(x=1153.5,y=666)
    
    gui.mainloop()

def deposite():
    # global account, pin, baln
    def dep2login():
        gui.destroy()
        login()
        
    def dep2ops():
        gui.destroy()
        options()
        
    def addbal():
        global baln
        baln = baln + int(i3.get())
        messagebox.showinfo(title="Transaction Sucessful", message="Money Deposited sucessfully, Thankyou")
        dep2ops()
    gui=Tk()

    gui.geometry("1300x730+100+30")
    gui.resizable(height="False", width="False")
    gui.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\\AKA BANK\\dep_1_1300x731.png"))
    bk=Label(gui,image=bckgrnd)
    bk.place(x=0,y=0)

    lb1=Label( gui, text="Enter the amount to be deposited:" , bg="#5b92c2", font=('BOLD'))
    lb1.place(x=675,y=300)

    i3=Entry(gui, font=("Trebuchet MS","40"), fg="RED", bg="#8CC8FD")
    i3.place(x=675, y=350, width=300, height=55)

    btnimg13=ImageTk.PhotoImage(Image.open("D:\AKA BANK\PROCEED.png"))
    bt34=Button(gui, image=btnimg13, command= addbal)
    bt34.place(x=700,y=525)
    
    btnimg3=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BACK.png"))
    bt21=Button(gui, image=btnimg3, command=dep2ops)
    bt21.place(x=479,y=666)

    btnimg7=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt21=Button(gui, image=btnimg7, command=dep2login)
    bt21.place(x=1153.5,y=666)

    gui.mainloop()
    
def withdrawl():
    # global account, pin, baln
    def wdr2login():
        gui.destroy()
        login()
        
    def wdr2ops():
        gui.destroy()
        options()
        
    def subbal():
        global baln
        if baln >= int(i2.get()):  
            baln = baln - int(i2.get())  
            messagebox.showinfo(title="Transaction Sucessful", message="Withdrawal Successful, Here's your Money!")
            wdr2ops()
        else:
            messagebox.showerror("Error", "Insufficient balance")

    gui=Tk()

    gui.geometry("1300x730+100+30")
    gui.resizable(height="False", width="False")

    gui.title("AKA Cooprative Bank")
    bckgrnd2=ImageTk.PhotoImage(Image.open("D:\\AKA BANK\\wd_1300x731.png"))
    bk=Label(gui,image=bckgrnd2)
    bk.place(x=0,y=0)

    lb4=Label( gui, text="Enter the amount to Withdraw :" , bg="#5b92c2", font=('BOLD'))
    lb4.place(x=675,y=280)

    lb5=Label( gui, text="Amount should be multiple of: 500, 2000" , bg="#5b92c2", font=('BOLD'))
    lb5.place(x=675,y=320)

    i2=Entry(gui, font=("Trebuchet MS","40"), fg="RED", bg="#8CC8FD")
    i2.place(x=675, y=350, width=300, height=55)

    btnimg13=ImageTk.PhotoImage(Image.open("D:\AKA BANK\PROCEED.png"))
    bt27=Button(gui, image=btnimg13 , command=subbal)
    bt27.place(x=700,y=525)


    btnimg14=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BACK.png"))
    bt28=Button(gui, image=btnimg14, command=wdr2ops)
    bt28.place(x=479,y=666)

    btnimg15=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt29=Button(gui, image=btnimg15, command=wdr2login)
    bt29.place(x=1153.5,y=666)
    gui.mainloop()

def pinge():
    # global account, pin, baln
    def pin2login():
        gui.destroy()
        login()
    
    def pin2ops():
        gui.destroy()
        options()
        
    def pinVal():
        global pin
        if i33.get() == pin:
            if i33.get() == i34.get():
                messagebox.showerror("Error", "New Pin is same as the last pin")
            else:
                if i34.get() == i35.get():
                    pin = i35.get()
                    messagebox.showinfo(title="Transaction Sucessful", message="Your pin is now changed")
                    pin2ops()
                else:
                    messagebox.showerror("Error", "Confirm Pin is not same as the pin")
                     
        else:
            messagebox.showerror("Error", "Current PIN do not match")
        
    gui=Tk()

    gui.geometry("1300x730+100+30")
    gui.resizable(height="False", width="False")

    gui.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\\AKA BANK\\gp_1300x731.png"))
    bk=Label(gui,image=bckgrnd)
    bk.place(x=0,y=0)

    l33=Label(gui, text="Input current PIN*", font="BOLD",bg="#5b92c2")
    l33.place(x=680,y=220)
    i33=Entry(gui, font=("Trebuchet MS","40"), fg="DARKBLUE", bg="#8CC8FD")
    i33.place(x=680,y=250, width=300, height=55)
    
    l34=Label(gui, text="Enter NEW PIN*", font="BOLD",bg="#5b92c2")
    l34.place(x=500,y=340)
    i34=Entry(gui, font=("Trebuchet MS","40"), fg="RED", bg="#8CC8FD")
    i34.place(x=500,y=370, width=300, height=55)
    
    l35=Label(gui, text="Confirm NEW PIN*", font="BOLD",bg="#5b92c2")
    l35.place(x=880,y=340)
    i35=Entry(gui, font=("Trebuchet MS","40"), fg="RED", bg="#8CC8FD")
    i35.place(x=880,y=370, width=300, height=55)

    btnimg13=ImageTk.PhotoImage(Image.open("D:\AKA BANK\PROCEED.png"))
    bt35=Button(gui, image=btnimg13 , command=pinVal)
    bt35.place(x=700,y=525)

    btnimg3=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BACK.png"))
    bt21=Button(gui, image=btnimg3, command=pin2ops)
    bt21.place(x=479,y=666)

    btnimg7=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt21=Button(gui, image=btnimg7, command=pin2login)
    bt21.place(x=1153.5,y=666)
    gui.mainloop()

def fcash():
    # global account, pin, baln
    def fc2ops():
        gui.destroy()
        options()
        
    def fc2lgn():
        gui.destroy()
        login()
    
    def qwid():
        global baln
        if baln >= int(lt.get(ACTIVE)): 
            baln = baln - int(lt.get(ACTIVE))  
            messagebox.showinfo(title="Transaction Sucessful", message="Fast Cash Withdrawal Successful!")
            fc2ops()
        else:
            messagebox.showerror("Error", "Insufficient balance")
    
    gui=Tk()

    gui.geometry("1300x730+100+30")
    gui.resizable(height="False", width="False")

    gui.title("AKA Cooprative Bank")
    bckgrnd=ImageTk.PhotoImage(Image.open("D:\\AKA BANK\\fc_1300x731.png"))
    bk=Label(gui,image=bckgrnd)
    bk.place(x=0,y=0)

    l33=Label(gui, text="SELECT THE AMOUNT YOU WANT TO FAST WITHDRAW:",font=("Trebuchet MS","20"),bg="#5b92c2", fg="RED")
    l33.place(x=500,y=210)
    lt=Listbox(gui,font=("Trebuchet MS","40"), fg="DARKBLUE", bg="#5b92c2",selectmode=SINGLE)
    lt.insert(1,500)
    lt.insert(2,1000)
    lt.insert(3,2000)
    lt.insert(4,3000)
    lt.insert(5,5000)
    lt.place(x=575,y=260, height=350, width=200)

    btnimg3=ImageTk.PhotoImage(Image.open("D:\AKA BANK\BACK.png"))
    bt21=Button(gui, image=btnimg3, command=fc2ops)
    bt21.place(x=479,y=666)

    btnimg7=ImageTk.PhotoImage(Image.open("D:\AKA BANK\Screenshot 2023-08-24 200627.png"))
    bt21=Button(gui, image=btnimg7, command=fc2lgn)
    bt21.place(x=1153.5,y=666)

    btnimg34=ImageTk.PhotoImage(Image.open("D:\AKA BANK\PROCEED.png"))
    bt34=Button(gui, image=btnimg34, command= qwid)
    bt34.place(x=850,y=400)

    gui.mainloop()

login()

