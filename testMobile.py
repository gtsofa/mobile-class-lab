import unittest

from mobile import Mobile

class MobileClassTest(unittest.TestCase):
    """docstring for MobileClassTest"""

    def test_mobile_instance(self):
        nokia = Mobile('Nokia')
        self.assertIsInstance(nokia, Mobile, msg='The object should be an instance of the `Mobile` class')

    def test_object_type(self):
        nokia = Mobile('Nokia')
        self.assertTrue((type(nokia) is Mobile), msg='The object should be a type of `Mobile`')

    def test_default_mobile_name(self):
        mp = Mobile()
        self.assertEqual('MobilePhone', mp.name, msg='The mobile should be called `MobilePhone` if no name was passed as an argument')

    def test_default_mobile_model(self):
        mp = Mobile()
        self.assertEqual('MP', mp.model, msg="The mobile's model should be called 'MP' if no model was passed as an argument.")

    def test_mobile_properties(self):
        blackberry = Mobile('Blackberry', 'Passport')
        self.assertListEqual(['Blackberry', 'Passport'],
                             [blackberry.name, blackberry.model, blackberry.os],
                             msg='The mobile name, model and os should be a property of the Mobile')

    def test_mobile_simcard(self):
        iPhone = Mobile('Iphone', 'Iphone6s')
        nokia = Mobile('Nokia', 'NokiaLumia520')
        self.assertListEqual([iPhone.simcard_type, nokia.simcard_type,
                             Mobile('Samsung', 'SamsungGalaxyS8').simcard_type],
                             ['NanoSim', 'MicroSim', 'NanoSim'],
                             msg='The mobile should have a NanoSim simcard type excepts its a NokiaLumia520')

    def test_mobile_browser(self):
        phone = Mobile('SmartPhone', 'BasicPhone')
        blackberry = Mobile('Blackberry', 'Priv')
        self.assertEqual([1, 0], [phone.num_of_browser, blackberry.num_of_browser],
                         msg='The mobile should have atleast one (1) browser unless its a basic phone')

    def test_mobile_type(self):
        blackberry = Mobile('Blackberry', 'Priv')
        self.assertTrue(blackberry.is_smartphone(),
                        msg='The mobile should be a smartphone if it is not a basic phone')


if __name__ == "__main__":
    unittest.main()
