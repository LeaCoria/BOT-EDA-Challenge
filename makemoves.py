import asyncio

class Makemoves():
    def __init__ (self, requestData):
        
        self.requestDataMoves = requestData
        
    async def mover(self, requestDataMoves):
        
        print(f"\n\n ESTAMOS EN MOVER\n{requestDataMoves}")