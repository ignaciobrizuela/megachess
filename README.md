# Megachess 
_This is a challenge for EDA Talen Show, **EventBrite**._
The task is to build an AI which can play **Megachess**.

## About me
I'm Ignacio Brizuela Electronic Engineer and also a programmer. I've been programming for a couple of years as a self-oriented person, now I'm ready to take a challenge that lead me to another level.

## Tools
This challenge requires websockets and I chossed Python 3 to solve it.

* Websockets.
* Python 3.

## Rules
- The rules are the same as a in a regular chess, except that instead of crown a pawn in the opposite side of the board, pawns crown in the middle squares.

- The board is 16x16 squares. So, now there are the quadruple of pieces.

![board_matrix](https://user-images.githubusercontent.com/40641262/100924869-f47a8480-34bf-11eb-9d1b-45aa64367015.png)

- There is no check or checkmate.

- There are 100 moves for color, 200 in total.

- The game is over when one color capture all rival pieces, when the amount of movements reaches 0 or when a player reaches -220 score.

- Win who get more points.

### Piece points
- Queen:     _5_
- Horse:    _30_
- Bishop:   _40_
- Rook:     _60_
- Pawn:     _70_
- King:    _100_

- If there is a capture, the player scores 10 times the piece value captured. 

## Program structure
This project is made by three parts. There is a Server which controls user accounts, matches, tournaments, etc. 
The Server sends and attends json requests.

![program_flow](https://user-images.githubusercontent.com/40641262/100389612-9dcb0180-300c-11eb-9013-ca4a4b75c10d.png)

Our task it's to comunicate with the Server and play megachess matches. In order to do that, it is necessary to create an asyncronous client.
When a challenge is accepted the client interact with the bot player to plan moves and then send a json request to make the move.

## From json to play
The json request that the Server sends when is my turn to play is like:

```
{
    "event":"your_turn",
    "data":{
    "board_id":"2d348323-2e79-4961-ac36-1b000e8c42a5",
    "turn_token":"e40573bb-138f-4171-a200-66258f546755",
    "username":"your_username",
    "actual_turn":"white",
    "board":"rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR",
    "move_left":19, 
    "opponent_username”: “rival_username”
}
}
```

As it's shown, the board it's a string and also it is indicated what color of pieces I am. Therefore, my solution was to create classes to manipulate this data.

![classes - Copy](https://user-images.githubusercontent.com/40641262/100390930-b9d0a200-3010-11eb-92a6-636aaec78275.png)

### Board
This class transforms the board string into a matrix using numpy. This makes easier to locate each piece from the board.
E.g:
```
[rook rook horse horse ...]
[rook rook horse horse ...]
[pawn pawn pawn  pawn ...]
[...]
...
```

#### Board string
```
"rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
```

#### Board matrix
```
[['r' 'r' 'h' 'h' 'b' 'b' 'q' 'q' 'k' 'k' 'b' 'b' 'h' 'h' 'r' 'r']
 ['r' 'r' 'h' 'h' 'b' 'b' 'q' 'q' 'k' 'k' 'b' 'b' 'h' 'h' 'r' 'r']
 ['p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p']
 ['p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P']
 ['P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P']
 ['R' 'R' 'H' 'H' 'B' 'B' 'Q' 'Q' 'K' 'K' 'B' 'B' 'H' 'H' 'R' 'R']
 ['R' 'R' 'H' 'H' 'B' 'B' 'Q' 'Q' 'K' 'K' 'B' 'B' 'H' 'H' 'R' 'R']]
```

Also this class has a method _get_pieces_from_board_ to transform a string array into a pieces array.
So, if we create a board object we will have access to the matrix board and all pieces availables to play.

### Pieces
There is a father class with all attributes in common: _color, row, col_ (principal) and _points_move_, _points_been_captured_ (secondary). The color piece and its position are check when a new object is created in order to prevent posible errors such as: 'color that doesn't exists', 'row or col out of the board'.
* The attribute color is boolean, that means that it's only available create a white (True) or black (False) color piece.
* Rows and columns go from 0 to 15.
Then there are children classes which inherite from Pieces and they are: _Pawn, Horse, Bishop, Rook, Queen, King_.
E.g:
To create a black pawn it is necessary to instance a new Pawn object like this:
```
black_pawn = Pawn(False, 3, 0)
```
This is a black pawn is at row 3, col 0.
Other object classes are:
```
black_horse  = Horse(False, 0, 2)
black_bishop = Bishop(False, 1, 4)
black_rook   = Rook(False, 0, 0)
...
white_queen  = Queen(True, 14, 6)
white_king   = King(True, 15, 9)
```

These classes have a method to validate their movements:_valid_move(element_in_square)_.

#### valid_move(element_in_square)
This function receives a destiny piece and returns True if the main piece can jump or capture to that position, otherwise, it returns False.
E.g:
In this position, it is white turn.
![pawn_poss](https://user-images.githubusercontent.com/40641262/100926594-753a8000-34c2-11eb-974c-69cd31bc326b.png)
The posible moves to do for the pawn are: capture one of the pawn in its diagonal or jump foward. The rest of the movements are invalid for the pawn.
![pawn_poss_green](https://user-images.githubusercontent.com/40641262/100926757-b03cb380-34c2-11eb-9af9-156967e09950.png)
Asume that the white pawn is in row=8, col=8
The function to ask for a valid move is:
```
white_pawn.valid_move(black_pawn_left)
```

## Strategy
My strategy is quite simple.
![player2_flow](https://user-images.githubusercontent.com/40641262/101046182-98673d00-355f-11eb-9141-010179a3a027.png) 
After to create a board object, the AI player scan for all posible moves for both color. It depends on what color I am, my movements will be positives and the rival movements negatives.
E.g:
Given this board:
![board_case](https://user-images.githubusercontent.com/40641262/101047961-052f0700-3561-11eb-9b88-7d2dfe2b831a.png)
The posible moves are:
```
({'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 15, 'score': -8},       # bishop moves
{'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': -8},
{'from_row': 1, 'from_col': 14, 'to_row': 2, 'to_col': 13, 'score': -100},      # bishop captures pawn
{'from_row': 1, 'from_col': 14, 'to_row': 0, 'to_col': 13, 'score': -8},
{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15},     # pawn moves foward
{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0},      # paw captures bishop
{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0},      # king captures bishop
{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5},
{'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5},
{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5},
{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5},
{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5},
{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5})         # king moves
```
The most dangerous move that black pieces have is to capture white_pawn. In this moment make a move foward seems to be a nice move, but there is necessary to check how the board will be after each possible move for white pieces.
Every move has a different score and its scores depend the action made.
The most important thing is to create a Queen army, so the pawns will try to crown if they can. Also, it is important to defend valuable pieces. Even though a queen captured gives 50 points, the are extremely dangerous, so it is necessary to delete them if there is any possibility.
The final score is a sum of the movement score that the piece makes now plus the best move I will have after the move plus the best move the rival will have.
```
final_score = best_move_now * 2 + best_move_after + best_move_rival_after
```
Multiple best_move_now by 2 highlit the move, because if I have a chance to make a good move now I could lose if later.
Because of that, the result of call _evaluate_moves_ is:
```
[[{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 13, 'score': 60.15}, 60.3],
[{'from_row': 2, 'from_col': 13, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],    # pawn capture bishop
[{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 14, 'score': 40.0}, 145.15],    # king capture bishop
[{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 15, 'score': 5}, -29.85],
[{'from_row': 2, 'from_col': 14, 'to_row': 2, 'to_col': 15, 'score': 5}, -29.85],
[{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 15, 'score': 5}, -29.85],
[{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 14, 'score': 5}, -29.85],
[{'from_row': 2, 'from_col': 14, 'to_row': 3, 'to_col': 13, 'score': 5}, -29.85],
[{'from_row': 2, 'from_col': 14, 'to_row': 1, 'to_col': 13, 'score': 5}, -50.0]]
```
As it' shown, the best move is to capture the black bishop now. So, calling _best_move_ will get the move that leads to a better position for white pieces.

Finally the AI returns the best move as: _from_row, from_col, to_row, to_col_

## Author ✒️

⌨️[IgnacioBrizuela](https://github.com/ignaciobrizuela)