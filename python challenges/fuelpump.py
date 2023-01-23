class Caixa():
    def __init__(self, user:str, password:str, balance:float=0):
        self.user = user
        self.password = password
        self.balance = balance
        self.history = []
        
    def addHistory(self, user, option, *args):
        self.history.append([user, option, self.balance, *args])
        
    def entrada(self, value:float):
        if self.balance + value > 0:
            self.balance += value
            return True
        else: return False
        
    def saida(self, value:float):
        if self.balance >= value:
            self.balance -= value
            return True
        else: return False 
        
    def getBalance(self):
        return self.balance
        
    def setBalance(self, value):
        self.balance = value
    
class BombaCombustivel():
    def __init__(self, type:str, literPrice:float, fuelQtt:float):
        self.type = type
        self.literPrice = literPrice
        self.fuelQtt = fuelQtt
        
    def fuelByValue(self, value):
        if self.fuelQtt >= (value/self.literPrice):
            self.fuelQtt -= (value/self.literPrice)
            return f'Supplied {(value/self.literPrice):.2f} liters.'
        else: return f'It was not possible to supply.\nFuel quantity: {self.fuelQtt:.2f} liters.'
    
    def fuelByLiter(self, liter):
        if self.fuelQtt >= liter:
            self.fuelQtt -= liter
            return f'Supplied ${liter*self.literPrice:.2f}.'
        else: return f'It was not possible to supply.\nFuel quantity: {self.fuelQtt:.2f} liters.'
    
    def setValue(self, value:float):
        self.literPrice = value
    
    def setTypeComb(self, type:str):
        self.type = type
    
    def setFuelQtt(self, qtt:float, valuePaid:float):
        balance = c.getBalance()
        if balance >= (qtt * valuePaid):
            c.setBalance(balance - (qtt * valuePaid))
            self.fuelQtt += qtt
            return True
        else: return False
    
    def getFuelQtt(self):
        return self.fuelQtt
        
    def getValue(self):
        return self.literPrice
b = BombaCombustivel('Gas', 5.55, 100)
c = Caixa('1', '1', 100)
def open():
    
    
    print('---------------------------------------')
    print('--             Fuel Pump             --')
    print('---------------------------------------')
    
    while True:
        conect = False
        print()
        user = input('User or "-1" from exit: ')
        if user == "-1": break
        password = input('Password: ')
        
        if c.user == user:
            if c.password == password:
                conect = True
            else: print ('\nInvalid user or password.') 
        else: print ('\nInvalid user or password.') 
        
        def cleanVar():
            option = False
            liter = False
            qtt = False
            valueBomb = False
            
        valueCOMB = 2.10
        
        while conect:
            print()
            print('1- Fuel by liter')
            print('2- Fuel by value')
            print('3- Change liter value')
            print('4- Check liter value')
            print('5- Change fuel quantity')
            print('6- Check fuel quantity')
            print('7- History')
            print('8- Balance')
            print('9- exit')
            
            try:
                cleanVar()
                option = int(input('Options: '))
                if option == 9:
                    break
                elif option == 1:
                    liter = float(input('\nHow many liters: '))
                    c.addHistory(user, option, liter, b.getFuelQtt(), b.getValue())
                    c.entrada(liter*b.getValue())
                    print(b.fuelByLiter(liter))
    
                elif option == 2:
                    valueBomb = float(input('\nHow much: '))
                    c.addHistory(user, option, valueBomb, b.getFuelQtt(), b.getValue())
                    c.entrada(valueBomb/b.getValue())
                    print(b.fuelByValue(valueBomb))
                    
                elif option == 3:
                    valueBomb = float(input('\nWhat is new value: '))
                    b.setValue(valueBomb)
                    c.addHistory(user, option, valueBomb, b.getFuelQtt(), b.getValue())
                    print(f'New value is ${valueBomb:.2f}.')
                    
                elif option == 4:
                    c.addHistory(user, option, b.getValue())
                    print(f'\nValue of fuel: ${b.getValue():.2f}.')
                    
                elif option == 5:
                    qtt = float(input('\nWhat is the amount to add: '))
                    if b.setFuelQtt(qtt, valueCOMB):
                        c.addHistory(user, option, valueCOMB, qtt, b.getFuelQtt(), b.getValue())
                        print(f'Total fuel in liters: {b.getFuelQtt():.2f}.')  
                    else: print(f'balance insufficient: ${c.getBalance():.2f}.')
                    
                elif option == 6:
                    c.addHistory(user, option, b.getFuelQtt())
                    print(f'\nTotal fuel in liters: {b.getFuelQtt():.2f}.')
                    
                    
                elif option == 7:
                    print('----------------History------------------')
                    print('Usr - Oper - Args')
                    for i in c.history:
                        print(i)
                        
                elif option == 8:
                    c.addHistory(user, option, b.getValue())
                    print(f'\nBalance: ${c.getBalance():.2f}.')
                    
                else: print('Invalid option.')
                
                
                    
            except ValueError as e:
                print('Invalid option.')
                continue