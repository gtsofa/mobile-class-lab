class Mobile(object):

    """OOP concepts theoretically linking it with real world and programming world, taking Mobile as an object.
    A Mobile has the following the properties:

    Attributes:
    imeiCode: a number representing the mobile's manufacture code
    isSingleSim: a boolean stating the number of simcards the mobile can accomodate
    processor: a string representing the amount of processing power
    internalMemory: a string representing the capacity the mobile has.
    brand: a string representing the mobile brand
    model: a string representing the model of the mobile

    functionality:
    dial():
    receive():
    sendMessage():
    receiveMessage():
    connectBlueTooth():
    getImeiCode():

    """

    def __init__(self, imeiCode, isSingleSim, processor, internalMemory, brand, model):
        self.imeiCode = imeiCode
        self.isSingleSim = isSingleSim
        self.processor = processor
        self.internalMemory = internalMemory
        self.brand = brand
        self.model = model

    def getImeiCode(self, imeiCode):
        """Returns the imeiCode of the mobile"""
        self.imeiCode = imeiCode
        return print("imeiCode - IEDF34343435235")

    def dial(self):
        print("Dial a number")

    def receive(self):
        print("Receive a call")

    def sendMessage(self):
        print("Message sent")

class Samsung(Mobile):
    """Polymorphism"""
    def getWIFIConnection(self):
        print("WIFI connected")

    def cameraClick(self, cameraMode):
        print("Camera clicked in " + cameraMode + "Mode")
