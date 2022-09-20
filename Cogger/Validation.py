import CharacterSet
import WheelHolderClass

class StringValidation():
    
    def __init__(self):
        self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.List = self.CharacterSetClass.inputValues
        self.WheelHolders = []
        
    def CheckString(self,Message):
        Valid = True
        MessageLength = len(Message)
        
        if MessageLength <= 0:
            Valid = False
            print("No String")
            
        for x in Message:
            if Valid == True:
                Valid = self.CheckChar(x)
        
        return Valid    
        
    
    def CheckChar(self,Char):
        Valid = True
        if Char in self.List:
            Valid = True
        else:
            Valid = False
            print("Unsupported charecter detected:",Char)
            
        return Valid
    
    def ReturnMessageTryCatch(self):
        Message = None
        NotMaxString = False
        while NotMaxString == False:
            try:
                Message = input("What is your message:")
                NotMaxString = True
            except:
                print("Message Error")
        
        return Message
    
    def ValidationManager(self):
        Message = None
        StringValid = False
        while StringValid == False:
            Message  = self.ReturnMessageTryCatch()
            StringValid = self.CheckString(Message)
        return Message
            
        
        
    
    
class KeyValidation():
    
    def __init__(self):
        self.KeySetClass = CharacterSet.KeySet()
        self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.List = self.KeySetClass.inputValues
        
    def ReturnKeyTryCatch(self):
        Key = None
        NotMaxString = False
        while NotMaxString == False:
            try:
                Key = input("What is your key:")
                NotMaxString = True
            except:
                print("Key Error")
        
        return Key
        
    
    def CheckString(self,Message):
        Valid = True
        MessageLength = len(Message)
        
        if MessageLength <= 0:
            Valid = False
            print("No Key")
            
        for x in Message:
            if Valid == True:
                Valid = self.CheckChar(x)
        
        return Valid    
        
    
    def CheckChar(self,Char):
        Valid = True
        if Char in self.List:
            Valid = True
        else:
            Valid = False
            print("Unsupported charecter detected:",Char)
            
        return Valid
    
    def CheckKeyLength(self, WheelHolder):
        
        Valid = True
        
        for x in WheelHolder.Wheels:
            if Valid == True:
                Valid = self.CheckWheelLength(x)
            
        
        return Valid
    
    def CheckWheelLength(self,Wheel):
        valid = True
        valueCount = len(Wheel.ImportedWheelKey)
        
        if valueCount == self.CharacterSetClass.count:
            valid = True
        else:
            valid = False
            print("Invalid Key", valueCount, self.CharacterSetClass.count)
        
        return valid
    
    def CheckKeyValuesAreUnique(self, WheelHolder):
        Valid = True
        for x in WheelHolder.Wheels:
            if Valid == True:
                Valid = self.CheckWheelValuesAreUnique(x)
        return Valid
    
    def CheckWheelValuesAreUnique(self,Wheel):
        valid = True
        valid = len(Wheel.ImportedWheelKey) == len(set(Wheel.ImportedWheelKey))
        if valid == False:
            print("Invalid Wheel Key values are not unique")
        return valid
        
    def CheckBackAndFrontOfStringAllWheels(self, key):
        Valid = True;
        
        KeyList = key.split("+")
        
        for x in KeyList:
            if Valid == True:
                Valid = self.CheckBackAndFrontOfString(x)
        return Valid
    
    def CheckBackAndFrontOfString(self, string):
        result = True;
        notBackDash = self.CheckBackOfStringIsNotDash(string)
        notFrontDash = self.CheckFrontOfStringIsNotDash(string)
        notBackPlus = self.CheckBackOfStringIsNotPlus(string)
        notFrontPlus = self.CheckFrontOfStringIsNotPlus(string)
        
        if notBackDash == False or notFrontDash == False or notBackPlus == False or notFrontPlus == False:
            result = False
            print("Check start and end of each wheel key")
        return result
        
    def CheckBackOfStringIsNotDash(self, string):
        value = True;
        if string[0] == "-":
            value = False
        return value
        
    
    def CheckFrontOfStringIsNotDash(self, string):
        value = True;
        if string[-1] == "-":
            value = False
        return value
    def CheckBackOfStringIsNotPlus(self, string):
        value = True;
        if string[0] == "+":
            value = False
        return value
        
    
    def CheckFrontOfStringIsNotPlus(self, string):
        value = True;
        if string[-1] == "+":
            value = False
        return value
    
    def ValidationManager(self):
        KeyValidChar = False
        KeyValidLength = False
        StartOrEndCheck = False
        WheelHolders = []
        while StartOrEndCheck == False or KeyValidChar == False or KeyValidLength == False or KeyValidUniqueChars == False:
            Key = self.ReturnKeyTryCatch()
            KeyValidChar = self.CheckString(Key)
            if KeyValidChar == True:
                StartOrEndCheck = self.CheckBackAndFrontOfStringAllWheels(Key)
                if StartOrEndCheck == True:
                    WheelHolders.append(WheelHolderClass.WheelHolder());
                    WheelHolders[0].ImportKey(Key)
                    KeyValidLength = self.CheckKeyLength(WheelHolders[0])
                    if KeyValidLength == True:
                        KeyValidUniqueChars = self.CheckKeyValuesAreUnique(WheelHolders[0])
            WheelHolders.clear()
        return Key
    
class NumberValidation():
    
    def ReturnKeyTryCatch(self):
        Key = None
        NotMaxString = False
        while NotMaxString == False:
            try:
                Number = int(input("How many wheels:"))
                NotMaxString = True
            except:
                print("Number Error")
        
        return Number
            
            
        
            
            
        
        
            
        
    
    
    