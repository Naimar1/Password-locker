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
            self.assertEqual(self.new_account.first_name,"Ange")
            self.assertEqual(self.new_account.last_name,"Ingabire")
            self.assertEqual(self.new_account.phone_number,"0788262733")
            self.assertEqual(self.new_account.email,"ange@gmail.com")
            self.assertEqual(self.new_account.password,"ange234")


