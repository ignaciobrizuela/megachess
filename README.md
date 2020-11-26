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

## Author ✒️
---

⌨️[IgnacioBrizuela](https://github.com/ignaciobrizuela)