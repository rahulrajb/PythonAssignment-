Database={
    'eddygrant':{
        'name': 'Sachin',
        'age':22,
        'email':'eddyXXXXgmail.com',
        'password':'red@123',
        'amount':20000
    },
    'sachin':{
        'name':'Tanuj',
        'age':25,
        'email':'tanuj@gmail.com',
        'password':'red@123',
        'amount':10000
    }
}
while(1>0):
    tempvar=int(input('''Enter your Choice:
    1.Sign in
    2.Sign Up
    3.Exit '''))
    if(tempvar==3):
        break
    elif(tempvar==1):
        username=input("Enter username: ")
        if((username in Database)==True):
            password=input("Enter password: ")
            if((password in Database[username]['password'])==True):
                print("Welcome",Database[username]['name'])
                while(1>0):
                    tempvar1=int(input('''Enter your Choice:
                    1. Check Balance
                    2. Deposit Balance
                    3. Withdrawl
                    4. Change Password
                    5. Log out    '''))
                    if(tempvar1==1):
                        print('Current Balance:',Database[username]['amount'])
                    elif(tempvar1==2):
                        depositamt=int(input("Enter amount: "))
                        Database[username]['amount']=Database[username]['amount']+depositamt
                    elif(tempvar1==3):
                        withdrawlamt=int(input("Enter amount: "))
                        print("Collect your Cash ",withdrawlamt)
                        Database[username]['amount']=Database[username]['amount']-withdrawlamt
                    elif(tempvar1==4):
                        while(1>0):
                            password=input("Enter old password:")
                            if(password==Database[username]['password']):
                                temp_pswd=eval(input("Enter new password:"))
                                Conf_pswd=eval(input("Enter confirm new password:"))
                                if(temp_pswd==Conf_pswd):
                                    Database[username]['password']=temp_pswd
                                    print("Password successfully changed")
                                    break
                                else:
                                    print("Password not matched")
                            else:
                                print("Enter password correctly")
                    elif(tempvar1==5):
                        break
            elif((password in Database[username]['password'])==False) :
                print('Forgot password')
                email=input( 'Enter the email:')
                if(email in Database[username]['email']==True):
                    Database[username]['password']=input('New password:')
                    print("Password successfully changed")
        else:
            print("Username Not Found")
    elif(tempvar==2):
        username=eval(input("Enter your username: "))
        name=eval(input("Enter your name: "))
        age=eval(input("Enter your age: "))
        email=eval(input("Enter your email: "))
        password=eval(input("Enter your password: "))
        amount=eval(input("Enter your amount: "))
        Database[username]={'name':name,'age':age,'email':email,'password':password,'amount':amount}
        print("Username successfully created")
