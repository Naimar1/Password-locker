class Account:
    '''
    Class that show new instances of account
    '''

    def __init__(self,first_name,last_name,phone_number,email,password):

         '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New account first name.
            last_name : New account last name.
            number: New account phone number.
            email : New account email address.
            password : New account password.
            
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    @classmethod
    def display_account(cls):
        '''
        method that returns account list
        '''
        return cls.account_list