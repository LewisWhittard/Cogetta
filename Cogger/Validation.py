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
            print("Valid")
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
        print(valid)
        return valid
        
    def CheckBackAndFrontOfStringNotDash(self, key):
        Valid = True;
        
        KeyList = key.split("+")
        
        for x in KeyList:
            if Valid == True:
                Valid = self.CheckBackAndFrontOfStringNotDashSingle(x)
        return Valid
    
    def CheckBackAndFrontOfStringNotDashSingle(self, string):
        result = True;
        back = self.CheckBackOfStringIsNotDash(string)
        front = self.CheckFrontOfStringIsNotDash(string)
        if back == False or front == False:
            result = False
            print(back)
            print(front)
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
    
    def ValidationManager(self):
        KeyValidChar = False
        KeyValidLength = False
        DashNotStartOrEnd = False
        WheelHolders = []
        while DashNotStartOrEnd == False or KeyValidChar == False or KeyValidLength == False or KeyValidUniqueChars == False:
            Key = self.ReturnKeyTryCatch()
            KeyValidChar = self.CheckString(Key)
            print("Char Pass",KeyValidChar)
            if KeyValidChar == True:
                DashNotStartOrEnd = self.CheckBackAndFrontOfStringNotDash(Key)
                if DashNotStartOrEnd == True:
                    WheelHolders.append(WheelHolderClass.WheelHolder());
                    WheelHolders[0].ImportKey(Key)
                    KeyValidLength = self.CheckKeyLength(WheelHolders[0])
                    print("KeyValidLength", KeyValidLength)
                    if KeyValidLength == True:
                        KeyValidUniqueChars = self.CheckKeyValuesAreUnique(WheelHolders[0])
                        print("KeyValidUniqueChars", KeyValidUniqueChars)
            WheelHolders.clear()
        return Key        
            
            
        
            
            
        
        
            
        
    
    
    