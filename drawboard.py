import defending_strategy

class Drawboard():
    def __init__ (self, requestData):
        
        self.requestData = requestData

    def printBoard(self):
        
        #This function is going to print the board at the moment
        #that the event 'your_turn' is emmited, but in the same time
        #is going to make a list of 17x17 dimensions that contains the
        #information of the board. Then it's going to be used to 
        #found any objet in the board
        boardPrinter = "  0a1b2c3d4e5f6g7h8\n  -----------------\n"
        boardDisposition = self.requestData["data"]["board"]
        rows = "0a1b2c3d4e5f6g7h8"
        indexString = 0
        indexRows = 0
        indexCol = 0
        arrColumns = 17
        arrRows = 17
        arrayBoard = [ ([0]*arrColumns) for arrRows in range(arrRows) ]
        for element in boardDisposition:
            if indexString == 0:
                boardPrinter += "0|" + element
                arrayBoard [indexRows][indexCol] = element
            else :
                if ( indexString % 17) != 0:
                        boardPrinter += element
                        arrayBoard [indexRows][indexCol] = element
                else:
                    boardPrinter += "\n" + rows[indexRows+1] + "|" + element
                    indexRows += 1
                    indexCol = 0
                    arrayBoard [indexRows][indexCol] = element
            indexString += 1
            indexCol += 1
        print(boardPrinter)
        return self.detectPositions(arrayBoard)                
        
    def detectPositions(self, arrayBoard):
        
        #After read the board i'm going to make a 2 dimensions list
        #with the positions of my peons and another for my enemie's
        #peons' position on the board. So its gonna be lists of 3x2.
        myPeons = []
        enPeons = []
        wallsH = []
        wallsV = []
        mySide = self.requestData["data"]["side"]
        if mySide == "N":
            enSide = "S"
        else:
            enSide = "N"
        indexRows = 0
        indexColumns = 0
        for arrRows in arrayBoard:
            for arrColumns in arrayBoard:
                if arrayBoard[indexRows][indexColumns] == mySide:
                    myPeons.append( [ int(indexRows/2) , int(indexColumns/2) ] )
                if ( arrayBoard[indexRows][indexColumns] == enSide ):
                    enPeons.append( [ int(indexRows/2) , int(indexColumns/2) ] )
                if indexColumns < 16 :
                    if ( arrayBoard[indexRows][indexColumns] == "-" and arrayBoard[indexRows][indexColumns+1] == "*" and arrayBoard[indexRows][indexColumns+2] == "-"):
                        wallsH.append( [ int(indexRows/2) , int(indexColumns/2) ] )
                if indexRows < 8:
                    if ( arrayBoard[indexRows][indexColumns] == "|" and arrayBoard[indexRows+1][indexColumns] == "*" and arrayBoard[indexRows+2][indexColumns] == "|"):
                        wallsV.append( [ int(indexRows/2) , int(indexColumns/2) ] )
                indexColumns += 1
            indexRows += 1
            indexColumns = 0
        return self.find_move(myPeons, enPeons, wallsH, wallsV)
    
        
    def find_move(self, myPeons, enPeons, wallsH, wallsV):

        #With the information in list myPeons i'm going to determinate
        #the peon to move and the move itself
        strategyPlay = defending_strategy.Defending_Strategy(self.requestData)
        return strategyPlay.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
