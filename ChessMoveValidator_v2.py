class Chess:
    ## Constructor
    def __init__(self):
        self.chessBoard = []
        for _ in range(8):
            chessRow = [0]*8
            self.chessBoard.append(chessRow)

    ## Print Board
    def printBoard(self):
        print("\n")
        for row in range(8):
            for col in range(8):
                print(str(self.chessBoard[row][col]).center(5),end = " ")
            print("\n")
        print("\n")

    ## Validate whether the destination location has a piece from same player
    def samePlayerPieceValidation(self, sourceRow, sourceCol, destRow, destCol):
        if self.chessBoard[destRow][destCol] != 0:
            if self.chessBoard[destRow][destCol][0] == self.chessBoard[sourceRow][sourceCol][0]:
                print("Error: Already have a piece by same player at dest location")
                return False
        return True

    ## Start a new game by resetting the chessboard
    def newGame(self):
        self.chessBoard[0][0], self.chessBoard[0][7] = '1R1', '1R2'
        self.chessBoard[0][1], self.chessBoard[0][6] = '1K1', '1K2'
        self.chessBoard[0][2], self.chessBoard[0][5] = '1B1', '1B2'
        self.chessBoard[0][3], self.chessBoard[0][4] = '1Q', '1X'
        
        self.chessBoard[7][0], self.chessBoard[7][7] = '2R1', '2R2'
        self.chessBoard[7][1], self.chessBoard[7][6] = '2K2', '2K2'
        self.chessBoard[7][2], self.chessBoard[7][5] = '2B2', '2B2'
        self.chessBoard[7][3], self.chessBoard[7][4] = '2Q', '2X'
        
        for pawn in range(len(self.chessBoard)):
            self.chessBoard[1][pawn] = '1P' + str(pawn+1)
            self.chessBoard[6][pawn] = '2P' + str(pawn+1)
        
        self.printBoard()

    ## Validate the movement of rook
    def ValidateRookMove(self, sourceRow, sourceCol, destRow, destCol):
        if not self.samePlayerPieceValidation(sourceRow, sourceCol, destRow, destCol):
            return False
        
        if sourceRow == destRow:
            if destCol > sourceCol:
                pointer = sourceCol + 1
                while pointer != destCol:
                    if self.chessBoard[destRow][pointer] != 0:
                        print("Error: Piece in between")
                        return False
                    pointer += 1
            else:
                pointer = sourceCol - 1
                while pointer != destCol:
                    if self.chessBoard[destRow][pointer] != 0:
                        print("Error: Piece in between")
                        return False
                    pointer -= 1
        elif sourceCol == destCol:
            if destRow > sourceRow:
                pointer = sourceRow + 1
                while pointer != destRow:
                    if self.chessBoard[pointer][destCol] != 0:
                        print("Error: Piece in between")
                        return False
                    pointer += 1
            else:
                pointer = sourceRow - 1
                while pointer != destRow:
                    if self.chessBoard[pointer][destCol] != 0:
                        print("Error: Piece in between")
                        return False
                    pointer -= 1
        else:
            print('Error: Wrong Move!!')
            return False
        return True

    ## Validate movement of Bishop
    def ValidateBishopMove(self, sourceRow, sourceCol, destRow, destCol):

        if not self.samePlayerPieceValidation(sourceRow, sourceCol, destRow, destCol):
            return False

        def checkPieceInBetween (rp, cp):
            if self.chessBoard[rp][cp] != 0:
                print("Error: Piece in between")
                return False
            return True
            
        if destRow > sourceRow and destCol > sourceCol:
            rowPointer = sourceRow + 1
            colPointer = sourceCol + 1
            ValidMoves = []
            while rowPointer < 8 and colPointer < 8:
                vm = [rowPointer, colPointer]
                ValidMoves.append(vm)
                rowPointer += 1
                colPointer += 1
            if [destRow, destCol] in ValidMoves:
                rowPointer = sourceRow + 1
                colPointer = sourceCol + 1
                while rowPointer != destRow:
                    isPieceInBtw = checkPieceInBetween(rowPointer, colPointer)
                    if not isPieceInBtw:
                        return False
                    rowPointer += 1
                    colPointer += 1
            else:
                print("Error: Wrong Move!!")
                return False
                    
        elif destRow < sourceRow and destCol < sourceCol:
            rowPointer = sourceRow - 1
            colPointer = sourceCol - 1
            ValidMoves = []
            while rowPointer > -1 and colPointer > -1:
                vm = [rowPointer, colPointer]
                ValidMoves.append(vm)
                rowPointer -= 1
                colPointer -= 1
            if [destRow, destCol] in ValidMoves:
                rowPointer = sourceRow - 1
                colPointer = sourceCol - 1
                while rowPointer != destRow:
                    isPieceInBtw = checkPieceInBetween(rowPointer, colPointer)
                    if not isPieceInBtw:
                        return False
                    rowPointer -= 1
                    colPointer -= 1
            else:
                print("Error: Wrong Move!!")
                return False
        elif destRow > sourceRow and destCol < sourceCol:
            rowPointer = sourceRow + 1
            colPointer = sourceCol - 1
            ValidMoves = []
            while rowPointer < 8 and colPointer > -1:
                vm = [rowPointer, colPointer]
                ValidMoves.append(vm)
                rowPointer += 1
                colPointer -= 1
            print(vm)
            if [destRow, destCol] in ValidMoves:
                rowPointer = sourceRow + 1
                colPointer = sourceCol - 1
                while rowPointer != destRow:
                    isPieceInBtw = checkPieceInBetween(rowPointer, colPointer)
                    print('piece btw value', isPieceInBtw)
                    if not isPieceInBtw:
                        return False
                    rowPointer += 1
                    colPointer -= 1
            else:
                print("Error: Wrong Move!!")
                return False
        elif destRow < sourceRow and destCol > sourceCol:
            rowPointer = sourceRow - 1
            colPointer = sourceCol + 1
            ValidMoves = []
            while rowPointer > -1 and colPointer < 8:
                vm = [rowPointer, colPointer]
                ValidMoves.append(vm)
                rowPointer -= 1
                colPointer += 1
            if [destRow, destCol] in ValidMoves:
                rowPointer = sourceRow - 1
                colPointer = sourceCol + 1
                while rowPointer != destRow:
                    isPieceInBtw = checkPieceInBetween(rowPointer, colPointer)
                    if not isPieceInBtw:
                        return False
                    rowPointer -= 1
                    colPointer += 1
            else:
                print("Error: Wrong Move!!")
                return False
        else:
            print("Error: Wrong Move!!")
            return False
        print("I'm here!! returning true")
        return True

    ## Validate movement of Knight
    def ValidateKnightMove (self, sourceRow, sourceCol, destRow, destCol):
        if not self.samePlayerPieceValidation(sourceRow, sourceCol, destRow, destCol):
            return False

        if sourceRow == destRow or sourceCol == destCol:
            print("Error: Wrong Move!!")
            return False

            
        if abs(sourceRow-destRow) <= 2 and abs(sourceCol - destCol) <= 2:
            if destRow > sourceRow and destCol > sourceCol:
                ValidMoves = []
                if sourceRow+2 <= 7 and sourceCol+1 <= 7:
                    ValidMoves.append([sourceRow+2,sourceCol+1])
                if sourceRow+1 <= 7 and sourceCol+2 <= 7:
                    ValidMoves.append([sourceRow+1,sourceCol+2])
                if [destRow, destCol] not in ValidMoves:
                    print("Error: Not a Valid Move")
                    return False
            elif destRow < sourceRow and destCol < sourceCol:
                ValidMoves = []
                if sourceRow-2 >= 0 and sourceCol-1 >= 0:
                    ValidMoves.append([sourceRow-2,sourceCol-1])
                if sourceRow-1 >= 0 and sourceCol-2 >= 0:
                    ValidMoves.append([sourceRow-1,sourceCol-2])
                if [destRow, destCol] not in ValidMoves:
                    print("Error: Not a Valid Move")
                    return False
            elif destRow > sourceRow and destCol < sourceCol:
                ValidMoves = []
                if sourceRow+2 <= 7 and sourceCol-1 >= 0:
                    ValidMoves.append([sourceRow+2,sourceCol-1])
                if sourceRow+1 <= 7 and sourceCol-2 >= 0:
                    ValidMoves.append([sourceRow+1,sourceCol-2])
                if [destRow, destCol] not in ValidMoves:
                    print("Error: Not a Valid Move")
                    return False
            elif destRow < sourceRow and destCol > sourceCol:
                ValidMoves = []
                if sourceRow-2 >= 0 and sourceCol+1 <= 7:
                    ValidMoves.append([sourceRow-2,sourceCol+1])
                if sourceRow-1 >= 0 and sourceCol+2 <= 7:
                    ValidMoves.append([sourceRow-1,sourceCol+2])
                if [destRow, destCol] not in ValidMoves:
                    print("Error: Not a Valid Move")
                    return False
        else:
            print("Error: Wrong Move!!")
            return False
        return True

    ## Validate movement of Queen
    def ValidateQueenMovement (self, sourceRow, sourceCol, destRow, destCol):
        if destRow == sourceRow or destCol == sourceCol:
            IsValidMove = self.ValidateRookMove(sourceRow, sourceCol, destRow, destCol)
            if not IsValidMove:
                return False
        else:
            IsValidMove = self.ValidateBishopMove(sourceRow, sourceCol, destRow, destCol)
            if not IsValidMove:
                return False
        return True

    ##Validate movement of King
    def ValidateKingMovement (self, sourceRow, sourceCol, destRow, destCol):
        if abs(destRow - sourceRow) <= 1 and abs(destRow - sourceRow) <= 1:
            if not self.samePlayerPieceValidation(sourceRow, sourceCol, destRow, destCol):
                return False
        else:
            print("Error: King can move just 1 step in any direction")
            return False
        return True

    ## Validate the movement of pawn
    def ValidatePawnMovement(self, sourceRow, sourceCol, destRow, destCol,plyr):
        steps = sourceRow - destRow
        abs_steps = abs(sourceRow - destRow)
        if (plyr == 1 and steps > 0) or (plyr == 2 and steps < 0):
            print("Error: Wrong Move") #Pawn can not move backwards
            return False
        elif sourceRow == destRow:
            print("Error: Wrong Move") #Pawn can not move sideways
            return False
        elif abs_steps > 2:
            print("Error: Wrong Move") #Pawn cannot move more than 2 steps (2 steps for forward first move)
            return False
        elif abs_steps == 2:
            if (plyr == 1 and sourceRow != 1) or (plyr == 2 and sourceRow != 6):
                print("Error: Wrong Move") # Pawn can not move more than 2 first forward steps
                return False
            elif sourceCol != destCol:
                print("Error: Wrong Move") # Pawn can only move 2 steps first forward move
                return False
            elif (plyr == 1 and (self.chessBoard[sourceRow+1][sourceCol] != 0 or self.chessBoard[sourceRow+2][sourceCol] != 0)) \
                 or (plyr == 2 and (self.chessBoard[sourceRow-1][sourceCol] != 0 or self.chessBoard[sourceRow-2][sourceCol] != 0)):
                print("Error: Piece in between") # Piece in between
                return False
            else:
                return True
        else:
            if sourceCol == destCol:   #Checking for forward move
                if (plyr == 1 and self.chessBoard[sourceRow+1][sourceCol] != 0) or (plyr == 2 and self.chessBoard[sourceRow-1][sourceCol] != 0):
                    print("Error: Piece in between") #Piece in between
                    return False
                else:
                    return True
            else:                       #Diagonal Move Validation
                if self.chessBoard[destRow][destCol] != 0 and self.samePlayerPieceValidation(sourceRow, sourceCol, destRow, destCol):
                    return True
                else:
                    print("Error: Wrong Move, Pawn Can not move at empty diagonal Position")
                    return False

