import websockets
import time
import json
import asyncio
import makemoves

class Connection():
    def __init__(self,token):
        
            self.uri = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={token}"
            self.user_list = list()
            
    async def start(self):
        
        while True:
            try:
                #print(f"\n\nConnection to \n\n{self.uri}\n\n")
                async with websockets.connect(self.uri) as websocket:
                    await self.play(websocket)
            except Exception:
                print("Connection error!")
                time.sleep(3)
                
    async def play(self, websocket):
    
        while True:
            try:
                request = await websocket.recv()
                print(f"{request}")
                requestData = json.loads(request)
                if requestData["event"] == "update_user_list":
                    self.user_list = requestData["data"]["users"]
                    print(f"\n\nUpdated user_list: \n{self.user_list}")
                if requestData["event"] == "challenge":
                    if requestData["data"]["opponent"] == "leandrocoria19@gmail.com":
                        await self.send(
                                websocket,
                                "accept_challenge",
                                {
                                    "challenge_id": requestData["data"]["challenge_id"],
                                }
                                )
                if requestData["event"] == "your_turn":
                    makeMoves = makemoves.Makemoves(requestData)
                    await makeMoves.mover()
            except Exception:
                print(f"Error {Exception}")
                break
    
    async def send (self,websocket,action,data):
        
        message = json.dumps(
            {
                'action' : action,
                'data': data,
            }
        )
        print(message)
        await websocket.send(message)