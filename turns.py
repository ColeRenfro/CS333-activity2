import Square as square

class Turns:
    
    #currentPlayer = 'X'

    def turnSwitch(currentPlayer):
    
        if currentPlayer == 'X':
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'

    def turnCheck(currentPlayer):
        
        while True:
            
            while currentPlayer == 'X':
                print("Player X's turn: ")
                square.xPlayerInput()
                square.win('X')
            
            while currentPlayer == 'O':
                print("Player O's turn:")
                square.oPlayerInput()
                square.win('O')

    def turns():
        currentPlayer = 'X'
        Turns.turnSwitch(currentPlayer)
        Turns.turnCheck(currentPlayer)


if __name__=='__main__':
    print("running")
    Turns.turns()

