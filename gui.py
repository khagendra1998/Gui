from tkinter import  *
from tkinter import ttk

class GUI :
    def __init__(self):
        self.root = Tk()
        self.root.title("Common Banking")
        h = self.root.winfo_screenwidth()
        w = self.root.winfo_screenheight()
        self.root.geometry("{0}x{1}+0+0".format(h,w))
        self.root.configure(background='#CC0001')
        self.title()
        self.nav_bar()
        #self.create_account()
        self.root.mainloop()


    def title(self):
        L = Label(self.root, text='Head Post Office Staff Savings & Co-operative Society Ltd. Alwar ',
              font=('Times new Roman', 30, 'bold'), bg='#CC0001', fg='yellow',justify="right")
        L.grid(row=0,column=0,padx=300,pady=20)

    def password(self):
        pass

    def nav_bar(self):
        acc = self.create_account()
        menubar = Menu(self.root,bg='white')

        create_ac = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Create Account",menu=create_ac,command=acc)

        account_detail = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Account Detail",menu=account_detail)

        account_balance = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Account Balance",menu=account_balance)

        loan = Menu(menubar,tearoff=0)
        loan.add_command(label="Loan Issue")
        loan.add_command(label="Loan Deposit")
        loan.add_command(label="Loan Extend")
        menubar.add_cascade(label="Loan",menu=loan)

        report = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Report", menu=report)

        service = Menu(menubar, tearoff=0)
        service.add_command(label="Deposit")
        service.add_command(label="Deposit Interest")
        service.add_command(label="Update User Profile")
        service.add_command(label="Account Summary")
        menubar.add_cascade(label="Service", menu=service)

        close_acc = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Close Account", menu=close_acc)

        calculator = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="EMI Calculator", menu=calculator)

        # display the menu
        self.root.config(menu=menubar)

    def create_account(self):
        frame1 = Frame(self.root, bg='#CC0001')
        frame1.grid(row=1, column=0)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        labelfont = ('times', 20, 'bold')
        Label(frame1, text='Loan Account Number',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=0)

        Label(frame1, text='Name of Employee',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=1)
        Label(frame1, text='Account Office',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=2)
        Label(frame1, text='Designation of Employee',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=3)
        Label(frame1, text='Contact Number',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=4)
        Label(frame1, text='Email ID',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=5)
        Label(frame1, text='Address',
              font=labelfont,
              bg='#CC0001',
              justify =LEFT,
              anchor=W).grid(row=6)

        Loan_Acc_No_Var = IntVar()
        Emp_Name_Var = StringVar()
        Acc_Office_Var = StringVar()
        Designation_Var = StringVar()
        Contact_Var = IntVar()
        Email_Var = StringVar()
        Address_Var = StringVar()

        # Label(root, text=,font=labelfont,bg='#CC0001').grid(row=0)
        e1 = Entry(frame1, textvariable=Loan_Acc_No_Var,
                   font=('times', 15),
                   width=50)
        e2 = Entry(frame1, textvariable=Emp_Name_Var,
                   font=('times', 15),
                   width=50)
        e3 = Entry(frame1, textvariable=Acc_Office_Var,
                   font=('times', 15),
                   width=50)
        e4 = Entry(frame1, textvariable=Designation_Var,
                   font=('times', 15),
                   width=50)
        e5 = Entry(frame1, textvariable=Contact_Var,
                   font=('times', 15),
                   width=50)
        e6 = Entry(frame1, textvariable=Email_Var,
                   font=('times', 15),
                   width=50)
        e7 = Entry(frame1, textvariable=Address_Var,
                   font=('times', 15),
                   width=50)
        e1.grid(row=0, column=1, padx=20, pady=20)
        e2.grid(row=1, column=1, padx=20, pady=20)
        e3.grid(row=2, column=1, padx=20, pady=20)
        e4.grid(row=3, column=1, padx=20, pady=20)
        e5.grid(row=4, column=1, padx=20, pady=20)
        e6.grid(row=5, column=1, padx=20, pady=20)
        e7.grid(row=6, column=1, padx=20, pady=20)

if __name__=='__main__':
    app = GUI()