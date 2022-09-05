import WheelHolderClass
import Validation

WheelHolders = []
StringValidation = Validation.StringValidation()
KeyValidation = Validation.KeyValidation()


print("0: Genarate a key");
print("1: Encrypt");
print("2: Decrypt");
print("3: Quit");

Action = input("Please enter a Number:")

if (Action == "0"):
    WheelHolders.clear()
    WheelHolders.append(WheelHolderClass.WheelHolder());
    Number = int(input("How many wheels:"))
    WheelHolders[0].GenarateKey(Number)
    WheelHolders.clear()
   
if (Action == "1"):
    WheelHolders.clear()
    KeyValidChar = False
    KeyValidLength = False
    DashNotStartOrEnd = False
    NotMaxString = False
    while NotMaxString == False or DashNotStartOrEnd == False or KeyValidChar == False or KeyValidLength == False or KeyValidUniqueChars == False:
        try:
            Key = input("What is your key:")
            NotMaxString = True
        except:
            print("Key Error")
        if NotMaxString == True:
            KeyValidChar = KeyValidation.CheckString(Key)
            print("Char Pass",KeyValidChar)
            if KeyValidChar == True:
                DashNotStartOrEnd = KeyValidation.CheckBackAndFrontOfStringNotDash(Key)
                if DashNotStartOrEnd == True:
                    WheelHolders.append(WheelHolderClass.WheelHolder());
                    WheelHolders[0].ImportKey(Key)
                    KeyValidLength = KeyValidation.CheckKeyLength(WheelHolders[0])
                    WheelHolders.clear()
                    print("KeyValidLength", KeyValidLength)
                    if KeyValidLength == True:
                        WheelHolders.append(WheelHolderClass.WheelHolder());
                        WheelHolders[0].ImportKey(Key)
                        KeyValidUniqueChars = KeyValidation.CheckKeyValuesAreUnique(WheelHolders[0])
                        print("KeyValidUniqueChars", KeyValidUniqueChars)
                        WheelHolders.clear()
    WheelHolders.append(WheelHolderClass.WheelHolder());
    WheelHolders[0].ImportKey(Key)
    StringValid = False
    while StringValid == False:
        Message = input("Enter your encrypted message:")
        StringValid = StringValidation.CheckString(Message)
    WheelHolders[0].EncryptMessage(Message)
    WheelHolders.clear()

if (Action == "2"):
    WheelHolders.clear()
    WheelHolders.append(WheelHolderClass.WheelHolder());
    Key = input("What is your key:")
    WheelHolders[0].ImportKey(Key)
    Message = input("Enter your encrypted message:")
    WheelHolders[0].DecryptMessage(Message)
    WheelHolders.clear()