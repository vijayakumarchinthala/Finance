
import pymysql as pym
'''****************************************************************************
                 FUNCTION TO CALL MENU
*****************************************************************************'''
def con():
    a=input("Press any key to continue")
'''****************************************************************************
                FUNCTION FOR  LOAN ENQUIRE
***************************************************************************'''

def months2():
    n=int(input("Enter the Account Number:"))  
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from months2')
    data=cur.fetchall()
    for i in data:
      if n==i[0]:
       
        print("\n\t\tName:",i[1])
        print("\nFirst month loan:",i[2])
        print("Second month loan:",i[3])
        print("Third month loan:",i[4])
        print("Fourth month loan:",i[5])
        print("Fifth month loan:",i[6])
        print("Sixth month loan:",i[7])
        break

"""***************************************************************************
              FUNCTION  FOR LOAN REPAYMENT
***************************************************************************"""

def loan_repay():
    n=int(input("Enter the Account Number:"))  
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    ans=input('Do you want to pay your monthly installment  (y/n)...')
    month=int(input('Enter the month number:'))
    if month>=1 and month<7:
        if ans=='y':
            for i in data:
                
                if n==i[0]:
                    print('Your Monthly istallment per month is:',i[6])
                    if i[5]==0:
                        print("You had cleared your loan amount :)")
                        break
                    
                    st='Update emi set In_Amount={} where Acc_no={}'
                    
                    if month==1:
                        
                    
                        st1='update months2 set Fi_Mo="{}" where Acc_no={}'
                    elif month==2:
                    
                        st1='update months2 set Se_Mo="{}" where Acc_no={}'
                    elif month==1:
                    
                        st1='update months2 set Thi_Mo="{}" where Acc_no={}'
                    elif month==1:
                    
                        st1='update months2 set Fo_Mo="{}" where Acc_no={}'
                    elif month==1:
                    
                        st1='update months2 set Fiv_Mo="{}" where Acc_no={}'
                    else:
                    
                        st1='update months2 set Si_Mo="{}" where Acc_no={}'
                    
                    
                    cur.execute(st.format(i[5]-i[6],n))
                    mycon.commit()
                    
                    cur.execute(st1.format("Paid",n))
                    mycon.commit()
                    
                    break
            else:
                print("Please Enter the Valid Account Number")
        else:
            print('Thank you for your cooperation')
            
        cur.execute('select * from emi')
        data=cur.fetchall()
        
        for i in data:
            if n==i[0]:
                print('Your remaining loan amount',i[5])
                break
        else:
            print("Please Enter the Valid Account Number")
            
    else:
       print('Enter month between 1 and 6:')
       month=int(input('Enter the month number:'))

"""***************************************************************************
                FUNCTION FOR EMI Details    
****************************************************************************"""

def emiinfo():
    print("\t\t\t\t\t\t\tKey Factors Affecting the EMI")
    print("\n\tOur Company interset rate is about 2% before taking the Loan,Please read the Following document carefully.")
    print("\n\tOur Interest rate calcalution:")
    print("\n\n\t1.Principal(P): It is the sum of money that you borrow from the lender.")
    print("Principal is an essential factor while determining the cost of your loan as Interest is calculated as a percentage of your principal")
    print("\n\t2.Tenure of Loan(T): It is the time period for which you have borrowed.")
    print("It has a major impact on EMI amount. Monthly installment is lesser for longer tenure loans and vice a versa.") 
    print("\n\t3.Interest Rate(R):  It is the rate at which lender offers you the loan.")
    print("Its important to do the basic research on interest rates offered in the market.Getting a competitive rate helps you work out a cost of loan in your benefit.")
    print("\n\n\tEquated Monthly Installment(EMI)=P*T*R/100")
    
    

"""***************************************************************************
                           ABOUT  US
****************************************************************************"""

def  About_us():
    print("\t\t\t\t\t\t\t\t COMPUTER PROJECT")
    print("\nPROJECT TITLE:FINANCE MANAGEMENT")
    print("\n\tDevelopers: N.someswar , T.Budha prabhas , D.vijaya Krishna")
    print("\tClass:XII")
    print("\tSUBJECT:Computer Science")
    print("\tRequired Software:Spyder")
    print("\n\n • As a loan officer:-")
    print(" • Our primary goal is to determine the best mortgage loan program for our customer (and of course, close the loan).")
    print(" • We can understand details like property type, loan amount, credit score etc., is the key to providing  our customers great service.")
    print(" • But to keep our business healthy, we also need a steady flow of new and repeat customers coming through our door.")
              


"""***************************************************************************
             FUNCTION TO CLOSE ACCOUNT
***************************************************************************"""

def  close_account():
    n=int(input("Enter the Account Number:"))
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    
    for i in data:
        if n==i[0]:
           cur.execute("delete from emi where Acc_No=%s"%n)
           mycon.commit()
           cur.execute("delete from months2 where Acc_No=%s"%n)
           mycon.commit()
           print("Your Account was successfully deleted")
           break
    else:
        print("Please Enter the Valid Account Number")
          

