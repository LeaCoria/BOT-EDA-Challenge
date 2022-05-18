import asyncio
from random import randint
import json

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
                    boardPrinter += "\n" + rows[indexRows] + "|" + element
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
        cantPeons = 3
        coords = 2
        myPeons = [ ([0]*coords) for cantPeons in range(cantPeons) ]
        enPeons = [ ([0]*coords) for cantPeons in range(cantPeons) ]
        indexRows = 0
        indexColumns = 0
        myOrder = 0
        enOrder = 0
        for arrRows in arrayBoard:
            for arrColumns in arrayBoard:
                if arrayBoard[indexRows][indexColumns] == self.requestData["data"]["side"]:
                    myPeons [myOrder][0] = int(indexRows/2)
                    myPeons [myOrder][1] = int(indexColumns/2)
                    myOrder += 1
                if ( arrayBoard[indexRows][indexColumns] != self.requestData["data"]["side"] and arrayBoard[indexRows][indexColumns] != " " ):
                    enPeons [enOrder][0] = int(indexRows/2)
                    enPeons [enOrder][1] = int(indexColumns/2)
                    enOrder += 1
                indexColumns += 1
            indexRows += 1
            indexColumns = 0
        return self.find_move(myPeons, enPeons, arrayBoard)
    
        
    def find_move(self, myPeons, enPeons, arrayBoard):

        #With the information in list myPeons i'm going to determinate
        #the peon to move and the move itself
        strategy = strategy.Strategy(self.requestData)
        return strategy.main_strategy(myPeons, enPeons, arrayBoard)
