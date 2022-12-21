import TranspositionCipherTable
import Validation

TableList = []
StringValidation = Validation.StringValidation()
KeyValidation = Validation.KeyValidation()
NumberValidation = Validation.NumberValidation()
TranspositionCipherKeyValidation = Validation.TranspositionKeyValidation()

print("Cogetta • Transposition Cipher • © Lewis Whittard 2022 • MIT License • Version: 1.1.0")

ProgramActive = True

while ProgramActive == True:
    print("0: Genarate a key")
    print("1: Encrypt")
    print("2: Decrypt")
    print("3: Quit")

    Action = input("Please enter a Number:")

    if (Action == "0"):
        Table.GenarateKey()
        
    elif (Action == "1"):
        TableList.clear()
        TableList.append(TranspositionCipherTable.Table(0))
        Key = TranspositionCipherKeyValidation.ValidationManager()
        TableList[0].ImportWheelKey(Key)
        string  = TableList[0].EncryptMessage("TheQuickBrownFoxJumpsOverTheLazyDog")
        print(string)
        TableList.clear()
    
    elif (Action == "2"):
        TableList.clear()
        TableList.append(TranspositionCipherTable.Table(0))
        TableList[0].ImportWheelKey("1-0-3-2-5-4-7-6")
        string  = TableList[0].Decrypt("hruToTBJrDQwpeeomhgiFOaunsLkxeycovz")
        print(string)
        TableList.clear()
        
    
    elif (Action == "3"):
        ProgramActive = False
    
    elif(Action != "0" or Action != "1" or Action != "2"or Action != "3"):
        print("Incorrect value please refer to the list of commands")
    