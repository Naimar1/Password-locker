from account import Account

def create_account(fname,lname,phone,email):
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email)
    return new_account
    


        u=input()
        username="naimar1"
        print(u)
        p=input()
        password="12345"
        print(p)
        if(u!=username and p!=password):
            print("Not true")
        else:
            print("Sign up")