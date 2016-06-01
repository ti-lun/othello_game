#### Katie Bui, #78495392.  Let's get codin'!

import tkinter
import othello

DEFAULT_FONT0 = ('Franklin Gothic', 45)
DEFAULT_FONT1 = ('Franklin Gothic', 20)
DEFAULT_FONT2 = ('Franklin Gothic', 14)
DEFAULT_GRAY = '#AABBAA'

class EnterInfo:
    
    def __init__(self, master_window):
        ''' Starts the popup window and displays score and toggles settings '''
        
        self._ok_clicked = False
        self._sidebar = tkinter.Frame(
            master = master_window,
            background = DEFAULT_GRAY)

        self._sidebar.grid(
            row = 0, column = 1, padx = 30, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.display_score()
        self.get_game_input()
        
        self._sidebar.rowconfigure(0, weight = 1)
        self._sidebar.rowconfigure(2, weight = 1)
        self._sidebar.rowconfigure(3, weight = 1)
        self._sidebar.rowconfigure(4, weight = 1)
        self._sidebar.rowconfigure(5, weight = 1)
        self._sidebar.rowconfigure(6, weight = 1)
        self._sidebar.rowconfigure(7, weight = 1)
        self._sidebar.rowconfigure(8, weight = 1)
        self._sidebar.rowconfigure(9, weight = 1)
        self._sidebar.rowconfigure(10, weight = 1)
        self._sidebar.columnconfigure(0, weight = 1)


    def display_score(self):
        ''' Displays the score using string variables and user-entered names '''

        self._whose_turn = tkinter.StringVar()
        self._whose_turn.set('Start playing Othello!\n')

        turn_label = tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT1,
            background = DEFAULT_GRAY,
            textvariable = self._whose_turn)

        turn_label.grid(row = 0, column = 0, columnspan = 2)

        ### P1 Entry + score
        
        self.p1_name = tkinter.StringVar()
        self.p1_name.set('(Black)\nPlayer 1')

        p1_score_label = tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            textvariable = self.p1_name)

        p1_score_label.grid(row = 1, column = 0, padx = 10)

        self.p1_score = tkinter.StringVar()
        self.p1_score.set(0)

        p1_score = tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT0,
            background = DEFAULT_GRAY,
            textvariable = self.p1_score)

        p1_score.grid(row = 2, column = 0)

        p1_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'Player 1\'s name')

        p1_label.grid(row = 3, column = 0,
                      sticky = tkinter.W)

        self.p1_entry = tkinter.Entry(
            master = self._sidebar,
            width = 20, font = DEFAULT_FONT2)

        self.p1_entry.grid(row = 3, column = 1, padx = 10,
                           sticky = tkinter.W)

        ### P2 Entry + score

        self.p2_name = tkinter.StringVar()
        self.p2_name.set('(White)\nPlayer 2')


        p2_score_label = tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            textvariable = self.p2_name)

        p2_score_label.grid(row = 1, column = 1)

        self.p2_score = tkinter.StringVar()
        self.p2_score.set(0)

        p2_score = tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT0,
            background = DEFAULT_GRAY,
            textvariable = self.p2_score)

        p2_score.grid(row = 2, column = 1)

        p2_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'Player 2\'s name')

        p2_label.grid(row = 4, column = 0,
                      sticky = tkinter.W)

        self.p2_entry = tkinter.Entry(
            master = self._sidebar,
            width = 20, font = DEFAULT_FONT2)

        self.p2_entry.grid(row = 4, column = 1, padx = 10,
                           sticky = tkinter.W)


    def get_game_input(self):
        ''' Gets information to start Othello game; asks for rows, columns,
    first turn, upper-right tile, how to win, and if the players want to use a
    guide.  Uses drop-down menus '''
        
        OPTIONS = [4, 6, 8, 10, 12, 14, 16]

        ### Get Rows
        
        row_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'Rows:')

        row_label.grid(row = 5, column = 0, sticky = tkinter.W)

        self._row_choice = tkinter.StringVar()
        self._row_choice.set(4)

        self.row_widget = tkinter.OptionMenu(
            self._sidebar,
            self._row_choice,
            *OPTIONS)

        self.row_widget.configure(background = DEFAULT_GRAY)
        
        self.row_widget.grid(row = 5, column = 1, padx = 10, sticky = tkinter.W)

        ### Get Columns

        column_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'Columns:')

        column_label.grid(row = 6, column = 0, sticky = tkinter.W)

        self._column_choice = tkinter.StringVar()
        self._column_choice.set(4)

        self.column_widget = tkinter.OptionMenu(
            self._sidebar,
            self._column_choice,
            *OPTIONS)

        self.column_widget.configure(background = DEFAULT_GRAY)
        
        self.column_widget.grid(row = 6, column = 1, padx = 10,
                                sticky = tkinter.W)

        ### Get First Player

        firstplayer_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'First turn goes to:')

        firstplayer_label.grid(row = 7, column = 0, sticky = tkinter.W)

        self._firstplayer_choice = tkinter.StringVar()
        self._firstplayer_choice.set('black')

        self.firstplayer_widget = tkinter.OptionMenu(
            self._sidebar,
            self._firstplayer_choice,
            'black', 'white')

        self.firstplayer_widget.configure(background = DEFAULT_GRAY)
        
        self.firstplayer_widget.grid(row = 7, column = 1, padx = 10,
                                     sticky = tkinter.W)

        ### Get Upper-Right

        upperright_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'The upper-right tile is:')

        upperright_label.grid(row = 8, column = 0, sticky = tkinter.W)

        self._upperright_choice = tkinter.StringVar()
        self._upperright_choice.set('black')

        self.upperright_widget = tkinter.OptionMenu(
            self._sidebar,
            self._upperright_choice,
            'black', 'white')

        self.upperright_widget.configure(background = DEFAULT_GRAY)
        
        self.upperright_widget.grid(row = 8, column = 1, padx = 10,
                                    sticky = tkinter.W)

        ### Get To-win

        towin_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'To win is to get')

        towin_label.grid(row = 9, column = 0, sticky = tkinter.W)

        self._towin_choice = tkinter.StringVar()
        self._towin_choice.set('the most discs')

        self.towin_widget = tkinter.OptionMenu(
            self._sidebar,
            self._towin_choice,
            'the most discs', 'the least discs')

        self.towin_widget.configure(background = DEFAULT_GRAY)
        
        self.towin_widget.grid(row = 9, column = 1, padx = 10,
                               sticky = tkinter.W)

        ### Get Guide

        guide_label= tkinter.Label(
            master = self._sidebar,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY,
            text = 'Show possible moves?')

        guide_label.grid(row = 10, column = 0, sticky = tkinter.W)

        self._guide_choice = tkinter.StringVar()
        self._guide_choice.set('yes')

        self.guide_widget = tkinter.OptionMenu(
            self._sidebar,
            self._guide_choice,
            'yes', 'no')

        self.guide_widget.configure(background = DEFAULT_GRAY)
        
        self.guide_widget.grid(row = 10, column = 1, padx = 10,
                               sticky = tkinter.W)
        

    def _get_all_info(self) -> [list]:
        ''' Function that is called when the "Let's play" button is clicked. It
    grabs all the information set with the drop-down menus and turns it into a
    list of information to start the game. '''

        self.p1_name.set('(Black)\n' + self.p1_entry.get())
        self.p2_name.set('(White)\n' + self.p2_entry.get())

        useful_info = []

        useful_info.append(int(self._row_choice.get()))
        useful_info.append(int(self._column_choice.get()))

        if self._firstplayer_choice.get() == 'black':
            useful_info.append(1)
        else:
            useful_info.append(2)

        if self._upperright_choice.get() == 'black':
            useful_info.append(1)
        else:
            useful_info.append(2)

        if self._towin_choice.get() == 'the most discs':
            useful_info.append('>')
        else:
            useful_info.append('<')       

        return useful_info

