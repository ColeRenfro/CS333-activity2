""" Skeleton of a Board class for a TicTacToe game """

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        pass

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
