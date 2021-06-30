#create class

class Atm(object):
    #constructor
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber


#open method for opening the atm
    def open(self):
        print('opening atm')

#printing everthing in the terminal
atm1 = Atm("123","456")
print (atm1.atmCardNumber)
atm1.open()