class AboutPopup:
    
    def __init__(self):
        ''' Establishes Toplevel object, configures the aesthetics of the window
    and shows the user a message. '''
        
        self.about = tkinter.Toplevel()
        self.about.configure(
            background = DEFAULT_GRAY)
        self.about.wm_title('About')

        about_label = tkinter.Label(
            master = self.about,
            text = 'About',
            font = DEFAULT_FONT0,
            background = DEFAULT_GRAY)

        about_label.grid(row = 0, column = 0,
                         sticky = tkinter.W, padx = 20, pady=20)

        message_pls = '''Hello!  My name is Katie Bui, student ID #78495932.  This is an \nassignment for ICS 32 at UC Irvine.  If I had more time, I would try \nto create a version with the heads of Walt and Jesse (from the\nshow "Breaking Bad") as pieces but maybe I can do that over the\nsummer.'''        

        message = tkinter.Label(
            master = self.about,
            text = message_pls,
            justify = tkinter.LEFT,
            font = DEFAULT_FONT2,
            background = DEFAULT_GRAY)

        message.grid(row = 1, column = 0,
                     sticky = tkinter.W, padx = 20)

        ok_button = tkinter.Button(
            master = self.about,
            text = 'Cool beans',
            font = DEFAULT_FONT2,
            command = self.about.destroy,
            highlightbackground = DEFAULT_GRAY)

        ok_button.grid(row = 2, column = 0,
                       sticky = tkinter.E, padx = 20, pady = 20)


    def show(self):
        ''' Shows Toplevel object when the "About" button is clicked. '''
        
        self.about.grab_set()
        self.about.wait_window()

        
