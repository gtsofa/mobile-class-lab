import unittest

from mobile import Mobile, Nokia,Samsung

class TestMobile(unittest.TestCase):
    #Test the Mobile Class

    def test_mobile_isinstance(self):
        mobile = Mobile('Mobile', '33F34343435235', 'Priv', 'NanoSim', 'BlackBerry OS 10.3')
        self.assertIsInstance(mobile, Mobile, msg='The object should be an instance of a Mobile class')

    def test_samsung_isinstance(self):
        samsung = Samsung('Samsung', 'CEGF34343476210', 'SamsungGalaxyS8', 'NanoSim', 'Android7')
        self.assertIsInstance(samsung, Samsung, msg='The object should be an instance of a Samsung class')

    def test_nokia_isinstance(self):
        nokia = Nokia('Nokia', 'IMX77333376244', 'Asha', 'NanoSim', 'Android7')
        self.assertIsInstance(nokia, Nokia, msg='The object should be an instance of a Nokia class')

    def test_object_type(self):
        mobile = Mobile('Mobile', '33F34343435235', 'Priv', 'NanoSim', 'BlackBerry OS 10.3')
        self.assertTrue((type(mobile) is Mobile), msg='The object should be a type of Mobile')
        samsung = Samsung('Samsung', 'XX2222222222', 'GalaxyS8', 'NanoSim', 'Android7')
        self.assertTrue((type(samsung) is Samsung), msg='The object should be a type of Samsung')
        nokia = Nokia('Nokia', 'IEDF34343435235', 'Lumia520', 'Microsim', 'Android7')
        self.assertTrue((type(nokia) is Nokia), msg='The object should be a type of Nokia')




if __name__ == '__main__':
    unittest.main(exit=False)
