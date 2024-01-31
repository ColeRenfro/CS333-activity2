class Square:
    def __init__(self, emptySquare, xSquare, oSquare):
        self.empty = emptySquare
        self.x = xSquare
        self.o = oSquare

        Square = {(0,0) : "empty",(0,1) : "empty",(0,2) : "empty",
                  (1,0) : "empty",(1,1) : "empty",(1,2) : "empty",
                  (2,0) : "empty",(2,1) : "empty",(2,2) : "empty"}

    def xPlayerInput():
        
        print("What column do you want your X in?")
        xColumn = input()
        
        if xColumn == 1 or 2 or 3:
            print("What row do you want your X in?")
            xRow = input()
            if xRow == 1 or 2 or 3:
                print("X placed at ")
                print("Column ", xColumn, " ")
                print("Row ", xRow, " ")
                Square.xClaim(xColumn, xRow)

        elif xColumn or xRow != 1 or 2 or 3:
            print("Invalid position.")

        
    def oPlayerInput():
        print("What column do you want your O in?")
        oColumn = input()
        if oColumn == 1 or 2 or 3:
            print("What row do you want your O in?")
            oRow = input()
            if oRow == 1 or 2 or 3:
                print("O placed at ")
                print("Column ", oColumn, " ")
                print("Row ", oRow, " ")
                Square.oClaim(oColumn, oRow)
        elif oColumn or oRow != 1 or 2 or 3:
            print("Invalid position.")


    def xClaim(column, row):
        Square[column,row] = 'X'

    def oClaim(column, row):
        Square[column,row] = 'O'

    def spotClaimedCheck(column,row):
        if Square(column,row) != "empty":
            return False
        

        
    def getSquare(column,row):
        return Square(column,row) 
      
    def won(type):
        for i in Square:
            for j in Square:
                if Square.getSquare(i,j) == type and Square.getSquare(i+1,j+1) == type and Square.getSquare(i+2,j+2) == type:
                    
                    return True
                if Square.getSquare(i,j) == type and Square.getSquare(i+1,j) == type and Square.getSquare(i+2,j) == type:
                    return True
                if Square.getSquare(i,j) == type and Square.getSquare(i,j+1) == type and Square.getSquare(i,j+2) == type:
                    return True               
                if Square.getSquare(i+1,j) == type and Square.getSquare(i+1,j+1) == type and Square.getSquare(i+1,j+2) == type:
                    return True
                if Square.getSquare(i+2,j) == type and Square.getSquare(i+2,j+1) == type and Square.getSquare(i+2,j+2) == type:
                   return True