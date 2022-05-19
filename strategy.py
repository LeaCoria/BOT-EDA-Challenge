from random import randint

class Strategy():
    def __init__ (self, requestData):
        
        self.requestData = requestData
    
    def main_strategy (self, myPeons, enPeons, wallsH, wallsV, arrayBoard):

        index = 0
        freePeons = []
        jumpPeons = []
        for peons in myPeons:
            if self.requestData["data"]["side"] == "N":
                if not( ( peons[0] + 1 == enPeons[0][0] and peons[1] == enPeons[0][1] ) or ( peons[0] + 1 == enPeons[1][0] and peons[1] == enPeons[1][1] ) or ( peons[0] + 1 == enPeons[2][0] and peons[1] == enPeons[2][1] ) ):
                    freePeons.append(myPeons[index])
                if ( ( peons[0] + 1 == enPeons[0][0] and peons[1] == enPeons[0][1] ) or ( peons[0] + 1 == enPeons[1][0] and peons[1] == enPeons[1][1] ) or ( peons[0] + 1 == enPeons[2][0] and peons[1] == enPeons[2][1] ) ):
                    jumpPeons.append(myPeons[index])
                index += 1
            if self.requestData["data"]["side"] == "S":
                if not( ( peons[0] - 1 == enPeons[0][0] and peons[1] == enPeons[0][1] ) or ( peons[0] - 1 == enPeons[1][0] and peons[1] == enPeons[1][1] ) or ( peons[0] - 1 == enPeons[2][0] and peons[1] == enPeons[2][1] ) ):
                    freePeons.append(myPeons[index])
                if ( ( peons[0] - 1 == enPeons[0][0] and peons[1] == enPeons[0][1] ) or ( peons[0] - 1 == enPeons[1][0] and peons[1] == enPeons[1][1] ) or ( peons[0] - 1 == enPeons[2][0] and peons[1] == enPeons[2][1] ) ):
                    jumpPeons.append(myPeons[index])
                index += 1
        return self.valid_vertical_move(myPeons, enPeons, jumpPeons, freePeons, wallsH, wallsV, arrayBoard)
    
    def valid_vertical_move(self, myPeons, enPeons, jumpPeons, freePeons, wallsH, wallsV, arrayBoard):
        
      
        freePeonsVerticalValid = []
        jumpPeonsVerticalValid = []
        if len(freePeons) > 0:
            for peon in freePeons:
                if self.requestData["data"]["side"] == "N":
                    if not(peon in wallsH):
                        freePeonsVerticalValid.append(peon)
                else:
                    if not( [ peon[0] - 1 , peon[1] ] in wallsH ):
                        freePeonsVerticalValid.append(peon)
        if len(jumpPeons) > 0:
            for peon in jumpPeons:
                if self.requestData["data"]["side"] == "N":
                    if not(peon in wallsH):
                        jumpPeonsVerticalValid.append(peon)
                else:
                    if not( [ peon[0] - 1 , peon[1] ] in wallsH ):
                        jumpPeonsVerticalValid.append(peon)
            if len(jumpPeonsVerticalValid) > 0:
                for peon in jumpPeonsVerticalValid:
                    if self.requestData["data"]["side"] == "N":
                        if peon[0] < 7 and not(peon in jumpPeonsVerticalValid):
                            jumpPeonsVerticalValid.append(peon)
                    else:
                        if peon[0] > 1 and not(peon in jumpPeonsVerticalValid):
                            jumpPeonsVerticalValid.append(peon)
            if len(jumpPeonsVerticalValid) > 0:
                for peon in jumpPeonsVerticalValid:
                    to_row = peon[0] + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                    to_col = peon[1]
                    if [ to_row , to_col ] in enPeons:
                        jumpPeonsVerticalValid.remove([ peon[0] , peon[1] ] )
            if len(jumpPeonsVerticalValid) > 0:
                for peon in jumpPeonsVerticalValid:
                    to_row = peon[0] + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                    to_col = peon[1]
                    if [ to_row , to_col ] in myPeons:
                        jumpPeonsVerticalValid.remove([ peon[0] , peon[1] ] )
        return self.move_peon(freePeonsVerticalValid, jumpPeonsVerticalValid, arrayBoard)
       
    
    def move_peon(self, freePeonsVerticalValid, jumpPeonsVerticalValid, arrayBoard):
        
        if len(jumpPeonsVerticalValid) > 0:
            from_row = jumpPeonsVerticalValid[0][0]
            from_col = jumpPeonsVerticalValid[0][1]
            to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
            to_col = from_col
            if len(jumpPeonsVerticalValid) > 1:
                if len(jumpPeonsVerticalValid) == 3:
                    from_row = jumpPeonsVerticalValid[0][0]
                    from_col = jumpPeonsVerticalValid[randint(0,2)][1]
                    to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                    to_col = from_col
                else:
                    if len(jumpPeonsVerticalValid) == 2:
                        from_row = jumpPeonsVerticalValid[0][0]
                        from_col = jumpPeonsVerticalValid[randint(0,1)][1]
                        to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                        to_col = from_col
                    else:
                        for peon in jumpPeonsVerticalValid:
                            if ( (self.requestData["data"]["side"] == "N" and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) ):
                                from_row = peon[0]
                                from_col = peon[1]
                                to_row = from_row + ( 2 if self.requestData["data"]["side"] == "N" else -2 )
                                to_col = from_col
        else:
            from_row = freePeonsVerticalValid[0][0]
            from_col = freePeonsVerticalValid[0][1]
            to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
            to_col = from_col
            if len(freePeonsVerticalValid) > 0:
                if len(freePeonsVerticalValid) > 1:
                    if len(jumpPeonsVerticalValid) == 3:
                        from_row = jumpPeonsVerticalValid[0][0]
                        from_col = jumpPeonsVerticalValid[randint(0,2)][1]
                        to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
                        to_col = from_col
                    else:
                        if len(jumpPeonsVerticalValid) == 2:
                            from_row = jumpPeonsVerticalValid[0][0]
                            from_col = jumpPeonsVerticalValid[randint(0,1)][1]
                            to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
                            to_col = from_col
                        else:
                            for peon in freePeonsVerticalValid:
                                if ( (self.requestData["data"]["side"] == "N" and from_row < peon[0] ) or (self.requestData["data"]["side"] == "S" and from_row > peon[0] ) ):
                                    from_row = peon[0]
                                    from_col = peon[1]
                                    to_row = from_row + ( 1 if self.requestData["data"]["side"] == "N" else -1 )
                                    to_col = from_col
        return {
            "from_row": from_row,
            "from_col": from_col,
            "to_row": to_row,
            "to_col": to_col
        }