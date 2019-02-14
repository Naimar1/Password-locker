class Account:
    '''
    Class that show new instances of account
    '''
    account_list = [] 
    def __init__(self,first_name,last_name,phone_number,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New account first name.
            last_name : New account last name.display_accounts
            number: New account phone number.
            email : New account email address.
            password : New account password.
            
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)
        
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0788501277","user@gmail.com","123") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        
        '''
        Method that takes a mail and returns an account that matches that mail.

        Args:
            email: email address to search for
        Returns :
            Account of the person that matches the email address.
        '''

        for account in cls.account_list:
            if account.email == email:
                print("")
                return account

    @classmethod
    def account_exist(cls,email):
        '''
        Method that checks if a account exists from the account list.
        Args:
            email: email address to search for
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.email == email:
                    return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns account list
        '''
        return cls.account_list