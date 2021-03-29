import WheelHolderClass

WheelHolders = []


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
    pause
   
if (Action == "1"):
    WheelHolders.clear()
    WheelHolders.append(WheelHolderClass.WheelHolder());
    Key = input("What is your key:")
    WheelHolders[0].ImportKey(Key)
    Message = input("Enter your encrypted message:")
    WheelHolders[0].EncryptMessageVersion2(Message)
    WheelHolders.clear()
    pause

if (Action == "2"):
    WheelHolders.clear()
    WheelHolders.append(WheelHolderClass.WheelHolder());
    Key = input("What is your key:")
    WheelHolders[0].ImportKey(Key)
    Message = input("Enter your encrypted message:")
    WheelHolders[0].DecryptMessageVersion2(Message)
    WheelHolders.clear()
    pause