## Working code Starts from here ##
if __name__ == "__main__":
    def getDestination():
        ipDest = input("Enter the location where you want to move, in the format of row:column\n")
        ipDestArray = ipDest.split(':')
        DestRow, DestColumn = int(ipDestArray[0]), int(ipDestArray[1])
        Valid = True
        if DestRow < 0 or DestRow > 7 or DestColumn < 0 or DestColumn > 7:
            Valid = False
            print("Error - Destination Location enetered is out of bounds")
        return DestRow, DestColumn, Valid
        
    print("Welcome")
    StartVariable = int(input("Enter 1 to start a new Chess Game\n"))
    if StartVariable == 1:
        print("R - represents Rook \nK - represents Knight \nB - represents Bishop \nQ - represents Queen \nX - represents King\n")
        chessGame = Chess()
        chessGame.newGame()
        ipSource = ""
        while ipSource != "E":
            print("You can exit from the game anytime by pressing any key.")
            ipSource = input("Enter the the location from where you want to move the piece in the format of row:column\n")
            try:
                ipArray = ipSource.split(':')
                SourceRow, SourceColumn = int(ipArray[0]), int(ipArray[1])
                piece = chessGame.chessBoard[SourceRow][SourceColumn]
                if piece != 0:
                    if piece[1] == 'R':
                        print('Rook')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidateRookMove(SourceRow, SourceColumn, DestRow, DestCol)
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                    elif piece[1] == 'K':
                        print('Knight')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidateKnightMove(SourceRow, SourceColumn, DestRow, DestCol)
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                    elif piece[1] == 'B':
                        print('Bishop')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidateBishopMove(SourceRow, SourceColumn, DestRow, DestCol)
                            print('Value of move',IsValidMove)
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                    elif piece[1] == 'X':
                        print('King')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidateKingMovement(SourceRow, SourceColumn, DestRow, DestCol)
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                    elif piece[1] == 'Q':
                        print('Queen')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidateQueenMovement(SourceRow, SourceColumn, DestRow, DestCol)
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                    else:
                        print('Pawn')
                        DestRow, DestCol, IsValidIndex  = getDestination()
                        if IsValidIndex:
                            IsValidMove = chessGame.ValidatePawnMovement(SourceRow, SourceColumn, DestRow, DestCol,int(piece[0]))
                            if IsValidMove:
                                chessGame.chessBoard[SourceRow][SourceColumn], chessGame.chessBoard[DestRow][DestCol] = 0, piece
                                chessGame.printBoard()
                else:
                    print('No chess piece is there on the given location')
            except:
                print("Exiting from the chess game.")
                break