class HelpPopup:

    def __init__(self):
        ''' Establishes Toplevel object, configures the aesthetics of the window
    and shows the user a message. '''
        
        self.help = tkinter.Toplevel()
        self.help.configure(background = DEFAULT_GRAY)
        self.help.wm_title('Help')

        help_label = tkinter.Label(
            master = self.help,
            font = DEFAULT_FONT0,
            text = 'Help',
            background = DEFAULT_GRAY)

        help_label.grid(row = 0, column = 0,
                        sticky = tkinter.W, padx = 20, pady = 20)

        help_message = '''If you're not sure how to play Othello, here's some basic rules.\nThe game also shows you possible moves as lightened discs if\nyou really need it.\n\nThere are two players, each signified with different colors.  Now,\nif your goal is to have the most discs by the end of the game,\nall you need to do is make as many "sandwiches" with your color\nas possible.  If you want to have the least discs by the end of the\ngame, try avoiding making large sandwiches.  You might make\nsandwiches in places you didn't even expect.\n\nIf a player cannot flip over any discs in their turn, the turn goes\nto the other player.\n\nHave fun!  (o^_^o)''' 

        help_message_label = tkinter.Label(
            master = self.help,
            font = DEFAULT_FONT2,
            text = help_message,
            justify = tkinter.LEFT,
            background = DEFAULT_GRAY)

        help_message_label.grid(row = 1, column = 0,
                          sticky = tkinter.W, padx = 20)

        thanks_button = tkinter.Button(
            master = self.help,
            font = DEFAULT_FONT2,
            text = 'Thanks',
            highlightbackground = DEFAULT_GRAY,
            command = self.help.destroy)

        thanks_button.grid(row = 2, column = 0,
                           sticky = tkinter.E, padx = 20, pady = 20)


    def show(self):
        ''' Shows Toplevel object when the "About" button is clicked. '''

        self.help.grab_set()
        self.help.wait_window()
        

