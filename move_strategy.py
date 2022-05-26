import horizontal_move

class Move_Strategy():
    
    def __init__ (self, requestData):
        
        self.requestData = requestData
    
    def main_move_strategy (self, myPeons, enPeons, wallsH, wallsV):
        
        #At the begining of the move function I'll verify wich peons I able
        #to move forward. But for the existence of the barrier it's probable
        #that the potencial move it's going to be to the hall on the rigth
        #border. In case that a vertical move is posible and all of my peons
        #are in the right border I will call a vertical move function to do so
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        if sideIsNorth:
            cont = 0
            for peon in myPeons:
                if ( peon[0] == 0 ) and not( [0,8] in myPeons ):
                    cont += 1
                else:
                    return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            if cont == 3:
                return self.move_lateral(myPeons)
        else:
            cont = 0
            for peon in myPeons:
                if ( peon[0] == 8 ) and not( [8,8] in myPeons ):
                    cont += 1
                else:
                    return self.verify_peons_vertical(myPeons, enPeons, wallsH, wallsV)
            if cont == 3:
                return self.move_lateral(myPeons)
            
    def move_lateral(self, myPeons):
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
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
        
        #In this function I'll verify the vertical moves and discriminate
        #them for free movement or jump movement
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        freePeonsVertical = []
        jumpPeonsVertical = []
        for peon in myPeons:
            if [ ( peon[0] + ( 1 if sideIsNorth else -1 ) ) , peon[1] ] in enPeons:
                jumpPeonsVertical.append(peon)
            else:
                freePeonsVertical.append(peon)
        if len(jumpPeonsVertical) > 0:
            return self.valid_vertical_jump(myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH, wallsV)
        else:    
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
    
    def valid_vertical_jump(self, myPeons, enPeons, jumpPeonsVertical, freePeonsVertical, wallsH, wallsV):
        
        #Validations of the vertical jumps movements
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        jumpPeonsVerticalValid = []
        jumpPeonsDiagonal = []
        for peon in jumpPeonsVertical:
            if sideIsNorth:
                if ( not( peon in wallsH)  ) and ( not( [ peon[0] , peon[1] - 1 ] in wallsH) ):
                    if not( [ peon[0] + 1 , peon[1] ] in wallsH ) and not( [ peon[0] + 1 , peon[1] - 1 ] in wallsH ):
                        jumpPeonsVerticalValid.append(peon)
                    else:
                        jumpPeonsDiagonal.append(peon)
            else:
                if not( [ peon[0] - 1 , peon[1] ] in wallsH) and not( [ peon[0] - 1 , peon[1] - 1 ] in wallsH):
                    if not( [ peon[0] - 2 , peon[1] ] in wallsH ) and not( [ peon[0] - 2 , peon[1] - 1 ] in wallsH ):
                        jumpPeonsVerticalValid.append(peon)
                    else:
                        jumpPeonsDiagonal.append(peon)
        if len(jumpPeonsVerticalValid) > 0:
            for peon in jumpPeonsVerticalValid:
                if sideIsNorth:
                    if peon[0] < 7 and not(peon in jumpPeonsVerticalValid):
                        jumpPeonsVerticalValid.append(peon)
                else:
                    if peon[0] > 1 and not(peon in jumpPeonsVerticalValid):
                        jumpPeonsVerticalValid.append(peon)
        else:
            if len(jumpPeonsDiagonal) > 0:
                return self.valid_diagonal_jump(myPeons, enPeons, jumpPeonsDiagonal, freePeonsVertical, wallsH, wallsV)
            else:
                return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        if len(jumpPeonsVerticalValid) > 0:
            for peon in jumpPeonsVerticalValid:
                to_row = peon[0] + ( 2 if sideIsNorth else -2 )
                to_col = peon[1]
                if ( [ to_row , to_col ] in enPeons ) or ( [ to_row , to_col ] in myPeons ):
                    jumpPeonsVerticalValid.remove([ peon[0] , peon[1] ] )
        else:
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        if len(jumpPeonsVerticalValid) > 0:
            return self.move_peon_jump(jumpPeonsVerticalValid)
        else:
            if len(jumpPeonsDiagonal) > 0:
                return self.valid_diagonal_jump(myPeons, enPeons, jumpPeonsDiagonal, freePeonsVertical, wallsH, wallsV)
            else:
                return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        
    def valid_diagonal_jump(self, myPeons, enPeons, jumpPeonsDiagonal, freePeonsVertical, wallsH, wallsV):
        
        #Validations of the diagonal jumps movements

        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        jumpPeonsDiagonalRigthValid = []
        jumpPeonsDiagonalLeftValid = []
        for peon in jumpPeonsDiagonal:
            if sideIsNorth:
                if not( [ peon[0] , peon[1] ] in wallsV ) and not( [ peon[0] + 1 , peon[1] ] in wallsV ):
                    jumpPeonsDiagonalRigthValid.append(peon)
                if not( [ peon[0] , peon[1] - 1 ] in wallsV ) and not( [ peon[0] + 1 , peon[1] - 1 ] in wallsV ):
                    jumpPeonsDiagonalLeftValid.append(peon)
            else:
                if not( [ peon[0] - 1 , peon[1] ] in wallsV ) and not( [ peon[0] - 2 , peon[1] ] in wallsV ):
                    jumpPeonsDiagonalRigthValid.append(peon)
                if not( [ peon[0] - 1 , peon[1] - 1 ] in wallsV ) and not( [ peon[0] - 2 , peon[1] - 1 ] in wallsV ):
                    jumpPeonsDiagonalLeftValid.append(peon)
        if len(jumpPeonsDiagonalRigthValid) > 0:
            for peon in jumpPeonsDiagonalRigthValid:
                if sideIsNorth:
                    if  ( peon[1] == 8 ) or ( [ peon[0] + 1 , peon[1] + 1 ] in myPeons ) or ( [ peon[0] + 1 , peon[1] + 1 ] in enPeons ):
                        jumpPeonsDiagonalRigthValid.remove(peon)
                        if not(peon in jumpPeonsDiagonalLeftValid):
                            jumpPeonsDiagonalLeftValid.append(peon)
                else:
                    if ( peon[1] == 8 ) or ( [ peon[0] - 1 , peon[1] - 1 ] in myPeons ) or ( [ peon[0] - 1 , peon[1] - 1 ] in enPeons ):
                        jumpPeonsDiagonalRigthValid.remove(peon)
                        if not(peon in jumpPeonsDiagonalLeftValid):
                            jumpPeonsDiagonalLeftValid.append(peon)
        if len(jumpPeonsDiagonalRigthValid) > 0:
            return self.move_peon_jump_diagonal_rigth(jumpPeonsDiagonalRigthValid)
        else:
            if len(jumpPeonsDiagonalLeftValid) > 0:
                for peon in jumpPeonsDiagonalLeftValid:
                    if sideIsNorth:
                        if ( peon[1] == 0 ) or ( [ peon[0] + 1 , peon[1] - 1 ] in myPeons ):
                            jumpPeonsDiagonalLeftValid.remove(peon)
                    else:
                        if ( peon[1] == 0 ) or ( [ peon[0] + 1 , peon[1] - 1 ] in myPeons ):
                            jumpPeonsDiagonalLeftValid.remove(peon)
            else:
                return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        if len(jumpPeonsDiagonalLeftValid) > 0:
            return self.move_peon_jump_diagonal_left(jumpPeonsDiagonalLeftValid)
        else:
            return self.valid_vertical_move(myPeons, enPeons, freePeonsVertical, wallsH, wallsV)
        
    def valid_vertical_move(self, myPeons, enPeons, freePeonsVertical, wallsH, wallsV):
        
        #Validations of the vertical movements

        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        HorizontalMove = horizontal_move.Horizontal_Move(self.requestData)
        freePeonsVerticalValid = []
        peonsHorizontalMove = []
        for peon in freePeonsVertical:
            if sideIsNorth:
                if not( ( peon in wallsH ) or ( [ peon[0] , peon[1] - 1 ] in wallsH ) ):
                    freePeonsVerticalValid.append(peon)
            elif not( ( [ peon[0] - 1 , peon[1] ] in wallsH ) or ( [ peon[0] - 1 , peon[1] - 1 ] in wallsH ) ):
                    freePeonsVerticalValid.append(peon)
            else:
                peonsHorizontalMove.append(peon)
        if len(freePeonsVerticalValid) > 0:
            for peon in freePeonsVerticalValid:
                if [ peon[0] + ( 1 if sideIsNorth else -1 ) , peon[1] ] in myPeons:
                    freePeonsVerticalValid.remove(peon)
        else:
            return HorizontalMove.verify_horizontal_move(myPeons, enPeons, peonsHorizontalMove, wallsH, wallsV)
        if len(freePeonsVerticalValid) > 0:
            return self.move_peon_free(freePeonsVerticalValid)
        else:
            return HorizontalMove.verify_horizontal_move(myPeons, enPeons, peonsHorizontalMove, wallsH, wallsV)
    
    def move_peon_jump(self, jumpPeonsVerticalValid):
        
         #Function that vertically jump an enemy peon and select
        #the closest peon to opponent's frontier

        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False

        from_row = jumpPeonsVerticalValid[0][0]
        from_col = jumpPeonsVerticalValid[0][1]
        to_row = from_row + ( 2 if sideIsNorth else -2 )
        to_col = from_col
        if len(jumpPeonsVerticalValid) > 1:
            for peon in jumpPeonsVerticalValid:
                if ( ( sideIsNorth and from_row < peon[0] ) and peon[0] < 7 ) or ( (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) and peon[0] > 1 ):
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row + ( 2 if sideIsNorth else -2 )
                    to_col = from_col
        return self.send(from_row, from_col, to_row, to_col)
    
    def move_peon_jump_diagonal_rigth(self, jumpPeonsDiagonalRigthValid):
        
        #Function that diagonal jump an enemy peon and select
        #the closest peon to opponent's frontier
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        from_row = jumpPeonsDiagonalRigthValid[0][0]
        from_col = jumpPeonsDiagonalRigthValid[0][1]
        to_row = from_row + ( 1 if sideIsNorth else -1 )
        to_col = from_col + 1
        if len(jumpPeonsDiagonalRigthValid) > 1:
            for peon in jumpPeonsDiagonalRigthValid:
                if ( sideIsNorth and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ):
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row + ( 1 if sideIsNorth else -1 )
                    to_col = from_col + 1
        return self.send(from_row, from_col, to_row, to_col)
    
    def move_peon_jump_diagonal_left(self, jumpPeonsDiagonalLeftValid):
            
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
            
        from_row = jumpPeonsDiagonalLeftValid[0][0]
        from_col = jumpPeonsDiagonalLeftValid[0][1]
        to_row = from_row + ( 1 if sideIsNorth else -1 )
        to_col = from_col - 1
        if len(jumpPeonsDiagonalLeftValid) > 1:
            for peon in jumpPeonsDiagonalLeftValid:
                if ( sideIsNorth and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ):
                    from_row = peon[0]
                    from_col = peon[1]
                    to_row = from_row + ( 1 if sideIsNorth else -1 )
                    to_col = from_col - 1
        return self.send(from_row, from_col, to_row, to_col)
    
    def move_peon_free(self, freePeonsVerticalValid):
        
        #Function that vertically moves forward the closest
        #peon to the enemy's frontier
        
        if self.requestData["data"]["side"] == "N":
            sideIsNorth = True
        else:
            sideIsNorth = False
        
        from_row = freePeonsVerticalValid[0][0]
        from_col = freePeonsVerticalValid[0][1]
        to_row = from_row + ( 1 if sideIsNorth else -1 )
        to_col = from_col
        if len(freePeonsVerticalValid) > 1:
                for peon in freePeonsVerticalValid:
                    if ( (sideIsNorth and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) ):
                        from_row = peon[0]
                        from_col = peon[1]
                        to_row = from_row + ( 1 if sideIsNorth else -1 )
                        to_col = from_col 
        return self.send(from_row, from_col, to_row, to_col)
    
    def send(self, from_row, from_col, to_row, to_col):
        
        #Function that send the message to the server
        
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