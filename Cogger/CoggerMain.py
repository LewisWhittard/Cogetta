import WheelHolderClass
import Validation

WheelHolders = []
StringValidation = Validation.StringValidation()
KeyValidation = Validation.KeyValidation()
NumberValidation = Validation.NumberValidation()

print("Cogger • © Lewis Whittard 2022 • MIT License")

ProgramActive = True

while ProgramActive == True:
    print("0: Genarate a key")
    print("1: Encrypt")
    print("2: Decrypt")
    print("3: Quit")

    Action = input("Please enter a Number:")

    if (Action == "0"):
        WheelHolders.clear()
        WheelHolders.append(WheelHolderClass.WheelHolder())
        Number = NumberValidation.ReturnKeyTryCatch()
        WheelHolders[0].GenarateKey(Number)
        WheelHolders.clear()
   
    elif (Action == "1"):
        WheelHolders.clear()
        Key = KeyValidation.ValidationManager()
        WheelHolders.append(WheelHolderClass.WheelHolder())
        WheelHolders[0].ImportKey(Key)
        StringValid = False
        Message = StringValidation.ValidationManager()
        WheelHolders[0].EncryptMessage(Message)
        WheelHolders.clear()

    elif (Action == "2"):
        WheelHolders.clear()
        WheelHolders.append(WheelHolderClass.WheelHolder())
        Key = KeyValidation.ValidationManager()
        WheelHolders[0].ImportKey(Key)
        Message = StringValidation.ValidationManager()
        WheelHolders[0].DecryptMessage(Message)
        WheelHolders.clear()
    
    elif (Action == "3"):
        ProgramActive = False
    
    elif(Action != "0" or Action != "1" or Action != "2"or Action != "3"):
        print("Incorrect value please refer to the list of commands")
    