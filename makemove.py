import asyncio

class Makemove():
    def __init__ (self, requestData):
        
        self.requestDataMoves = requestData
        
    async def mover(self, requestDataMoves):
        
        await self.printBoard
    
    async def printBoard(self):
        
        boardPrinter = "  0a1b2c3d4e5f6g7h8\n  -----------------\n"
        boardDisposition = self.requestDataMoves["data"]["board"]
        rows = "0a1b2c3d4e5f6g7h8"
        i=0
        j=0
        for element in boardDisposition:
            if i == 0:
                boardPrinter += "0|" + element
            else :
                if ( i % 17) != 0:
                        boardPrinter += element
                else:
                    boardPrinter += "\n" + rows[j] + "|" + element
                    j += 1
            i += 1
        print(boardPrinter)