from importlib.metadata import SelectableGroups
import re
import websocket
import time
import json
import asyncio

class Connection():
    def __init__(self,token):
        
            self.uri = f"wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token=~{token}"
            self.user_list = list()
            
    async def start(self):
        
        while True:
            try:
                print(f"Connection to {self.uri}")
                async with websocket.connect(self.uri) as websocket:
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
                if requestData['event'] == 'update_user_list':
                    self.user_list = requestData['data']['users']
                    print(f"Updated user_list: {self.user_list}")
            except Exception:
                print(f"Error {Exception}")
                break
                