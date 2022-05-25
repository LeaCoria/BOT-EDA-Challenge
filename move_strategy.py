import horizontal_move

class Move_Strategy():
    
    def __init__ (self, requestData):
        
        self.requestData = requestData
    
    def main_move_strategy (self, myPeons, enPeons, wallsH, wallsV):
        
        if self.requestData["data"]["side"] == "N":
            cont = 0
            if ( [0,6] in myPeons ) and ( [0,7] in myPeons ) and ( [0,8] in myPeons ):
                return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            elif ( [0,7] in myPeons ) and ( [0,8] in myPeons ) and ( [1,8] in myPeons ):
                return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            elif ( [0,7] in myPeons ) and ( [0,8] in myPeons ):
                for peon in myPeons:
                    if peon[0] > 0:
                        return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
                    else:
                        cont += 1
                if cont == 3:
                    return self.move_lateral(myPeons)
            else:
                return self.move_lateral(myPeons)
        else:
            cont = 0
            if ( [8,6] in myPeons ) and ( [8,7] in myPeons ) and ( [8,8] in myPeons ):
                return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            elif ( [8,7] in myPeons ) and ( [8,8] in myPeons ) and ( [7,8] in myPeons ):
                return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            elif ( [8,7] in myPeons ) and ( [8,8] in myPeons ):
                for peon in myPeons:
                    if peon[0] < 8:
                        return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
                    else:
                        cont += 1
                if cont == 3:
                    return self.move_lateral(myPeons)
            else:
                return self.move_lateral(myPeons)
            
    def move_lateral(self, myPeons):
        freePeonsHorizontal = []
        for peon in myPeons:
            if peon[1] != 8:
                freePeonsHorizontal.append(peon)
        for peon in freePeonsHorizontal:
            if [ peon[0] , peon[1] + 1 ] in myPeons:
                freePeonsHorizontal.remove(peon)
        from_row = freePeonsHorizontal[0][0]
        from_col = freePeonsHorizontal[0][1]
        to_row = from_row
        to_col = from_col + 1
        if len(freePeonsHorizontal) > 0:
            for peon in freePeonsHorizontal:
                if from_col < peon[1] :
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row
                    to_col = from_col + 1
        return self.send(from_row, from_col, to_row, to_col)
                
    def verify_peons_vertical(self, myPeons, enPeons, wallsH, wallsV):
        
        freePeonsVertical = []
        jumpPeonsVertical = []
        for peon in myPeons:
            if [ ( peon[0] + ( 1 if self.requestData["data"]["side"] == "N" else -1 ) ) , peon[1] ] in enPeons:
                jumpPeonsVertical.append(peon)
            else:
                freePeonsVertical.append(peon)
        if len(jumpPeonsVertical) > 0:
            return self.valid_vertical_jump(myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH, wallsV)
        else:    
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
    
    def valid_vertical_jump(self, myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH, wallsV):
        
        jumpPeonsVerticalValid = []
        for peon in jumpPeonsVertical:
            if self.requestData["data"]["side"] == "N":
                if ( not( peon in wallsH)  ) and ( not( [ peon[0] , peon[1] - 1 ] in wallsH) ):
                    jumpPeonsVerticalValid.append(peon)
            else:
                if not( ( [ peon[0] - 1 , peon[1] ] in wallsH ) and not( [ peon[0] - 1 , peon[1] - 1 ] in wallsH ) ):
                    jumpPeonsVerticalValid.append(peon)
        if len(jumpPeonsVerticalValid) > 0:
            for peon in jumpPeonsVerticalValid:
                if self.requestData["data"]["side"] == "N":
                    if peon[0] < 7 and not(peon in jumpPeonsVerticalValid):
                        jumpPeonsVerticalValid.append(peon)
                else:
                    if peon[0] > 1 and not(peon in jumpPeonsVerticalValid):
                        jumpPeonsVerticalValid.append(peon)
        else:
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        if len(jumpPeonsVerticalValid) > 0:
            for peon in jumpPeonsVerticalValid:
                to_row = peon[0] + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                to_col = peon[1]
                if ( [ to_row , to_col ] in enPeons ) or ( [ to_row , to_col ] in myPeons ):
                    jumpPeonsVerticalValid.remove([ peon[0] , peon[1] ] )
        else:
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        if len(jumpPeonsVerticalValid) > 0:
            return self.move_peon_jump(jumpPeonsVerticalValid)
        else:
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
    
    def valid_vertical_move(self, myPeons, enPeons, freePeonsVertical, wallsH, wallsV):
        
        HorizontalMove = horizontal_move.Horizontal_Move(self.requestData)
        freePeonsVerticalValid = []
        for peon in freePeonsVertical:
            if self.requestData["data"]["side"] == "N":
                if not( ( peon in wallsH ) or ( [ peon[0] , peon[1] - 1 ] in wallsH ) ):
                    freePeonsVerticalValid.append(peon)
            else:
                if not( ( [ peon[0] - 1 , peon[1] ] in wallsH ) or ( [ peon[0] - 1 , peon[1] - 1 ] in wallsH ) ):
                    freePeonsVerticalValid.append(peon)
        if len(freePeonsVerticalValid) > 0:
            for peon in freePeonsVerticalValid:
                if [ peon[0] + ( 1 if self.requestData["data"]["side"] == "N" else -1 ) , peon[1] ] in myPeons:
                    freePeonsVerticalValid.remove(peon)
        #else:
        #    return HorizontalMove.horizontal_move(myPeons, enPeons, wallsH, wallsV)
        if len(freePeonsVerticalValid) > 0:
            return self.move_peon_free(freePeonsVerticalValid)
        #else:
        #    return HorizontalMove.horizontal_move(myPeons, enPeons, wallsH, wallsV)
        
       
    
    def move_peon_jump(self, jumpPeonsVerticalValid):
        
        from_row = jumpPeonsVerticalValid[0][0]
        from_col = jumpPeonsVerticalValid[0][1]
        to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
        to_col = from_col
        if len(jumpPeonsVerticalValid) > 1:
            for peon in jumpPeonsVerticalValid:
                if ( ( self.requestData["data"]["side"] == "N" and from_row < peon[0] ) and peon[0] < 7 ) or ( (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) and peon[0] > 1 ):
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                    to_col = from_col
        return self.send(from_row, from_col, to_row, to_col)
        
    def move_peon_free(self, freePeonsVerticalValid):
        
        from_row = freePeonsVerticalValid[0][0]
        from_col = freePeonsVerticalValid[0][1]
        to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
        to_col = from_col
        if len(freePeonsVerticalValid) > 1:
                for peon in freePeonsVerticalValid:
                    if ( (self.requestData["data"]["side"] == "N" and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) ):
                        from_row = peon[0]
                        from_col = peon[1]
                        to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
                        to_col = from_col 
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