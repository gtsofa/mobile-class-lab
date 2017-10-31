import unittest

from mobile import Mobile

class TestMobile(unittest.TestCase):
    #Test the Mobile Class

    def test_mobile_isinstance(self):
        nokia = Mobile('nokia', 'imeiCode', 'model', 'simCard', 'os')
        self.assertIsInstance(nokia, Mobile, msg='The object should be an instance of a Mobile class')



if __name__ == '__main__':
    unittest.main()
