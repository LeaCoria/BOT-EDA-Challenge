import unittest
import drawboard

class TestDrawBoard(unittest.TestCase):

    
    def test_print_board(self):
        
        requestData = {
            "event": "your_turn",
            "data": {
                "player_2": "uno",
                "player_1": "dos",
                "score_2": 0.0,
                "walls": 10.0,
                "score_1": 0.0,
                "side": "N",
                "remaining_moves": 200.0,
                "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ",
                "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
            }
            }
        myPeons = [[0,1],[0,4],[0,7]]
        enPeons = [[8,1],[8,4],[8,7]]
        wallsH = []
        wallsV = []
        arrayBoard = [[' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ']]
        resultado = drawboard.Drawboard(requestData)
        result = resultado.main_defending_strategy(myPeons, enPeons, wallsH, wallsV, arrayBoard)
        msg = {
            "action": "wall",
            "data": {
                "game_id": requestData["data"]["game_id"],
                "turn_token": requestData["data"]["turn_token"],
                "row": (0 if requestData["data"]["side"] == "N" else 7),
                "col": 0,
                "orientation": "h"
            }
            }
        self.assertEqual( result, msg )
        
        
if __name__  == '__main__':
    unittest.main()