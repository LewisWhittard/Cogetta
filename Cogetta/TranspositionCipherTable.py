import TranspositionCipherColumn
import CharacterSet
from random import *


class Table():
    def __init__(self,iD):
        self.CharacterSetClass = self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.ID = iD
        self.ListOfColumns = []
        self.Key = None
        self.Column0 = TranspositionCipherColumn.Column(0)
        self.Column1 = TranspositionCipherColumn.Column(1)
        self.Column2 = TranspositionCipherColumn.Column(2)
        self.Column3 = TranspositionCipherColumn.Column(3)
        self.Column4 = TranspositionCipherColumn.Column(4)
        self.Column5 = TranspositionCipherColumn.Column(5)
        self.Column6 = TranspositionCipherColumn.Column(6)
        self.Column7 = TranspositionCipherColumn.Column(7)
        self.ListOfColumns.append(self.Column0)
        self.ListOfColumns.append(self.Column1)
        self.ListOfColumns.append(self.Column2)
        self.ListOfColumns.append(self.Column3)
        self.ListOfColumns.append(self.Column4)
        self.ListOfColumns.append(self.Column5)
        self.ListOfColumns.append(self.Column6)
        self.ListOfColumns.append(self.Column7)
        
    def importKey(key):
        Key = key
    
    def GenarateKey(self):
        Key = ""
        Counter = 0
        GenaratedKey = self.CharacterSetClass.transporationCipherColumnId.copy()
        shuffle(GenaratedKey)
        for i in GenaratedKey:
            if Counter == 7:
                Key = Key + str(i)
            else:
                Key = Key + str(i) + "-"
            Counter = Counter + 1
        self.GenaratedKey = Key
        print(Key)
            
    