
class Horizontal_Move():
    
    def __init__(self, requestData):
        
        self.requestData = requestData

    #In this class I used the same logic of the vertical move,
    #but change it to make a horizontal move
        
    def verify_horizontal_move(self, myPeons, enPeons, peonsHorizontalMove, wallsH, wallsV):
        
        freePeonsHorizontal = []
        jumpPeonsHorizontal = []
        for peon in peonsHorizontalMove:
            if [ peon[0] , peon[1] - 1 ] in enPeons:
                jumpPeonsHorizontal.append(peon)
            else:
                freePeonsHorizontal.append(peon)
        if len(jumpPeonsHorizontal) > 0:
            return self.valid_horizontal_jump(myPeons, enPeons, jumpPeonsHorizontal, freePeonsHorizontal, wallsH, wallsV)
        else:
            return self.valid_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
    
    def valid_horizontal_jump(self, myPeons, enPeons, jumpPeonsHorizontal, freePeonsHorizontal, wallsH, wallsV):
        
        jumpPeonsHorizontalValid = []
        for peon in jumpPeonsHorizontal:
            if not( [ peon[0] - 1 , peon[1] - 1 ] in wallsV ) and not( [ peon[0] - 1 , peon[1] ] in wallsV ):
                jumpPeonsHorizontalValid.append(peon)
        if len(jumpPeonsHorizontalValid) > 0:
            for peon in jumpPeonsHorizontalValid:
                to_row = peon[0]
                to_col = peon[1] - 2
                if ( [ to_row , to_col ] in enPeons ) or ( [ to_row , to_col ] in myPeons ):
                    jumpPeonsHorizontalValid.remove(peon)
        else:
            return self.valid_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        if len(jumpPeonsHorizontalValid) > 0:
            return self.move_peon_jump(jumpPeonsHorizontalValid)
        else:
            return self.valid_horizontal_move(myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV)
        
    def valid_horizontal_move(self, myPeons, enPeons, freePeonsHorizontal, wallsH, wallsV):
        
        freePeonsHorizontalValid = []
        for peon in freePeonsHorizontal:
            if not( [ peon[0] - 1 , peon[1] - 1 ] in wallsV ) and not( [ peon[0] - 1 , peon[1] ] in wallsV ):
                freePeonsHorizontalValid.append(peon)
        if len(freePeonsHorizontalValid) > 0:
            for peon in freePeonsHorizontalValid:
                if [ peon[0] , peon[1] - 1 ] in myPeons:
                    freePeonsHorizontalValid.remove(peon)
        if len(freePeonsHorizontalValid) > 0:
            return self.move_peon_free(freePeonsHorizontalValid)
        
    def move_peon_jump(self, jumpPeonsHorizontalValid):
        
        from_row = jumpPeonsHorizontalValid[0][0]
        from_col = jumpPeonsHorizontalValid[0][1]
        to_row = from_row
        to_col = from_col - 2
        if len(jumpPeonsHorizontalValid) > 1:
            for peon in jumpPeonsHorizontalValid:
                if (from_col < peon[1]) and peon[1] > 1:
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row
                    to_col = to_col - 2
        return self.send(from_row, from_col, to_row, to_col)
    
    def move_peon_free(self, freePeonsHorizontalValid):
        
        from_row = freePeonsHorizontalValid[0][0]
        from_col = freePeonsHorizontalValid[0][1]
        to_row = from_row
        to_col = from_col - 1
        if len(freePeonsHorizontalValid) > 1:
            for peon in freePeonsHorizontalValid:
                if (from_col < peon[1]) and peon[1] > 1:
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row
                    to_col = to_col - 1
        return self.send(from_row, from_col, to_row, to_col)
                 
    def send(self, from_row, from_col, to_row, to_col):
        
        message = {
                "action" : "move",
                "data": {
                    "game_id": self.requestData["data"]["game_id"],
                    "turn_token": self.requestData["data"]["turn_token"],
                    "from_row": from_row,
                    "from_col": from_col,
                    "to_row": to_row,
                    "to_col": to_col
                }
            }
        return message