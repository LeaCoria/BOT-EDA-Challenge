import unittest
import move_strategy


class TestDefendigStrategy(unittest.TestCase):

    
    def test_main_move_strategy(self):
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,1],[0,4],[0,7]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = [[0,0],[0,2],[0,4],[0,6]]
        wallsV = [[1,7],[3,7],[5,7],[7,6],[5,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,7,0,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,1],[0,4],[0,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,4,0,5,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,1],[0,7],[0,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,1,0,2,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,6],[0,7],[1,8]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = [[0,0],[0,2],[0,4],[0,6]]
        wallsV = [[1,7],[3,7],[5,7],[7,6],[5,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,7,0,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,6],[0,8],[1,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,6,0,7,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        myPeons = [[8,5],[8,7],[8,8]]
        enPeons = [[0,1],[0,4],[0,7]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,6],[2,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(8,5,8,6,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[7,8],[8,7],[8,6]]
        enPeons = [[7,1],[0,4],[0,7]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,7],[2,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(8,7,8,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[8,6],[8,8],[7,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(8,6,8,7,requestData)
        self.assertEqual( result, messageToSend )
        
    
    def test_verify_peons_vertical(self):
        
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,6],[0,7],[0,8]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = [[0,0],[0,2],[0,4],[0,6]]
        wallsV = [[1,7],[3,7],[5,7],[7,6],[5,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,8,1,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,6],[0,7],[0,8]]
        enPeons = [[8,1],[8,4],[1,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(0,8,2,8,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        myPeons = [[8,6],[8,7],[8,8]]
        enPeons = [[0,6],[0,7],[0,8]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,6],[2,6]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(8,8,7,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[8,6],[8,7],[8,8]]
        enPeons = [[0,6],[0,7],[7,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
        messageToSend = self.send(8,8,6,8,requestData)
        self.assertEqual( result, messageToSend )
        
        
    def test_valid_vertical_jump(self):
        
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,7],[0,8],[4,8]]
        enPeons = [[8,1],[8,4],[1,7]]
        wallsH = [[0,0],[0,2],[0,4],[0,6]]
        wallsV = [[1,7],[3,7],[5,7],[7,6],[5,6]]
        jumpPeonsVertical = [[0,7]]
        freePeonsVertical = [[4,8],[0,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_jump(myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH)
        messageToSend = self.send(4,8,5,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[5,8]]
        enPeons = [[8,1],[8,4],[6,8]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,7],[2,6]]
        jumpPeonsVertical = [[5,8]]
        freePeonsVertical = [[0,8],[0,7]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_jump(myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH)
        messageToSend = self.send(5,8,7,8,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        myPeons = [[8,7],[8,8],[5,8]]
        enPeons = [[0,1],[0,4],[4,8]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,6],[2,6]]
        jumpPeonsVertical = [[5,8]]
        freePeonsVertical = [[8,8],[8,7]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_jump(myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH)
        messageToSend = self.send(5,8,3,8,requestData)
        self.assertEqual( result, messageToSend )
        
    def test_valid_vertical_move(self):
        
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,6],[0,7],[0,8]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = [[0,0],[0,2],[0,4],[0,6]]
        wallsV = [[1,7],[3,7],[5,7],[7,6],[5,6]]
        freePeonsVertical = [[0,6],[0,7],[0,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH)
        messageToSend = self.send(0,8,1,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[1,8]]
        freePeonsVertical = [[0,7],[0,8],[1,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH)
        messageToSend = self.send(1,8,2,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[0,7],[0,8],[2,8]]
        freePeonsVertical = [[0,7],[0,8],[2,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH)
        messageToSend = self.send(2,8,3,8,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        myPeons = [[8,7],[8,8],[7,8]]
        myPeons = [[0,6],[0,7],[0,8]]
        wallsH = [[7,0],[7,2],[7,4],[7,6]]
        wallsV = [[6,7],[4,7],[2,7],[0,6],[2,6]]
        freePeonsVertical = [[8,7],[8,8],[7,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH)
        messageToSend = self.send(7,8,6,8,requestData)
        self.assertEqual( result, messageToSend )
        
        myPeons = [[8,7],[8,8],[6,8]]
        freePeons = [[6,8],[8,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.valid_vertical_move(myPeons, enPeons, freePeons, wallsH)
        messageToSend = self.send(6,8,5,8,requestData)
        self.assertEqual( result, messageToSend )
        
    def test_move_peon_jump(self):
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        jumpPeonsVerticalValid = [[0,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_jump(jumpPeonsVerticalValid)
        messageToSend = self.send(0,8,2,8,requestData)
        self.assertEqual( result, messageToSend )
        
        jumpPeonsVerticalValid = [[0,8],[5,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_jump(jumpPeonsVerticalValid)
        messageToSend = self.send(5,8,7,8,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        jumpPeonsVerticalValid = [[8,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_jump(jumpPeonsVerticalValid)
        messageToSend = self.send(8,8,6,8,requestData)
        self.assertEqual( result, messageToSend )

        jumpPeonsVerticalValid = [[5,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_jump(jumpPeonsVerticalValid)
        messageToSend = self.send(5,8,3,8,requestData)
        self.assertEqual( result, messageToSend )
        
        jumpPeonsVerticalValid = [[5,8],[3,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_jump(jumpPeonsVerticalValid)
        messageToSend = self.send(3,8,1,8,requestData)
        self.assertEqual( result, messageToSend )
        
    def test_move_peon_free(self):
        
        requestData = {
            "data": {
                "side": "N",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        freePeonsVerticalValid = [[0,8],[2,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_free(freePeonsVerticalValid)
        messageToSend = self.send(2,8,3,8,requestData)
        self.assertEqual( result, messageToSend )
        
        freePeonsVerticalValid = [[0,8],[7,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_free(freePeonsVerticalValid)
        messageToSend = self.send(7,8,8,8,requestData)
        self.assertEqual( result, messageToSend )
        
        requestData["data"]["side"] = "S"
        freePeonsVerticalValid = [[1,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_free(freePeonsVerticalValid)
        messageToSend = self.send(1,8,0,8,requestData)
        self.assertEqual( result, messageToSend )
        
        freePeonsVerticalValid = [[1,8],[3,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_free(freePeonsVerticalValid)
        messageToSend = self.send(1,8,0,8,requestData)
        self.assertEqual( result, messageToSend )
        
        freePeonsVerticalValid = [[3,8],[5,8]]
        result = move_strategy.Move_Strategy(requestData)
        result = result.move_peon_free(freePeonsVerticalValid)
        messageToSend = self.send(3,8,2,8,requestData)
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