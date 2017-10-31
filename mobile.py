class Mobile(object):
    """OOP concepts theoretically linking it with real world and programming world, taking Mobile as an object.
    A Mobile has the following the properties:

    Attributes:
    imeiCode: a number representing the mobile's manufacture code
    name: a string representing the mobile brand name
    model: a string representing the model of the mobile
    os: a string representing operating system of the mobile device

    functionality:


    """

    def __init__(self, name, imeiCode, model, simCard, os):
        self.name = name
        self.imeiCode = imeiCode
        self.model = model
        self.simCard = simCard
        self.os = os