"""***************************************************************************
             FUNCTION  TO  LOGIN  THE PROGRAM
****************************************************************************"""    

def login():
    n=int(input("Enter the Account Number:"))
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    
    for i in data:
        if n==i[0]:
            print('\n')
            print("Login Successful")
            print("Total amount is:",i[5])
            break   
    else:
        print("Please Enter the Valid Account Number")
            

        
"""***************************************************************************
                 FUNCTION TO  ENQUIRY BALANCE AMOUNT
****************************************************************************"""

def  balance_enquiry():
    n=int(input("Enter the Account Number:"))
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    for i in data:
        if n==i[0]:
            print('\n')
            print('Account Number:',i[0])
            print('Name:',i[1])
            print('Address:',i[2])
            print('Number:',i[3])
            print('Loan:',i[4])
            print('\n'+'\n')
            break
    else:
        print("Please Enter the Valid Account Number")

def Interest_rate():
    
    Acc_no=int(input('Enter the account number:'))

    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    for i in data:
        if i[0]==Acc_no:
            print('Succesful')
            
            print('Total Amount with interest amount:',i[5])
            
            print('Months:',6)
            
            
    
   
    
"""***************************************************************************
               FUNCTION TO  CREATE NEW ACCOUNT
****************************************************************************"""

def New_Account():
    Acc_no=0
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    for i in data:
        Acc_no=i[0]
    Name=input('Enter the name:')
    Address=input('Enter adddress:')
    Number=input('Enter valid number:')
    global Loan
    Loan=int(input('Enter lOAN:'))
    
    print("Log in successfully")
    print("Our interest rate is 2%")
    p=Loan
    r=2
    a=p*6*r/100
    x=p+a
    
    y=0
    y=x//6
    print("\n\nThe Monthly installment Amount per month:",y)
            
            
    st='''INSERT INTO emi(Acc_no,Name,Address,Number,Loan,In_amount,emi)
        VALUES({},'{}','{}','{}',{},{},{})'''.format(Acc_no+1,Name,Address,Number,Loan,x,y)
        
   
    
    cur.execute(st)
    mycon.commit()
    
    print('your account succesfully created')
    print('your account number is',Acc_no+1)
    
    st1='''INSERT INTO months2(Acc_no,Name)
        VALUES({},'{}')'''.format(Acc_no+1,Name)
        
    cur.execute(st1)
    mycon.commit()
    
  
       
"""***************************************************************************
                 FUNCTION TO ENQUIRE THE NUMBER OF ACCOUNTS
***************************************************************************"""

def number_of_accounts():
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='emi')
    cur=mycon.cursor()
    cur.execute('select * from emi')
    data=cur.fetchall()
    
    for i in data:
        print('\n')
        print('Account Number:',i[0])
        print('Name:',i[1])
        print('Address:',i[2])
        print('Number:',i[3])
        print('Total Amount:',i[5])
        print('Interest Amount for the loan amount :',i[6])
        print('\n'+'\n')

"""***************************************************************************
                       INTRODUCTORY FUNCTION
***************************************************************************"""
               
def introduction():
    
    print("\n\n\t\t\t\t\t\t\tHARI OM")
    print ("\n\n\t\t\t\t\tFINANCE MANAGEMENT")
    print("\n\n MADE BY:Someswar\n\t\tBudha prabhas\n\t\tVijaya Krishna")
    print("\n\nSCHOOL NAME:GVK Chinmaya Vidyalaya")
    print("\n\t\t\t\t Kothuru(v),Indukurupeta(M),Nellore(dt)")
 
"""***************************************************************************
                    THE  MAIN FUNCTION OF THE PROGRAM 
***************************************************************************"""    

introduction()


a=1



while a:
    print( 3*"\n",221*"=")
    print ('''MAIN MENU
    
    1. About_us
    2. EMI Info
    3. login       
    4. New Account
    5. Number of accounts
    6. Balance Enquiry
    7. Close An Account
    8. Interest Amount
    9. loan Repayment
   10. loan enquiry
   11. Exit
    ''')
    
    ch=int(input("Enter the choice(1-11): "))
    if ch==3:
        login()
        con()
    elif ch==4:
        New_Account()
        con()
    elif ch==5:
         number_of_accounts()
         con()
    elif ch==6:
         balance_enquiry()
         con()
    elif ch==7:
        close_account()
        con()
    elif ch==8:
        Interest_rate()
        con()
    elif ch==1:
        About_us()    
        con()
    elif ch==2:
        emiinfo()
        con()
    elif ch==11:
        print("\n\n\t\t\t\t\t\t************THe END*************")
        break
    elif ch==9:
        loan_repay()
        con()
    elif ch==10:
        months2()
        con()
    else:
        print("Please Enter the Right Choice")
        
               
"""*****************************************************************************
				END OF PROJECT
*****************************************************************************"""
        








    