class OthelloApplication:

    ### STARTING THE WINDOW

    def __init__(self):
        ''' Starts Tkinter root window, configures aesthetics of the root and
    Canvas object, binds events to functions that drive the game forward, and
    displays all the buttons that grab information from the sidebar. '''

        self._game_state = False
        self._discs = []
        self._root_window = tkinter.Tk()
        self._root_window.configure(background=DEFAULT_GRAY)
        self._root_window.wm_title('Othello, submitted by Katie Bui, #78495932')

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            background = '#337755',
            borderwidth = 0,
            width = 600,
            height = 600)

        self._canvas.grid(
            row = 0, column = 0, rowspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        self._canvas.bind('<Configure>', self.configure_grid)
        self._canvas.bind('<Button-1>', self.move_click)

        ### Buttons!

        buttons_frame = tkinter.Frame(
            master = self._root_window,
            background = DEFAULT_GRAY)

        buttons_frame.grid(row = 1, column = 1)

        help_button = tkinter.Button(
            master = buttons_frame,
            font = DEFAULT_FONT2,
            highlightbackground = DEFAULT_GRAY,
            text = "Help",
            command = self.launch_help)

        help_button.grid(row = 0, column = 0, pady = 10, padx = 10)

        about_button = tkinter.Button(
            master = buttons_frame,
            font = DEFAULT_FONT2,
            highlightbackground = DEFAULT_GRAY,
            text = "About",
            command = self.launch_about)

        about_button.grid(row = 0, column = 1, pady = 10, padx = 10)

        ok_button = tkinter.Button(
            master = buttons_frame,
            font = DEFAULT_FONT2,
            highlightbackground = DEFAULT_GRAY,
            text = "Let's play",
            command = self.ok_button_clicked)

        ok_button.grid(row = 0, column = 2, columnspan = 2,
                       sticky = tkinter.E, pady = 10, padx = 10)

        self.sidebar = EnterInfo(self._root_window)        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)


    def launch_help(self) -> None:
        ''' Launches Help popup when the "Help" button is clicked. '''
        
        help_popup = HelpPopup()
        help_popup.show()


    def launch_about(self) -> None:
        ''' Launches About popup when the "About" button is clicked. '''
        
        about = AboutPopup()
        about.show()


    def ok_button_clicked(self) -> othello.GameState:
        ''' Grabs all the information that was set in the sidebar and starts
    an Othello game. '''
        
        self.info_list = self.sidebar._get_all_info()
        self.sidebar._whose_turn.set('Game has started!\n')
        self.othelloGame = othello.GameState(self.info_list[0], self.info_list[1])
        self._game_state = True
        self.othelloGame.create_board()
        self.othelloGame.first_turn(self.info_list[2])
        self.othelloGame.initialize_discs(self.info_list[3])
        self._change_score()
        self.draw_grid()

    ### DRAWING THE GRID

    def configure_grid(self, event:tkinter.Event):
        ''' Clears canvas and redraws all discs when the window is resized. '''
        
        if self._game_state == True:
            self._canvas.delete(tkinter.ALL)
            self.draw_grid()
            
    
    def draw_grid(self):
        ''' Draws the grid and discs according to the number of rows and columns
    the user specifies and the current window size. '''
        
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for c in range(self.othelloGame._columns):
            self._canvas.create_line(c*(canvas_width/(self.othelloGame._columns)), 0, \
                                     c*(canvas_width/(self.othelloGame._columns)), canvas_height, fill='#225530')
        for r in range(self.othelloGame._rows):
            self._canvas.create_line(0, r*(canvas_height/(self.othelloGame._rows)), \
                                     canvas_width, r*(canvas_height/(self.othelloGame._rows)), fill = ('#225530'))
        self._get_intersections()
        self._draw_all_discs()


    def _refresh(self):
        ''' Clears canvas and redraws all discs every time a move is made;
    whether or not the canvas is resized.  This is to redraw the possible
    moves discs every time.'''
        
        if self._game_state == True:
            self._canvas.delete(tkinter.ALL)
            self.draw_grid()

    ### VALIDATING MOVES

    def move_click(self, event: tkinter.Event) -> None:
        ''' Decides what to do when someone clicks on the screen.  If the move
    is invalid, clicking will do nothing.  If the turn *after* the user who
    just clicked cannot make a move, then it will give the turn back. '''

        if self._game_state == True:

            try:
                movetuple = self._moved_here(event.x, event.y)
                
                if self.othelloGame.master_valid_before(self.othelloGame._turn):
                    self.othelloGame.flip(movetuple[-1], movetuple[0], movetuple[1])
                    self._refresh()
                    self._change_score()
                    self._change_turn()
                    self._winner()
                    self.othelloGame.master_invalid_after(self.othelloGame._turn)

            except othello.CannotMoveError:
                self.othelloGame.switch_turn()
                self._change_turn()
                self._winner()
                self._refresh()

            except othello.InvalidMoveError:
                pass

            except IndexError:
                pass

    def _moved_here(self, x = int, y = int) -> tuple:
        ''' Returns user's move as tuple of (column, row, turn) to put into
    Othello game logic '''

        if self._game_state == True:

            canvas_width = self._canvas.winfo_width()
            canvas_height = self._canvas.winfo_height()

            tuple_info = []
            for intersection in self._intersections:
                int_x, int_y = intersection
                if y < int_y:
                    tuple_info.append(int_y)
                    if x < int_x:
                        tuple_info.append(int_x)
                        break

            lower_right_corner = (tuple_info[-1], tuple_info[0])
            row_col = []
            
            for i in range(self.othelloGame._columns+1):
                if lower_right_corner[0] == (i*(canvas_width/self.othelloGame._columns)):
                    row_col.append(i)
                    break

            for i in range(self.othelloGame._rows+1):
                if lower_right_corner[1] == (i*(canvas_height/self.othelloGame._rows)):
                    row_col.append(i)
                    break
                
            return (row_col[0]-1, row_col[-1]-1, self.othelloGame._turn)


    def _get_intersections(self):
        ''' Stores the intersections of the current grid with a list of (x, y)
    pixel coordinates.  '''

        if self._game_state == True:
            canvas_width = self._canvas.winfo_width()
            canvas_height = self._canvas.winfo_height()
            self._intersections = []

            for w in range(self.othelloGame._columns+1):
                for h in range(self.othelloGame._rows+1):
                    self._intersections.append((w*(canvas_width/(self.othelloGame._columns)), \
                                               (h*(canvas_height/(self.othelloGame._rows)))))
                    
    ### DRAWING THE DISCS


    def _draw_all_discs(self):
        ''' Draws all the discs onto the canvas in accordance to the current
    window size. '''
            
        draw_these = []
        draw_these_possible = []
        board = self.othelloGame._board

        if self.sidebar._guide_choice.get() == 'yes':

            for rowcol in self._all_candidates():
                coord = (rowcol[0]+1, rowcol[1]+1, rowcol[2])
                draw_these.append(self._colrow_to_pix(coord))

        for column in range(len(board)):
            for row in range(len(board[0])):
                if board[column][row] != 0:
                    colrow = (row+1, column+1, board[column][row])
                    draw_these.append(self._colrow_to_pix(colrow))

        small_width = self._canvas.winfo_width()/(self.othelloGame._columns**2.2)
        small_height = self._canvas.winfo_height()/(self.othelloGame._rows**2.2)
        
        for discs in draw_these:
            if discs[4] == 1:
                self._canvas.create_oval(discs[0]+small_width, discs[1]+small_height, discs[2]-small_width, discs[3]-small_height,
                                         fill='#001711', outline = '#001711')
            elif discs[4] == 2:
                self._canvas.create_oval(discs[0]+small_width, discs[1]+small_height, discs[2]-small_width, discs[3]-small_height,
                                         fill='#BBEECC', outline = '#BBEECC')
            elif discs[4] == 0:
                self._canvas.create_oval(discs[0]+small_width, discs[1]+small_height, discs[2]-small_width, discs[3]-small_height,
                                         fill='#448866', outline = '#448866') 


    def _change_score(self) -> None:
        ''' Changes the score displayed in the sidebar to whatever the current
    score is. '''

        self.sidebar.p1_score.set(self.othelloGame.count_discs(1))
        self.sidebar.p2_score.set(self.othelloGame.count_discs(2))


    def _change_turn(self) -> None:
        ''' Changes the turn displayed in the sidebar. '''

        if self.othelloGame._turn == 1:
            self.sidebar._whose_turn.set(self.sidebar.p1_name.get() + '\'s turn')
        elif self.othelloGame._turn == 2:
            self.sidebar._whose_turn.set(self.sidebar.p2_name.get() + '\'s turn')

            
    def _colrow_to_pix(self, colrow: tuple) -> tuple:
        ''' Turns tuples with row, column, turn information into pixel
    coordinates for tkinter the discs to draw with. '''
        
        row, col, turn = colrow
        canvas_height = self._canvas.winfo_height()
        canvas_width = self._canvas.winfo_width()
        
        return ((col-1)*(canvas_width/(self.othelloGame._columns)),
                (row-1)*(canvas_height/(self.othelloGame._rows)), \
                col*(canvas_width/(self.othelloGame._columns)), \
                row*(canvas_height/(self.othelloGame._rows)), turn)


    def _all_candidates(self) -> list:
        ''' Makes a list of the spots in the grid that can be potential moves
    for a certain player to make '''
        
        candidates = []
        
        for column in range(len(self.othelloGame._board)):
            for row in range(len(self.othelloGame._board[0])):
                if self.othelloGame.master_flip(self.othelloGame._turn, column, row) != []:
                    candidates.append((row, column, 0))
              
        return candidates


    def _winner(self) -> None:
        ''' Displays who the winner is in the sidebar when there are no more
    valid moves to make. '''
        
        if self.othelloGame.are_there_no_valid_moves() == True:

            if self.othelloGame.judge_winner(self.info_list[-1]) == 'BLACK':
                self.sidebar._whose_turn.set(self.sidebar.p1_name.get() + ' wins!')
            elif self.othelloGame.judge_winner(self.info_list[-1]) == 'WHITE':
                self.sidebar._whose_turn.set(self.sidebar.p2_name.get() + ' wins!')
            else:
                self.sidebar._whose_turn.set("It's a draw.")

            self._game_state = False

    def start(self):
        self._root_window.mainloop()

if __name__ == '__main__':
    game = OthelloApplication()
    game.start()
