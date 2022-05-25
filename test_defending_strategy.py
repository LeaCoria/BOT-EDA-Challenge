import unittest
import defending_strategy


class TestDefendigStrategy(unittest.TestCase):

    
    def test_main_strategy(self):
        
        requestData = {
            "data": {
                "side": "N",
                "remaining_moves": 200.0,
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,1],[0,4],[0,7]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = []
        wallsV = []
        result = defending_strategy.Defending_Strategy(requestData)
        result = result.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,0,"h",requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["remaining_moves"] = 197.0
        requestData["data"]["side"] = "S"
        result = defending_strategy.Defending_Strategy(requestData)
        result = result.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(7,2,"h",requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["remaining_moves"] = 120.0
        result = defending_strategy.Defending_Strategy(requestData)
        result = result.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(7,0,"h",requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["remaining_moves"] = 30.0
        requestData["data"]["side"] = "N"
        result = defending_strategy.Defending_Strategy(requestData)
        result = result.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(3,7,"v",requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["remaining_moves"] = 73.0
        result = defending_strategy.Defending_Strategy(requestData)
        result = result.main_defending_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,6,"h",requestData)
        self.assertEqual( result, messageToSend )

    def send (self, row, col, orientation, requestData):
        
        message = {
                "action" : "wall",
                "data": {
                    "game_id": requestData["data"]["game_id"],
                    "turn_token": requestData["data"]["turn_token"],
                    "row": row,
                    "col": col,
                    "orientation": orientation
                }
            }
        return message
        
if __name__  == '__main__':
    unittest.main()