import asyncio
from random import randint
import json

from requests import request

class Makemove():
    def __init__ (self, requestData):
        
        self.requestData = requestData

    def printBoard(self):
        
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
        
    def detectPositions(self, arrBoard):
        
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
        for arrRows in arrBoard:
            for arrColumns in arrBoard:
                if arrBoard[indexRows][indexColumns] == self.requestData["data"]["side"]:
                    myPeons [myOrder][0] = int(indexRows/2)
                    myPeons [myOrder][1] = int(indexColumns/2)
                    myOrder += 1
                if ( arrBoard[indexRows][indexColumns] != self.requestData["data"]["side"] and arrBoard[indexRows][indexColumns] != " " ):
                    enPeons [enOrder][0] = int(indexRows/2)
                    enPeons [enOrder][1] = int(indexColumns/2)
                    enOrder += 1
                indexColumns += 1
            indexRows += 1
            indexColumns = 0
        return self.move(myPeons, enPeons)
    
        
    def move(self, myPeons, enPeons):

        choosePeon = randint(0,2)
        from_row = myPeons[choosePeon][0]
        from_col = myPeons[choosePeon][1]
        to_col = myPeons[choosePeon][1]
        if ( self.requestData["data"]["side"] == "N" ):
            to_row = myPeons[choosePeon][0] + 1
        else:
            to_row = myPeons[choosePeon][0] - 1
        return {
            "from_row": from_row,
            "from_col": from_col,
            "to_row": to_row,
            "to_col": to_col
        }