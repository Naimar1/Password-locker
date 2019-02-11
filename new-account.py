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
        self.assertEqual(len(account.account_list),1)
        contact_list = [] 
 
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

if __name__ == '__main__':
    unittest.main()


