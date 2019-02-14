import random
from account import Account
from credentials import CheckAccount
    
    # Create account

def create_account(fname,lname,phone,email,password):
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email,password)
    return new_account
     
     # Save account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()
    
    # Delete account

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

    # Find acount

def find_account(email):
    '''
    Function that finds an account by email address and returns an account
    '''
    return Account.find_by_email(email)

    #Check account

def check_existing_accounts(email):
    '''
    Function that check if an account exists with that email address and return a Boolean
    '''
    return Account.account_exist(email)

    #Display all account

def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()

def main():
    print("This is your Account List. What is your name?")
    user_name = input()
    print('\n')
    print(f"Hey Dear {user_name}. what would you like to do?")
    print('\n')
    print("Use short codes")
    print("-"*16)
    print('\n')
    print("Use these short codes : da - display account, fa -find an account, ea -existing account, gp -generate password, np -new password, dl -delete account, ex -exit the account list ")
    print('\n')
    print("New Account")
    print("-"*11)

    print ("First name")
    print("-"*10)
    f_name = input()

    print("Last name")
    print("-"*10)
    l_name = input()

    print("Phone number")
    print("-"*12)
    p_number = input()

    print("Email address")
    print("-"*13)
    e_address = input()
                              
    print("Account's Password")
    print("-"*18)
    print("\nChoose:")
    print("-"*10)
    print("'gp' - Application to generate password for you, 'np' - new password")
    a_password = input()
    if a_password == "np":
                print("\nEnter your password")
                print("-"*18)
                pass_word = input()
    elif a_password == "gp":
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                pass_word = "".join(random.choice(chars) for _ in range(6))
                print(f"\nYour password is: **{pass_word}**")

    #save_accounts(create_accounts(view_password,account,login_name,pass_word))
    print("\n")
    #print(f"New credentials **{account}**, **{login_name}**, **{pass_word}** created")
    new_account = Account(f_name,l_name,p_number,e_address,a_password)
    new_account.save_account()
    # save_accounts(create_account(f_name,l_name,p_number,e_address,a_password)) # create and save new account.
    print ('\n')
    print(f"New Account {f_name} {l_name} is created")
    print ('\n')
    while True:
                
                short_code = input().lower()
                # if short_code == 'ca':
                        
                            
                if short_code == 'da':

                        if (len(display_account())>0):
                                print("Here is some elements of your accounts")
                                print('\n')

                                for account in display_account():
                                        print(f"{account.first_name} {account.last_name} .....{account.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any account saved yet")
                                print('\n')

                elif short_code == 'fa':

                        print("Enter the email you want to search for")
                        print('\n')

                        e_address = input()
                        if check_existing_accounts(e_address):
                                search_account = find_account(e_address)
                                print(f"{search_account.first_name} {search_account.last_name}")
                                print('-' * 12)

                                print(f"Phone number.......{search_account.phone_number}")
                                print(f"Email address.......{search_account.email}")
                                print(f"Account's Password.......{search_account.password}")
                                print('\n')
                        else:
                                print("That account does not exist")

                elif short_code == "ea":

                        print("\nLogin to your account")
                        print("-"*20)
                        username_input = input()
                        user_password_input = input()
                        for account in Account.account_list:
                                if account.email == username_input and account.password == user_password_input:       
                                        print("The email is right")
                                        print("-" * 6)
                                        
                                # elif  account.password == password:
                                #         print("\nPassword:")
                                #         print("-"*10)
                                #         user_password_input = input()
                                #         view_password = user_password_input
                                #         print("Successfully")

                                else:
                                        print("This account don't exist")
                        # if check_existing_accounts(user_password_input):
                        #         print("\nYou can put the new one!")
                        #         print("New Credential")
                        #         print("-" *10)

                        #         print("\nWhich account you want to be applied to?")
                        #         print("-"*40)
                        #         account = input()

                        #         print(f"\nyour username for the {account} account?")
                        #         print("-"*40)
                        #         login_name = input()

                        #         print("\nChoose:")
                        #         print("-"*10)
                        #         print("'gp' - Application to generate password for you, 'np' - new password")
                        #         password_creation_input = input()
                        #         if password_creation_input == "np":
                        #                 print("\nEnter your password")
                        #                 print("-"*10)
                        #                 pass_word = input()
                        #         elif password_creation_input == "gp":
                        #                 chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                        #                 pass_word = "".join(random.choice(chars) for _ in range(6))
                        #                 print(f"\nYour password is: **{pass_word}**")

                        #         save_credentials(create_credentials(view_password,account,login_name,pass_word))
                        #         print("\n")
                        #         print(f"New credentials **{account}**, **{login_name}**, **{pass_word}** created")
                                                
                elif short_code == 'dl':

                        print("Are u sure you want to delete this account?")
                        print('\n')
                        print("Yes")
                        new_account.delete_account()
                        print("Account deleted") 
                #else:
                        #print("This account does not exist")
                        # e_address = input()
                        # if check_existing_accounts(e_address):
                        #         search_account = delete_account(e_address)
                        #         print(f"{search_account.first_name} {search_account.last_name}")
                        #         print('-' * 12) 
                        #         print('\n')
                        #         print("Delete it") 

                        # else:
                        #         print("That account does not exist")
     

                elif short_code == "ex":
                        print("Finish .......")
                        break
                else:
                        print("I really don't get that.")
                        
if __name__ == '__main__':

        main()

