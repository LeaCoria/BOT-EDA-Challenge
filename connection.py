from unittest import result
import websockets
import time
import json
import asyncio
import drawboard

class Connection():
    def __init__(self,token):
        
            self.uri = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={token}"
            self.user_list = list()
            
    async def start(self):
        
        while True:
            try:
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
                    print(f"\n\n {requestData}")
                    print(requestData["data"]["board"])
                    drawBoard = drawboard.Drawboard(requestData)
                    result = drawBoard.printBoard()
                    await self.send(
                        websocket,
                        "move",
                        {
                            "game_id": requestData["data"]["game_id"],
                            "turn_token": requestData["data"]["turn_token"],
                            "from_row": result["from_row"], 
                            "from_col": result["from_col"], 
                            "to_row": result["to_row"], 
                            "to_col": result["to_col"], 
                        }
                    )
            except KeyboardInterrupt:
                print("Exiting...")
                break
            except Exception as e:
                print("error {}".format(str(e)))
                break
    
    async def send (self,websocket,action,data):
        
        message = json.dumps(
            {
                "action" : action,
                "data": data,
            }
        )
        print(f"\n\n{message}")
        await websocket.send(message)