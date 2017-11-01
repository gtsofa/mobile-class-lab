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

    #if one arg is assigned all args need to be assigned as well that's why use None
    def __init__(self, name=None, imeiCode=None, model=None, simCard='NanoSim', os=None):
        self.name = name
        self.imeiCode = imeiCode
        self.model = model
        self.simCard = simCard
        self.os = os

class Nokia(Mobile):
    """Nokia class implementation
    Attributes:
        browser = a string representing the type of a browser the Nokia phone has; which will be used to test if it's a smartphone or just a basic phone
        
    """
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
            
    def cameraClick(self):
        #Function that shows camera functionality
        return 'Camera clicked!'

class Samsung(Mobile):
    """class Samsung extends Mobile class functionality and adds its own attributes and functions.
    Attributes:
    cameraMode: A string representing the camera mode
        
    """
    def __init__(self, name=None, imeiCode=None, model=None, simCard=None, os=None, browser=None, cameraMode='Panaroma'):
        super(Samsung, self).__init__(name, imeiCode, model, simCard=None, os=None)
        self.cameraMode = cameraMode
        
     #This is one overloaded method which shows camera functionality as well but with its camera's different mode(panaroma)     
    def cameraClick(self, cameraMode):
        return "Camera clicked in {} cameraMode".format(self.cameraMode)
