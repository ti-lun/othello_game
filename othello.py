#### Katie Bui, #78495392.  Let's get codin'!

#### Global constants to designate players to integer values.

NONE = 0
BLACK = 1
WHITE = 2

class GameState:

    def __init__(self, rows: int, columns: int):

        self._board = []    # Currently an empty board.
        self._turn = 0 # It's no one's turn.
        self._rows = rows
        self._columns = columns

        
    def create_board(self) -> [list]:
        ''' Creates new board with specified columns and rows, fills it up with 0s '''    

        try:

            if self._rows % 2 != 0 or self._rows < 4 or self._rows > 16:
                raise InvalidMoveError()

            elif self._columns % 2 != 0 or self._columns < 4 or self._columns > 16:
                raise InvalidMoveError()

            new_board = []
            
            for col in range(self._columns):
                new_col = []
                
                for row in range(self._rows):
                    new_col.append(0)
                    
                new_board.append(new_col)

            self._board = new_board

        except InvalidMoveError:
            print('INVALID ROWS AND/OR COLUMNS')


    def initialize_discs(self, turn: int) -> None:
        ''' Starts gameplay with four pieces in the center of the board '''

        #first pieces
        self._board[int(1 + (self._columns - 4)/2)][int(1 + (self._rows - 4)/2)] = turn
        self._board[int(2 + (self._columns - 4)/2)][int(2 + (self._rows - 4)/2)] = turn

        #second pieces
        self._board[int(1 + int(self._columns - 4)/2)][int(2 + int(self._rows - 4)/2)] = self.opposite_turn(turn)
        self._board[int(2 + (self._columns - 4)/2)][int(1 + (self._rows - 4)/2)] = self.opposite_turn(turn)


    def flip(self, turn: int, spot_col: int, spot_row: int) -> None:
        ''' Flips discs in the game board according to the spot in the board that's picked.
        It also switches the turn to be opposite of the player who just moved. '''

        self.is_spot_empty(spot_col, spot_row)
        flip_these = self.master_flip(turn, spot_col, spot_row)

        if flip_these == []:
            raise InvalidMoveError()
        
        elif self._board[spot_col][spot_row] != 0:
            raise InvalidMoveError()
        
        else:
            for discs in flip_these:
                self._board[discs[0]][discs[1]] = turn
                self._board[spot_col][spot_row] = turn
            
            self._turn = self.switch_turn()
            

    def count_discs(self, player: int) -> int:
        ''' Counts up all the discs of a certain player '''
        
        sum = 0
        
        for row in range(len(self._board[0])):
            
            for col in range(len(self._board)):
                if self._board[col][row] == player:
                    sum += 1
        return sum
    

    def return_board(self) -> [list]:
        ''' Returns the game board. '''

        return self._board                   

    ### TURN
    
    def first_turn(self, turn: int) -> int:
        ''' Sets the GameState turn with who goes first '''

        self._turn = turn
        
        return self._turn
    

    def opposite_turn(self, turn: int) -> int:
        ''' Reverses the turn regardless of what the GameState's turn is. '''

        if turn == 1:
            return 2
        
        elif turn == 2:
            return 1


    def switch_turn(self) -> int:
        ''' Switches the GameState's turn to the other player '''

        if self._turn == 1:
            self._turn = 2
            
        elif self._turn == 2:
            self._turn = 1
            
        return self._turn

    ### WINNER

    def master_valid_before(self, turn: int) -> bool:
        ''' Returns bool if, for a certain player, the player can make a valid move '''

        master_flip_these = []
        empty_spots = self.find_empty_spots()

        for column, row in empty_spots:

            flip_these = self.master_flip(turn, column, row)
            master_flip_these.extend(flip_these)
        
        if master_flip_these == []:
            return False
        else:
            return True
            

    def master_invalid_after(self, turn: int) -> None:
        ''' Raises InvalidMoveError if there are no discs to be flipped. '''

        master_flip_these = []
        empty_spots = self.find_empty_spots()

        for column, row in empty_spots:

            flip_these = self.master_flip(turn, column, row)
            master_flip_these.extend(flip_these)
        
        if master_flip_these == []:
            raise CannotMoveError()


    def are_there_no_valid_moves(self) -> bool:
        ''' Checks if both players can move; if not, then it returns False. '''

        if self.master_valid_before(self._turn) == False and self.master_valid_before(self.opposite_turn(self._turn)) == False:
            return True
        else:
            return False


    def judge_winner(self, sign: 'str') -> str:
        ''' Determines who is the winner based on sign '''
        

        total_black = self.count_discs(1)
        total_white = self.count_discs(2)

        if sign == '>':
            
            if total_black > total_white:
                return 'BLACK'
            
            elif total_black < total_white:
                return 'WHITE'
            
            else:
                return 'NONE'
            
        elif sign == '<':
            
            if total_black < total_white:
                return 'BLACK'
            
            elif total_black > total_white:
                return 'WHITE'
            
            else:
                return 'NONE'


    def try_to_flip(self, turn: int, spot_col: int, spot_row: int, put_here: list, direction: tuple) -> list:
        ''' Returns list of discs to flip in ONE direction '''

        column_direction = direction[0]
        row_direction = direction[1]
        
        try:

            if spot_col < 0 or spot_row < 0:
                return []

            elif self._board[spot_col][spot_row] == turn:
                return put_here

            elif self._board[spot_col+column_direction][spot_row+row_direction] == 0:
                return []

            else:
                put_here.append((spot_col, spot_row))
                return self.try_to_flip(turn, spot_col+column_direction, spot_row+row_direction, put_here, direction)

        except IndexError:

            return []


        
    def master_flip(self, turn: int, spot_col: int, spot_row: int) -> list:
        ''' Returns list of discs to flip in all directions in ONE spot '''
        
        discs_to_flip = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:

            discs_to_flip.extend(self.try_to_flip(turn, spot_col, spot_row, [], direction))

        while (spot_col, spot_row) in discs_to_flip:

            discs_to_flip.remove((spot_col, spot_row))
            
        return discs_to_flip


    def find_empty_spots(self) -> list:
        ''' Returns list of spots in the board that are empty '''

        empty_spots_list = []
        
        for column in range(len(self._board)):
            
            for row in range(len(self._board[column])):
                
                if self._board[column][row] == 0:
                    empty_spots_list.append((column, row))

        return empty_spots_list
    

    def is_spot_empty(self, spot_col: int, spot_row: int) -> None:

        if self._board[spot_col][spot_row] != 0:
           raise InvalidMoveError()
        

class InvalidMoveError(Exception):
    pass

class CannotMoveError(Exception):
    pass
