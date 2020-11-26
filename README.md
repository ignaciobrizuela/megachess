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
- The rules are the same as a in a regular chess, except that instead of crown a pawn in the opposite side of the board pawns crown in the middle squares.

- The board is 16x16 squares. So, now there are the quadruple of pieces.

![board](https://user-images.githubusercontent.com/40641262/100382354-f0e78900-2ff9-11eb-96c1-bbbecb35b228.png)

_This is a board picture_

- There is no check or checkmate.

- There are 100 moves for color, 200 in total.

- The game is over when one color capture all rival pieces o when the amount of movements reach 0.

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
This project is made by three parts. It has a Server which controls user accounts, matches, tournaments, etc. and the way to do it is sending and attending json requests.

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
This class transforms the board string into a matrix. This makes easier to locate each piece from the board.

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

Also this class has a method _get_pieces_from_board_ to list all pieces in the board and make them as attributes of the class.
So, if we create a board object we will have access to the matrix board and all pieces availables to play.

## Author ✒️

⌨️[IgnacioBrizuela](https://github.com/ignaciobrizuela)