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
        self.MaxValue = self.CharacterSetClass.maxId
        self.MinimumValue = self.CharacterSetClass.minId
        
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
            print("No key")
            
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
            print("Invalid key", valueCount, self.CharacterSetClass.count)
        
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
            print("Invalid wheel key values are not unique")
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
        notFrontPlus = self.CheckFrontOfStringIsNotPlus(string)
        if notFrontPlus == True:
            notBackDash = self.CheckBackOfStringIsNotDash(string)
            notFrontDash = self.CheckFrontOfStringIsNotDash(string)
            notBackPlus = self.CheckBackOfStringIsNotPlus(string)
        else:
            notBackDash = False
            notFrontDash = False
            notBackPlus = False
        
        if notBackDash == False or notFrontDash == False or notBackPlus == False or notFrontPlus == False:
            result = False
            print("Check start and end of each wheel key")
        return result
        
    def CheckBackOfStringIsNotDash(self, string):
        value = True;
        if string[-1] == "-":
            value = False
        return value
        
    
    def CheckFrontOfStringIsNotDash(self, string):
        value = True;
        if string[0] == "-":
            value = False
        return value
    def CheckBackOfStringIsNotPlus(self, string):
        value = True;
        if string[-1] == "+":
            value = False
        return value
        
    
    def CheckFrontOfStringIsNotPlus(self, string):
        value = True;
        
        if string == "" or string[0] == "+":
            value = False
        return value
    
    def CheckNotForInvalidCombonations(self, string):
        value = True
        
        if "--" in string:
            value = False
        
        elif "+-" in string:
            value = False
            
        elif "-+" in string:
            value = False
            
        elif "++" in string:
            value = False
            
        if value == False:
            print("Invalid combination")
        
        return value
    
    def CheckValueIsNotLargerThenMaxValueAllWheels(self,WheelHolder):
        Value = True
        
        for i in WheelHolder.Wheels:
            if Value == True:
                Value = self.CheckValueIsNotLargerThenMaxValue(i)
        
        return Value
    
    def CheckValueIsNotLargerThenMaxValue(self,Wheel):
        Value = True
        for i in Wheel.ImportedWheelKey:
            if i > self.MaxValue:
                Value = False
                print("Value is too large", i)
        return Value
    
    def CheckValueIsNotSmallerThenMinimumValueAllWheels(self,WheelHolder):
        Value = True
        for i in WheelHolder.Wheels:
            if Value == True:
                Value = self.CheckValueIsNotSmallerThenMinimumValue(i)
        
        return Value
    
    def CheckValueIsNotSmallerThenMinimumValue(self,Wheel):
        Value = True
        for i in Wheel.ImportedWheelKey:
            if i < self.MinimumValue:
                Value = False
                print("Value is too small", i)
        return Value
    
    def CheckMaximumAndMinimumValues(self, WheelHolder):
        Value = False
        ValueMinimum = self.CheckValueIsNotSmallerThenMinimumValueAllWheels(WheelHolder)
        ValueMaximum  = self.CheckValueIsNotLargerThenMaxValueAllWheels(WheelHolder)
        
        if ValueMaximum == True and ValueMinimum == True:
            Value = True
        
        return Value
        
    
    def ValidationManager(self):
        KeyValidChar = False
        KeyValidLength = False
        StartOrEndCheck = False
        InvalidCombonation = False
        MaximumAndMinimumCheck = False
        WheelHolders = []
        while MaximumAndMinimumCheck == False or StartOrEndCheck == False or KeyValidChar == False or KeyValidLength == False or KeyValidUniqueChars == False or InvalidCombonation == False:
            Key = self.ReturnKeyTryCatch()
            InvalidCombonation = self.CheckNotForInvalidCombonations(Key)
            KeyValidChar = self.CheckString(Key)
            if KeyValidChar == True and InvalidCombonation == True:
                StartOrEndCheck = self.CheckBackAndFrontOfStringAllWheels(Key)
                if StartOrEndCheck == True:
                    WheelHolders.append(WheelHolderClass.WheelHolder());
                    WheelHolders[0].ImportKey(Key)
                    KeyValidLength = self.CheckKeyLength(WheelHolders[0])
                    if KeyValidLength == True:
                        KeyValidUniqueChars = self.CheckKeyValuesAreUnique(WheelHolders[0])
                        if KeyValidUniqueChars == True:
                            MaximumAndMinimumCheck = self.CheckMaximumAndMinimumValues(WheelHolders[0])
                            
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
    
class TranspositionKeyValidation():
    
    def __init__(self):
        self.KeySetClass = CharacterSet.TranspositionCipherKeySet()
        self.List = self.KeySetClass.inputValues
        self.MaxValue = self.KeySetClass.transpositionCiphermaxId
        self.MinimumValue = self.KeySetClass.transpositionCipherminId
        self.Count = len(self.List)
        
    def ImportKey(self, Key):
        ImportedKey = Key.split("-")
        return ImportedKey
    
    def CheckString(self,Message):
        Valid = True
        MessageLength = len(Message)
        
        if MessageLength <= 0:
            Valid = False
            print("No key")
            
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
    
    def CheckKeyLength(self, Key):
        valid = True
        valueCount = len(Key)
        
        if valueCount == len(self.KeySetClass.transpositionCipherColumnId):
            valid = True
        else:
            valid = False
            print("Invalid key", valueCount, len(self.KeySetClass.transpositionCipherColumnId))
            
        return valid
    
    def CheckValuesAreUnique(self, Key):
        valid = True
        valid = len(self.KeySetClass.transpositionCipherColumnId) == len(set(Key))
        if valid == False:
            print("Invalid wheel key values are not unique")
        return valid
    
    def CheckValueIsNotSmallerThenMinimumValue(self, Key):
        Value = True
        ConvertedKey = list(map(int, Key))
        for i in ConvertedKey:
            if i < self.MinimumValue:
                Value = False
                print("Value is too small", i)
        return Value
    
    def CheckValueIsNotLargerThenMaxValue(self, Key):
        Value = True
        ConvertedKey = list(map(int, Key))
        for i in ConvertedKey:
            if i > self.MaxValue:
                Value = False
                print("Value is too large", i)
        return Value
    
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
        
    def ValidationManager(self):
        LengthCheck = False
        UniqueCheck = False
        LargestValueCheck = False
        SmallestValueCheck = False
        KeyValidChar = False
        
        
        while LengthCheck == False or UniqueCheck == False or LargestValueCheck == False or SmallestValueCheck == False:
            Key = self.ReturnKeyTryCatch()
            KeyValidChar = self.CheckString(Key)
            if KeyValidChar == True:
                ImportedKey = self.ImportKey(Key)
                LengthCheck = self.CheckKeyLength(ImportedKey)
                if LengthCheck == True:
                    UniqueCheck = self.CheckValuesAreUnique(ImportedKey)
                    if UniqueCheck == True:
                        LargestValueCheck = self.CheckValueIsNotLargerThenMaxValue(ImportedKey)
                        if LargestValueCheck == True:
                            SmallestValueCheck = self.CheckValueIsNotSmallerThenMinimumValue(ImportedKey)
        
        return Key
            
        
        
        
        
    
    
            
            
        
            
            
        
        
            
        
    
    
    