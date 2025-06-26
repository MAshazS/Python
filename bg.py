import tkinter as tk
from tkinter import messagebox
import chess 
from PIL import Image, ImageTk
import time
import random

class MainMenu:
    def __init__(self, root):
        # Initialize the main menu with a root window   
        self.root = root
        self.root.title("Game Menu")

        # Create a frame with dark background and padding

        frame = tk.Frame(
            root, 
            bg="darkslategrey", 
            padx=10, 
            pady=10
        )

        frame.pack(
            expand=True,
            fill=tk.BOTH
        )

        # Create and pack a label in the frame with the text "Welcome to the Games Menu"

        self.label = tk.Label(
            frame,
            text="Welcome to the Games Menu",
            bg="darkslategrey",
            fg="azure",
            padx=20,
            pady=40,
            font=("Comic Sans MS", 30),
        )
        self.label.pack(pady=20)

        tk.Label(frame,text="", bg="darkslategrey", padx=20, pady=40).pack()

        # Create and pack a login button with a command to show the login window

        self.login_button = tk.Button(
            frame,
            text="Login",
            font=("Comic Sans MS", 16),
            fg="blue",
            bg="mintcream",
            padx=20,
            pady=10,
            command=self.show_login,
        )
        self.login_button.pack()

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=15).pack()

        # ... (similar structure for signup and quit buttons)

        self.signup_button = tk.Button(
            frame,
            text="Sign Up",
            font=("Comic Sans MS", 16),
            fg="blue",
            bg="mintcream",
            padx=20,
            pady=10,
            command=self.show_signup,
        )
        self.signup_button.pack()

        # Create and pack a space label

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=15).pack()

        self.quit_button = tk.Button(
            frame,
            text="Quit",
            font=("Comic Sans MS", 16),
            fg="red",
            bg="mintcream",
            padx=20,
            pady=10,
            command=root.destroy,
        )
        self.quit_button.pack()
        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

    def show_login(self):

        # Create a new window for the login window

        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Decalre two gloval string variables for the username and password

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Create a frame in the login window

        frame = tk.Frame(login_window, bg="darkslategrey", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create and pack labels, entry widgets, and buttons for username and password entry

        tk.Label(
            frame,
            text="Username:",
            font=("Comic Sans MS", 16),
            fg="azure",
            bg="darkslategrey",
            padx=20,
            pady=10,
        ).pack()

        #Username entry label

        username_entry = tk.Entry(
            frame,
            textvariable=self.username_var,
            font=("Comic Sans MS", 16),
            fg="slategrey",
            bg="snow",
        )
        username_entry.pack()

        # Create and pack a space label

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

        tk.Label(
            frame,
            text="Password:",
            font=("Comic Sans MS", 16),
            fg="azure",
            bg="darkslategrey",
            padx=20,
            pady=10,
        ).pack()
        password_entry = tk.Entry(
            frame,
            textvariable=self.password_var,
            font=("Comic Sans MS", 16),
            fg="slategrey",
            bg="snow",
            show = "*"
        )
        password_entry.pack()

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

        #Create a Login Button that will proceed with command

        login_button = tk.Button(
            frame,
            text="Login",
            font=("Comic Sans MS", 16),
            fg="olive",
            bg="mintcream",
            padx=20,
            pady=10,
            command=lambda: self.login(login_window),
        )
        login_button.pack()
        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()
    
    def login(self,win):

        # Get the username and password from the entry widgets and convert them to strings

        username = self.username_var.get()

        #ADD A NEW LINE TO THE STRINGS

        username = username + "\n"

        password = self.password_var.get()

        #ADD A NEW LINE TO THE STRINGS

        password = password + "\n"

        #Check if the username and password are in the correct files and proceed to the game menu if they are

        if self.credentialCheck(username, password, "usernames.txt", "passwords.txt"):
            self.show_game_menu(username, password)   
            win.destroy()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def show_signup(self):

        # Create a new window for the signup window

        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")

        frame = tk.Frame(signup_window, bg="darkslategrey", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create and pack labels, entry widgets, and buttons for username and password entry

        self.newusername_var = tk.StringVar()
        self.newpassword_var = tk.StringVar()

        #Create and pack a label for the new username and password entry

        tk.Label(
            frame,
            text="Enter your new Username: ",
            font=("Comic Sans MS", 16),
            fg="azure",
            bg="darkslategrey",
            padx=20,
            pady=10,
        ).pack()

        username_entry = tk.Entry(
            frame,
            textvariable=self.newusername_var,
            font=("Comic Sans MS", 16),
            fg="slategrey",
            bg="snow",
        )
        username_entry.pack()

        #add a space label

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

        tk.Label(
            frame,
            text="Enter your new Password: ",
            font=("Comic Sans MS", 16),
            fg="azure",
            bg="darkslategrey",
            padx=20,
            pady=10,
        ).pack()

        password_entry = tk.Entry(
            frame,
            textvariable=self.newpassword_var,
            show="*",
            font=("Comic Sans MS", 16),
            fg="slategrey",
            bg="snow",
        )
        password_entry.pack()

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

        #Create a Register Button that will proceed with command

        signup_button = tk.Button(
            frame,
            text="Register",
            font=("Comic Sans MS", 16),
            fg="midnightblue",
            bg="mintcream",
            command=lambda: self.choose_games(signup_window),
        )
        signup_button.pack()

        #add a space label

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

    def signup(self, win, chess_choice, othello_choice,gta_choice):

        # Get the username and password from the entry widgets and assign them to strings

        username = self.newusername_var.get()
        password = self.newpassword_var.get()

        #Check if the username and password are in the correct files and proceed to the game menu if they are

        with open("usernames.txt", "a") as usernames:
            usernames.write(username + "\n")

        with open("passwords.txt", "a") as passwords:
            passwords.write(password + "\n")

        #Check if the username and password are in the correct files and show them the games if they are

        if chess_choice == 1:
            with open("ChessUsers.txt", "a") as chess_usernames:
                chess_usernames.write(username + "\n")

            with open("ChessUsersPasswords.txt", "a") as chess_passwords:
                chess_passwords.write(password + "\n")

        if othello_choice == 1:
            with open("OthelloUsers.txt", "a") as othello_usernames:
                othello_usernames.write(username + "\n")

            with open("OthelloUsersPasswords.txt", "a") as othello_passwords:
                othello_passwords.write(password + "\n")

        #destroy windows

        win.destroy()
        self.root.deiconify()

    def choose_games(self,win):

        # Create a new window for the choose games window

        choosegames_window = tk.Toplevel(self.root)
        choosegames_window.title("Choose Games")

        frame = tk.Frame(choosegames_window, bg="darkslategrey", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create integer variables to store as choices to buy the game or not

        chess_choice = tk.IntVar()
        othello_choice = tk.IntVar()
        gta_choice = tk.IntVar()

        win.destroy()

        # Create and pack checkbuttons

        c1 = tk.Checkbutton(
            frame,
            variable=chess_choice,
            text="Chess $69.99",
            font=("Comic Sans MS", 16),
            fg="crimson",
            bg="darkslategrey",
            onvalue=1,
            offvalue=0,
        )
        c1.pack()

        c2 = tk.Checkbutton(
            frame,
            variable=othello_choice,
            text="Othello $75.09",
            font=("Comic Sans MS", 16),
            fg="gold",
            bg="darkslategrey",
            onvalue=1,
            offvalue=0,
        )
        c2.pack()

        c3 = tk.Checkbutton(
            frame,
            variable=gta_choice,
            text="GTA 6 (Pre-Order) $99",
            font=("Comic Sans MS", 16),
            fg="lightcoral",
            bg="darkslategrey",
            onvalue=1,
            offvalue=0,
        )
        c3.pack()

        # Create a OK Button that will proceed with command

        ok_button = tk.Button(
            frame,
            text="Ok",
            font=("Comic Sans MS", 16),
            fg="midnightblue",
            bg="mintcream",
            command=lambda: self.signup(
                choosegames_window,
                chess_choice.get(),
                othello_choice.get(),
                gta_choice.get(),
            ),
        )
        ok_button.pack()

    def credentialCheck(self, userCred, userPass, usernameFile, passwordFile):
        # Check if the username and password are in the correct files and return True if they are and False if they aren't
        usernames = open(usernameFile, "r")
        passwords = open(passwordFile, "r")

        # Read the files and store them in lists

        userList = usernames.readlines()
        passList = passwords.readlines()

        if (userCred not in userList) or (userPass not in passList):
            return False
        else:
            indexUser = userList.index(userCred)
            indexPass = passList.index(userPass)
        if indexUser == indexPass:
            return True
        else:
            return False

    def show_game_menu(self, username, password):
        # Create a new window for the game menu window
        game_menu = tk.Toplevel(self.root)
        game_menu.title("Game Menu")

        frame = tk.Frame(game_menu, bg="darkslategrey", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        #Calls the credntialCheck function to check if the username and password are in the correct files

        if self.credentialCheck(
            username, password, "ChessUsers.txt", "ChessUsersPasswords.txt"
        ):
            tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()
            chess_button = tk.Button(
                frame,
                text="Chess",
                font=("Comic Sans MS", 16),
                fg="crimson",
                bg="mintcream",
                command=self.start_chess_game,
            )
            chess_button.pack()

        if self.credentialCheck(
            username, password, "OthelloUsers.txt", "OthelloUsersPasswords.txt"
        ):
            tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()
            othello_button = tk.Button(
                frame,
                text="Othello",
                font=("Comic Sans MS", 16),
                fg="royalblue",
                bg="mintcream",
                command=self.start_othello_game,
            )
            othello_button.pack()

        #loads the GTA button regardless of whether that is in the files or not

        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()
        gta6_button = tk.Button(
            frame,
            text="GTA 6, COMING OUT SOON...",
            font=("Comic Sans MS", 16),
            fg="saddlebrown",
            bg="mintcream",
            command=self.display_GTA_message,
        )
        gta6_button.pack()
        tk.Label(frame, text="", bg="darkslategrey", padx=20, pady=30).pack()

    def start_chess_game(self):

        # Create a new window for the chess game window

        chess_window = tk.Toplevel(self.root)
        chess_window.title("Chess Game")

        chess_game = ChessGame(chess_window)
        chess_game.start_chess_game()

    def start_othello_game(self):

        # Create a new window for the othello game window

        othello_window = tk.Toplevel(self.root)
        othello_window.title("Othello Game")
        othello_game = OthelloGame(othello_window)
        othello_game.start_othello_game()

    def display_GTA_message(self):

        # Create a GTA message window

        messagebox.showinfo(
            "GTA 6",
            "GTA 6 is coming out soon, stay tuned!" + "\n" + "Press X for doubt",
        )

class ChessGame:
    # This class is used to create the chess game window
    game_state = True
    def __init__(self, root):

        # Constructor to initialize the chess game

        self.root = root
        self.root.title("Chess Game")

        # Create a frame for the chess game with a crimson background

        frame = tk.Frame(root, bg="crimson", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        # Initialize chess board, squares, and selected square

        self.board = chess.Board()
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.selected_square = None

        # Load piece images for chess board

        self.piece_images = {}
        for piece_name in [
            "black_pawn",
            "black_rook",
            "black_knight",
            "black_bishop",
            "black_queen",
            "black_king",
            "white_pawn",
            "white_rook",
            "white_knight",
            "white_bishop",
            "white_queen",
            "white_king",
        ]:
            img_path = f"images/{piece_name}.png"
            self.piece_images[piece_name] = ImageTk.PhotoImage(
                Image.open(img_path).resize((64, 64))
            )

        # Create a canvas to draw the chess board and pieces

        self.canvas = tk.Canvas(frame, width=8 * 64, height=8 * 64, bg="black")
        self.canvas.pack()

        # Labels for turn, move, and timer

        self.turn_label = tk.Label(
            frame,
            text="White's Turn",
            font=("Comic Sans MS", 20),
            fg="azure",
            bg="crimson",
        )
        self.turn_label.pack()

        self.move_label = tk.Label(
            frame, text="", font=("Comic Sans MS", 16), fg="azure", bg="crimson"
        )
        self.move_label.pack()

        self.timer_label = tk.Label(
            frame,
            text="Timer: 00:00",
            font=("Comic Sans MS", 16),
            fg="azure",
            bg="crimson",
        )
        self.timer_label.pack()

        self.move_label = tk.Label(frame, pady=30, bg="crimson")
        self.move_label.pack()

        # Draw the chess board and pieces

        self.draw_board()
        self.draw_pieces()

        # Bind click event to canvas

        self.canvas.bind("<Button-1>", self.on_click)

        # Record start time and update the timer

        self.start_time = time.time()
        self.update_timer()
        

    def draw_board(self):

        # Draw the chess board on the canvas

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = "#F0D9B5"
                else:
                    color = "#B58863"
                self.canvas.create_rectangle(
                    col * 64, row * 64, (col + 1) * 64, (row + 1) * 64, fill=color
                )

    def draw_pieces(self):

        # Draw the chess pieces on the same canvas as the board

        piece_mapping = {
            chess.PAWN: "pawn",
            chess.ROOK: "rook",
            chess.KNIGHT: "knight",
            chess.BISHOP: "bishop",
            chess.QUEEN: "queen",
            chess.KING: "king",
        }

        for row in range(8):
            for col in range(8):
                piece = self.board.piece_at(chess.square(col, 7 - row))
                if piece is not None:
                    if piece.color == chess.BLACK:
                        color = "black"
                    else:
                        color = "white"

                    piece_type = piece_mapping.get(piece.piece_type, "")
                    if piece_type:
                        piece_name = f"{color}_{piece_type}"
                        self.squares[row][col] = self.canvas.create_image(
                            col * 64 + 32,
                            (7 - row) * 64 + 32,
                            image=self.piece_images[piece_name]
                        )

    def update_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.draw_pieces()

    def update_turn_label(self):
        if self.board.turn == chess.WHITE:
            self.turn_label.config(text="White's Turn", fg="seashell", bg="crimson")
        else:
            self.turn_label.config(
                text="Black's Turn", fg="darkslategray", bg="crimson"
            )

    def on_click(self, event):

        # Handle click event on the canvas/chess board

        col = event.x // 64
        row = event.y // 64
        square = chess.square(col, row)

        # Check if a square is selected or not

        if self.selected_square is None:
            self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            piece = self.board.piece_at(self.selected_square)

            # Handle pawn promotion when reaching the end of the board

            if (
                piece
                and piece.piece_type == chess.PAWN
                and chess.square_rank(square) in [0, 7]
            ):
                self.handle_pawn_promotion(square)
                self.selected_square = None
                self.update_turn_label()
                self.update_board()
                self.check_for_game_end()

            # Check if the move is legal

            elif move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.update_board()
                self.update_turn_label()
                self.move_label.config(
                    text=f"Legal Move: {move.uci()}",
                    font=("Comic Sans MS", 16),
                    fg="azure",
                    pady=10,
                )
                self.check_for_game_end()
            else:
                self.selected_square = None
                self.move_label.config(text="Illegal Move", fg="silver")
                messagebox.showinfo(
                    "Invalid Move", "This move is not valid. Try again."
                )
                self.root.deiconify()

    def handle_pawn_promotion(self, square):

        # Handle pawn promotion and choose the promoted piece

        promotion_choice = self.choose_promotion_piece()
        color = self.board.turn
        piece_mapping = {
            "queen": chess.QUEEN,
            "rook": chess.ROOK,
            "bishop": chess.BISHOP,
            "knight": chess.KNIGHT,
        }
        promoted_piece_type = piece_mapping[promotion_choice]
        promoted_piece = chess.Piece(promoted_piece_type, color)
        legal_moves = list(self.board.legal_moves)
        move = next(move for move in legal_moves if move.to_square == square)
        self.board.remove_piece_at(move.from_square)
        self.board.set_piece_at(square, promoted_piece)

        self.update_board()
        self.update_turn_label()
        self.move_label.config(text=f"Legal Move: {move.uci()}", fg="white")
        self.check_for_game_end()

        dummy_move = chess.Move.null()
        self.board.push(dummy_move)
        self.update_board()
        self.move_label.config(text=f"Legal Move: {move.uci()}", fg="white")
        self.update_turn_label()
        self.check_for_game_end()
        return move

    def choose_promotion_piece(self):

        # Display a dialog box to choose the piece to promote the pawn to and let the player choose the promoted piece in case of pawn promotion

        promotion_options = ["queen", "rook", "bishop", "knight"]

        promotion_dialog = tk.Toplevel(self.root)
        promotion_dialog.title("Pawn Promotion")

        frame = tk.Frame(promotion_dialog, bg="maroon", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        piece_type = tk.StringVar(promotion_dialog)
        piece_type.set("queen")

        # Create radio buttons for promotion options

        for option in promotion_options:
            tk.Radiobutton(
                frame,
                text=option.capitalize(),
                font=("Comic Sans MS", 16),
                fg="#B59410",
                bg="maroon",
                pady=10,
                variable=piece_type,
                value=option,
            ).pack()

        # Close the promotion dialog when the player clicks on the confirm button

        def confirm_promotion():
            promotion_dialog.destroy()

        fun_messages = [
            "Choose a Piece Wisely!!",
            "And he sacrfices....THE GAME",
            "Is the Queen the strongest piece in the game because it is the Queen, or is it the Queen because it is the strongest piece in the game?",
            "Always bet on the pawn",
            "Stand Proud, you're strong",
            "How did it feel, teaching Magnus Carlsen how to play the game?"
        ]

        # Display a fun message and a confirm button to choose the promoted piece

        tk.Label(
            frame,
            text=random.choice(fun_messages),
            font=("Comic Sans MS", 16),
            fg="#3c005a",
            bg="maroon",
            pady=30,
            padx=20,
        ).pack()

        tk.Button(
            frame,
            text="Confirm",
            font=("Comic Sans MS", 16),
            fg="#3c005a",
            bg="#80ff80",
            pady=10,
            command=confirm_promotion,
        ).pack()

        # Wait for the promotion dialog to close

        self.root.wait_window(promotion_dialog)
        
        return piece_type.get().lower()

    def check_for_game_end(self):

        # Check if the game has ended (checkmate or stalemate)

        if self.board.is_checkmate() or self.board.is_stalemate():

            self.show_game_over_message()

            self.timer_label.config(text="Game Over", fg="green")

            self.game_state = False

    def show_game_over_message(self):

        # Display a message indicating the winner or draw

        result = self.board.result()
        if result == "1-0":
            winner = "White"
        elif result == "0-1":
            winner = "Black"
        else:
            winner = "Draw"
        messagebox.showinfo("Game Over", f"The game is over!\nWinner: {winner}")

    def update_timer(self):

        # Update the game timer label

        elapsed_time = int(time.time() - self.start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        self.timer_label.config(text=f"Timer: {minutes:02d}:{seconds:02d}")
        if self.game_state:
            self.root.after(1000, self.update_timer)

    def start_chess_game(self):
        # Start the chess game
        # Start the main loop for the chess game

        self.root.mainloop()

class OthelloGame:
    def __init__(self, root):

        # Initialize the Othello game

        self.root = root
        self.root.title("Othello Game")
        self.current_turn = 0

        # Initialize the Othello board

        self.board = [[" "] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = "White"
        self.board[3][4] = self.board[4][3] = "Black"

        # Create a frame for the Othello game with a royalblue background

        frame = tk.Frame(root, bg="royalblue", padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create a canvas to draw the Othello board

        self.canvas = tk.Canvas(frame, width=400, height=400, bg="green")
        self.canvas.pack()

        # Labels for player turn, move status, and timer

        self.player_turn_label = tk.Label(
            frame,
            text="Player Turn: {}".format(self.current_player()),
            font=("Comic Sans MS", 16),
            fg = "white" if self.current_player() == "White" else "black",
            bg="royalblue",
            pady=10,
        )
        self.player_turn_label.pack()

        self.move_status_label = tk.Label(
            frame,
            text="Move Status: ",
            font=("Comic Sans MS", 16),
            bg="royalblue",
            pady=10,
        )
        self.move_status_label.pack()

        self.timer_label = tk.Label(
            frame,
            text="Timer: 00:00",
            font=("Comic Sans MS", 16),
            bg="royalblue",
            pady=20,
        )
        self.timer_label.pack()

        # Draw the initial Othello board

        self.draw_board()

        # Bind click event to canvas to draw the chess pieces

        self.canvas.bind("<Button-1>", self.on_click)

        # Record start time and start the timer

        self.start_time = time.time()
        self.timer_running = True

        self.update_timer()
    
    def current_player(self):
        # Determine the current player based on the turn number
        if self.current_turn % 2 == 0:
            return "Black"
        else:
            return "White"
        
    def draw_board(self):

        # Draw the Othello board on the canvas

        for row in range(8):
            for col in range(8):
                if self.board[row][col] == "Black":
                    fill_color = "black"
                elif self.board[row][col] == "White":
                    fill_color = "white"
                else:
                    fill_color = "green"
                x0, y0 = col * 50, row * 50
                x1, y1 = (col + 1) * 50, (row + 1) * 50
                self.canvas.create_rectangle(
                    x0, y0, x1, y1, fill="green", outline="black"
                )
                if self.board[row][col] == "White" or self.board[row][col] == "Black":
                    self.canvas.create_oval(
                        x0, y0, x1, y1, fill=fill_color, outline="green"
                    )

        # Highlight valid moves with small circles
        
        valid_moves = [
            (r, c) for r in range(8) for c in range(8) if self.is_valid_move(r, c)
        ]
        for r, c in valid_moves:
            x0, y0 = c * 50 + 25, r * 50 + 25
            if self.current_player() == "Black":
                self.canvas.create_oval(
                    x0 - 10, y0 - 10, x0 + 10, y0 + 10, fill="black", outline="black"
                )
            else:
                self.canvas.create_oval(
                    x0 - 10, y0 - 10, x0 + 10, y0 + 10, fill="white", outline="white"
                )
    
    def is_valid_move(self, row, col):

        # Check if a move is valid based on the current board state

        # Check if a move is valid for the current player

        if self.board[row][col] != " ":
            return False

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            flips = 0

            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != " ":
                if self.board[r][c] == self.opponent_player():
                    flips += 1
                else:
                    break

                r, c = r + dr, c + dc

            if (
                flips > 0
                and 0 <= r < 8
                and 0 <= c < 8
                and self.board[r][c] == self.current_player()
            ):
                return True

        return False
    
    def on_click(self, event):

        # Handle click event on the Othello board

        col = event.x // 50
        row = event.y // 50

        if self.is_valid_move(row, col):
            self.make_move(row, col)
            self.draw_board()
            self.update_game_status()

        else:
            self.move_status_label.config(text="Move Status: Invalid Move")
            messagebox.showinfo("Invalid Move", "This move is not valid. Try again.")

    def make_move(self, row, col):

        # Make a move on the Othello board and update the board state

        self.board[row][col] = self.current_player()

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            flips = 0

            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != " ":
                if self.board[r][c] != self.current_player():
                    flips += 1
                else:
                    break

                r, c = r + dr, c + dc

            if (
                flips > 0
                and 0 <= r < 8
                and 0 <= c < 8
                and self.board[r][c] == self.current_player()
            ):
                r, c = row + dr, col + dc
                for _ in range(flips):
                    self.board[r][c] = self.current_player()
                    r, c = r + dr, c + dc

        # Update turn and player turn label

        self.current_turn += 1
        self.player_turn_label.config(
            text="Player Turn: {}".format(self.current_player()),
            fg = "white" if self.current_player() == "White" else "black"

        )

    def update_game_status(self):

        # Update the game status based on the current board state
        # Update game status labels and check for game end conditions

        self.move_status_label.config(text="Move Status: Valid Move")

        if not any(self.is_valid_move(r, c) for r in range(8) for c in range(8)):
            self.timer_running = False
            self.update_timer()
            winner = self.get_winner()
            if winner:
                messagebox.showinfo("Game Over", "Player {} wins!".format(winner))
                self.timer_label.config(text="Timer: Game Over")
            else:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.timer_label.config(text="Timer: Game Over")

    def get_winner(self):

        # Check if the game has ended and return the winner
        # Determine the winner based on the number of black and white pieces

        black_count = sum(row.count("Black") for row in self.board)
        white_count = sum(row.count("White") for row in self.board)

        if black_count > white_count:
            return "Black"
        elif white_count > black_count:
            return "White"
        else:
            return None
    
    def opponent_player(self):

        # Get the opponent player of the current player

        if self.current_player() == "Black":
            return "White"
        else:
            return "Black"
        
    def update_timer(self):

        # Update the timer label every second

        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            self.timer_label.config(text=f"Timer: {minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)

    def start_othello_game(self):

        # Start the main loop for the Othello game

        self.root.mainloop()
        

if __name__ == "__main__": 
    # Check if this script is being run directly

    root = tk.Tk()
    # Create the main Tkinter window

    main_menu = MainMenu(root)
    # Create an instance of the MainMenu class
    
    root.mainloop()
    # Start the mainloop for the Tkinter window/application


