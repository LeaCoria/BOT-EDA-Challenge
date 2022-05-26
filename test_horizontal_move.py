import unittest
import horizontal_move


class TestDefendigStrategy(unittest.TestCase):
    
    def test_horizontal_move(self):
        
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        '''myPeons = [[3,8],[2,8],[1,8]]
        enPeons = [[1,0],[1,1],[1,2]]
        wallsH = [[0,0],[0,2],[0,4],[0,6],[3,7]]
        wallsV = [[1,7],[5,7],[7,6],[5,6]]
        freePeonsHorizontal = [[3,8]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,8,3,7,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[3,8],[2,8],[1,8]]
        enPeons = [[1,0],[1,1],[3,7]]
        freePeonsHorizontal = [[3,8]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,8,3,6,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[3,7],[3,8],[1,8]]
        enPeons = [[1,0],[1,1],[3,7]]
        freePeonsHorizontal = [[3,7]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,7,3,6,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[3,8]]
        enPeons = [[8,0],[8,1],[3,6]]
        wallsH = [[0,0],[0,2],[0,4],[0,6],[3,7]]
        wallsV = [[1,7],[5,7],[7,6],[5,6],[3,5]]
        freePeonsHorizontal = [[3,8]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,8,3,7,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[3,7]]
        enPeons = [[8,0],[8,1],[3,6]]
        wallsH = [[0,0],[0,2],[0,4],[0,6],[3,7]]
        wallsV = [[1,7],[5,7],[7,6],[5,6],[3,5]]
        freePeonsHorizontal = [[3,7]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,7,4,6,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[3,7]]
        enPeons = [[8,0],[8,1],[3,6]]
        wallsH = [[0,0],[0,2],[0,4],[0,6],[3,7]]
        wallsV = [[1,7],[5,7],[7,6],[5,6],[2,5]]
        freePeonsHorizontal = [[3,7]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,7,4,6,requestData)
        self.assertEqual( result, messageToSend )'''
        
        myPeons = [[0,7],[0,8],[3,7]]
        enPeons = [[8,0],[8,1],[3,6]]
        wallsH = [[0,0],[0,2],[0,4],[0,6],[3,7],[3,5]]
        wallsV = [[1,7],[5,7],[7,6],[5,6],[2,5]]
        freePeonsHorizontal = [[3,7]]
        result = horizontal_move.Horizontal_Move(requestData)
        result = result.verify_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        messageToSend = self.send(3,7,2,6,requestData)
        self.assertEqual( result, messageToSend )
        
    def send(self, from_row, from_col, to_row, to_col, requestData):
            
        message = {
                "action" : "move",
                "data": {
                    "game_id": requestData["data"]["game_id"],
                    "turn_token": requestData["data"]["turn_token"],
                    "from_row": from_row,
                    "from_col": from_col,
                    "to_row": to_row,
                    "to_col": to_col
                }
            }
        return message
    
if __name__  == '__main__':
    unittest.main()