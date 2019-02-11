import unittest
from account import Account

class CheckAccount(unittest.TestCase):
    '''
    Check class that define test cases for the account class.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_account = Account("Ange","Ingabire","0788262733","ange@gmail.com","ange234")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"Ange")
        self.assertEqual(self.new_account.last_name,"Ingabire")
        self.assertEqual(self.new_account.phone_number,"0788262733")
        self.assertEqual(self.new_account.email,"ange@gmail.com")
        self.assertEqual(self.new_account.password,"ange234")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)
       
        account_list = [] 
 
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
            test_account = Account("Test","user","0712345678","user@gmail.com","123") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678","user@gmail.com","123") # new contact
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678","user@gmail.com","123") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    def test_find_account_by_mail(self):
        
        '''
        test to check if we can find an account by email address and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344","user@gmail.com","123") # new contact
        test_account.save_account()

        found_account = Account.find_by_mail("user@gmail.com")

        self.assertEqual(found_account.password,test_account.password)

   

if __name__ == '__main__':
    unittest.main()


