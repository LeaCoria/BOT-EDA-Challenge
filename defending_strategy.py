import move_strategy

class Defending_Strategy():
    def __init__ (self, requestData):
        
        self.requestData = requestData
    
    def main_defending_strategy (self, myPeons, enPeons, wallsH, wallsV):

        turn_counter = 101 - int( ( self.requestData["data"]["remaining_moves"] + 1 ) / 2 )
        MovePlay = move_strategy.Move_Strategy(self.requestData)
        
        #The first nine moves i'm going to make a defense barrier in
        #my side. Here I wrote the indications to make it. Also there
        #is the verifications of the currents walls that may be in the
        #place that i want. In that case i skip the wall indication
        #to a move indication.
        
        if ( (turn_counter == 1) or ( (turn_counter-1) % 20 == 0 ) ):
            if not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 0 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 1 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 0 ] in wallsV ):
                return self.send( (0 if self.requestData["data"]["side"] == "N" else 7), 0, "h")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 2) or ( (turn_counter-2) % 20 == 0 ):
            if not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 2 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 1 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 3 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 2 ] in wallsV ):
                return self.send( (0 if self.requestData["data"]["side"] == "N" else 7), 2, "h")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 3) or ( (turn_counter-3) % 20 == 0 ):
            if not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 4 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 3 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 5 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 4 ] in wallsV ):
                return self.send( (0 if self.requestData["data"]["side"] == "N" else 7), 4, "h")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 4) or ( (turn_counter-4) % 20 == 0 ):
            if not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 6 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 5 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 7 ] in wallsH ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 6 ] in wallsV ):
                return self.send( (0 if self.requestData["data"]["side"] == "N" else 7), 6, "h")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 5) or ( (turn_counter-5) % 20 == 0 ):
            if not( [ ( 1 if self.requestData["data"]["side"] == "N" else 6 ) , 7 ] in wallsV ) and not( [ ( 0 if self.requestData["data"]["side"] == "N" else 7 ) , 7 ] in wallsV ) and not( [ ( 2 if self.requestData["data"]["side"] == "N" else 5 ) , 7 ] in wallsV ) and not( [ ( 1 if self.requestData["data"]["side"] == "N" else 7 ) , 7 ] in wallsH ):
                return self.send( (1 if self.requestData["data"]["side"] == "N" else 6), 7, "v")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 6) or ( (turn_counter-6) % 20 == 0 ):
            if not( [ ( 3 if self.requestData["data"]["side"] == "N" else 4 ) , 7 ] in wallsV ) and not( [ ( 2 if self.requestData["data"]["side"] == "N" else 3 ) , 7 ] in wallsV ) and not( [ ( 5 if self.requestData["data"]["side"] == "N" else 5 ) , 7 ] in wallsV ) and not( [ ( 3 if self.requestData["data"]["side"] == "N" else 4 ) , 7 ] in wallsH ):
                return self.send( (3 if self.requestData["data"]["side"] == "N" else 4), 7, "v")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 7) or ( (turn_counter-7) % 20 == 0 ):
            if not( [ ( 5 if self.requestData["data"]["side"] == "N" else 2 ) , 7 ] in wallsV ) and not( [ ( 4 if self.requestData["data"]["side"] == "N" else 1 ) , 7 ] in wallsV ) and not( [ ( 6 if self.requestData["data"]["side"] == "N" else 3 ) , 7 ] in wallsV ) and not( [ ( 6 if self.requestData["data"]["side"] == "N" else 3 ) , 7 ] in wallsH ):
                return self.send( (5 if self.requestData["data"]["side"] == "N" else 2), 7, "v")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 8) or ( (turn_counter-8) % 20 == 0 ):
            if not( [ ( 7 if self.requestData["data"]["side"] == "N" else 0 ) , 6 ] in wallsV ) and not( [ ( 6 if self.requestData["data"]["side"] == "N" else 1 ) , 6 ] in wallsV ) and not( [ ( 7 if self.requestData["data"]["side"] == "N" else 1 ) , 6 ] in wallsH ):
                return self.send( (7 if self.requestData["data"]["side"] == "N" else 0), 6, "v")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        elif (turn_counter == 9) or ( (turn_counter-9) % 20 == 0 ):
            if not( [ ( 5 if self.requestData["data"]["side"] == "N" else 2 ) , 6 ] in wallsV ) and not( [ ( 4 if self.requestData["data"]["side"] == "N" else 1 ) , 6 ] in wallsV ) and not( [ ( 6 if self.requestData["data"]["side"] == "N" else 3 ) , 6 ] in wallsV ) and not( [ ( 6 if self.requestData["data"]["side"] == "N" else 3 ) , 6 ] in wallsH ):
                return self.send( (5 if self.requestData["data"]["side"] == "N" else 2), 6, "v")
            else:
                return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
        
        else:
            return MovePlay.main_move_strategy(myPeons, enPeons, wallsH, wallsV)
    
    def send(self, row, col, orientation):
        
        message = {
                "action" : "wall",
                "data": {
                    "game_id": self.requestData["data"]["game_id"],
                    "turn_token": self.requestData["data"]["turn_token"],
                    "row": row,
                    "col": col,
                    "orientation": orientation
                }
            }
        return message