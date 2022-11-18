import TranspositionCipherColumn

class Table():
    def __init__(self,iD):
        ID = iD
        ListOfColumns = []
        Key = None
        Column0 = TranspositionCipherColumn.Column(0)
        Column1 = TranspositionCipherColumn.Column(1)
        Column2 = TranspositionCipherColumn.Column(2)
        Column3 = TranspositionCipherColumn.Column(3)
        Column4 = TranspositionCipherColumn.Column(4)
        Column5 = TranspositionCipherColumn.Column(5)
        Column6 = TranspositionCipherColumn.Column(6)
        Column7 = TranspositionCipherColumn.Column(7)
        ListOfColumns.Add(Column0)
        ListOfColumns.Add(Column1)
        ListOfColumns.Add(Column2)
        ListOfColumns.Add(Column3)
        ListOfColumns.Add(Column4)
        ListOfColumns.Add(Column5)
        ListOfColumns.Add(Column6)
        ListOfColumns.Add(Column7)
        
    def importKey(key):
        Key = key
    
    def GenarateKey():
        Return None
            
    