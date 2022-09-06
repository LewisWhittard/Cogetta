import WheelHolderClass
import Validation

WheelHolders = []
StringValidation = Validation.StringValidation()
KeyValidation = Validation.KeyValidation()
NumberValidation = Validation.NumberValidation()
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
   
    if (Action == "1"):
        WheelHolders.clear()
        Key = KeyValidation.ValidationManager()
        WheelHolders.append(WheelHolderClass.WheelHolder())
        WheelHolders[0].ImportKey(Key)
        StringValid = False
        Message = StringValidation.ValidationManager()
        WheelHolders[0].EncryptMessage(Message)
        WheelHolders.clear()

    if (Action == "2"):
        WheelHolders.clear()
        WheelHolders.append(WheelHolderClass.WheelHolder())
        Key = KeyValidation.ValidationManager()
        WheelHolders[0].ImportKey(Key)
        Message = StringValidation.ValidationManager()
        WheelHolders[0].DecryptMessage(Message)
        WheelHolders.clear()
    
    if (Action == "3"):
        ProgramActive = False
        
    else:
        print("Incorrect Value")
    