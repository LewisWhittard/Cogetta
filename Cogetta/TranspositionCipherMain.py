import TranspositionCipherTable
import Validation

Table = TranspositionCipherTable.Table(0)
StringValidation = Validation.StringValidation()
KeyValidation = Validation.KeyValidation()
NumberValidation = Validation.NumberValidation()

print("Cogetta Transposition Cipher • © Lewis Whittard 2022 • MIT License • Version: 1.0.0")

ProgramActive = True

while ProgramActive == True:
    print("0: Genarate a key")
    print("1: Encrypt")
    print("2: Decrypt")
    print("3: Quit")

    Action = input("Please enter a Number:")

    if (Action == "0"):
        Table.GenarateKey()
        
    if (Action == "1"):
        Table.ImportWheelKey("1-0-6-2-5-4-7-3")
        string  = Table.EncryptMessage("TheQuickBrownFoxJumpsOverTheLazyDog")
        print(string)
    
    if (Action == "2"):
        Table.ImportWheelKey("1-0-6-2-5-4-7-3")
        string  = Table.Decrypt("TheQuickBrownFoxJumpsOverTheLazyDog")
        print(string)
        
    
    elif (Action == "3"):
        ProgramActive = False
    
    elif(Action != "0" or Action != "1" or Action != "2"or Action != "3"):
        print("Incorrect value please refer to the list of commands")
    