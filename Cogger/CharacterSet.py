class EnglishStandard():
        inputValues = ['1','2','3','4','5','6','7','8','9','0',
                'q','w','e','r','t','y','u','i','o','p',
                'a','s','d','f','g','h','j','k','l',
                'z','x','c','v','b','n','m',
                'Q','W','E','R','T','Y','U','I','O','P',
                'A','S','D','F','G','H','J','K','L',
                'Z','X','C','V','B','N','M',
                '|','`','¬','!','"','£','$','%','^','&','*','(',')','-','+',
                '[','{','}',']',';',':','@','\'','#','~','\\','<',',','.','?','/',' ','_','=']
    
        inputId= []
        Counter = 0
        for i in inputValues:
            inputId.append(Counter)
            Counter = Counter + 1
        maxId = inputId[-1]
        count = len(inputId)
        
        
        
            
            
                
                
        
class DemoSet():
        inputValues = ['A','S','D','F']
        inputId=[0,1,2,3]
        maxId = inputId[-1]
        
class KeySet():
    inputValues = ['1','2','3','4','5','6','7','8','9','0',
                '+','-']