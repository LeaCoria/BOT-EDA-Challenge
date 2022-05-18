from requests import request


class Strategy():
    def __init__ (self, requestData):
        
        self.requestData = requestData
    
    def main_strategy (self, myPeons, enPeons, arrayBoard):
        if self.requestData["data"]["side"] == "N":
            return self.north_strategy(myPeons, enPeons, arrayBoard)
        else:
            return self.south_strategy(myPeons, enPeons, arrayBoard)
        
    def north_strategy(self, myPeons, enPeons, arrayBoard):
        for peons in myPeons:
            if ( ( peons[0] + 1 == enPeons[0][1] ) or ( peons[0] + 1 == enPeons[1][1] ) or ( peons[0] + 1 == enPeons[2][1] ) ):
                myPeons.remove(peons)
        closeRow = myPeons[0][0]
        for peons in myPeons:
            if closeRow < peons[0]:
                closeRow = peons[0]
                from_row = peons[0]
                from_col = peons[1]
                to_row = peons[0] + 1
                to_col = peons[1]
        
                
    
    def soyth_strategy(self, myPeons, enPeons, arrayBoard):
        print("hola")