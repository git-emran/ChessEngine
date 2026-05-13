# Chess Engine

This is a chess engine written in python. The AI is designed to be a challenging and dynamic gameplay experience.

## Features

 1	Single-Player Mode: Play against an AI opponent with adjustable difficulty levels. 2	Interactive GUI: Drag and drop chess pieces with smooth animations.
 3	Move Validation: Ensures all moves comply with chess rules.
 4	Undo Functionality: Allows players to undo moves.
 5	Game Over Detection: Detects checkmate, stalemate, and draw conditions.
 6	Customizable Board: Option to change the appearance of the chessboard and pieces.


## How to Run

 1	Navigate to the project directory.
 2	Run the main script: python main.py
 3	The game window will open, and you can start playing.

## Game Controls

 1	Start a New Game: Select New Game from the menu.
 2	Make a Move: Click and drag a piece to the desired square.
 3	Undo a Move: Click the Undo button.
 4	Adjust AI Difficulty: Go to the settings menu and choose the desired difficulty level.

##  AI Logic

The AI uses the Minimax algorithm with alpha-beta pruning to determine the best moves. The depth of the search tree can be adjusted to change the difficulty level. At higher difficulties, the AI calculates several moves ahead, making it more challenging to defeat.

## Future Improvements

Multiplayer Mode: Support for online or local multiplayer.
Enhanced AI: Implementation of machine learning techniques for adaptive gameplay.
Mobile Version: Develop a mobile-friendly version for iOS and Android.
Game Analysis: Add a feature to analyze and provide feedback on completed games.
