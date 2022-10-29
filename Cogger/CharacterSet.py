class EnglishStandard():
        
        versionId = "Test Set"
        
        if (versionId == "Test Set"): 
            inputValues = ['A','S','D','F']       
        if (versionId == 100): 
            numbers100 = ['0','1','2','3','4','5','6','7','8','9']
            lowerCase100 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            higherCase100 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            specialCharacters100 = ['!','"','#','$','%','&',"/","'",'(',')','*','+',',','-','.','\\',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~',' ','£']
            inputValues = numbers100 + lowerCase100 + higherCase100 + specialCharacters100
    
        inputId= []
        Counter = 0
        for i in inputValues:
            inputId.append(Counter)
            Counter = Counter + 1
        maxId = inputId[-1]
        count = len(inputId)
        minId = inputId[0]

class KeySet():
    inputValues = ['1','2','3','4','5','6','7','8','9','0',
                '+','-']