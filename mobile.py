class Mobile:
    """OOP concepts theoretically linking it with real world and programming world, taking Mobile as an object.
    A Mobile has the following the properties:

    Attributes:
    imeiCode: a number representing the mobile's manufacture code
    name: a string representing the mobile brand name
    model: a string representing the model of the mobile
    os: a string representing operating system of the mobile device

    functionality:
    """

    def __init__(self, name=None, imeiCode=None, model=None, simCard='NanoSim', os=None):
        self.name = name
        self.imeiCode = imeiCode
        self.model = model
        self.simCard = simCard
        self.os = os

class Nokia(Mobile):
    #Class Nokia extends class Mobile
    def __init__(self, name=None, imeiCode=None, model=None, simCard='NanoSim', os=None, browser=None):
        #Reusing the super class method[Mobile] by the child
        super(Nokia,self).__init__(name, imeiCode, model, simCard='Microsim', os='Nougat')
        self.browser = browser

    def has_browser(self):
        #Method to determine weather object nokia has_browser
        if self.browser == 'html5':
            return True
        elif self.browser == 'none':
            return False
        return False

    def is_smartphone(self):
        if self.browser == 'html5':
            return '{} model {} is a smartphone'.format(self.name, self.model)
        elif self.browser == 'none':
            return '{} model {} is a basic phone'.format(self.name, self.model)

class Samsung(Mobile):
    pass
