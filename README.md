# ♔♕♖Chess♗♘♙
Lucas Alejandro Boschin
📍 Argentina, Mendoza

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-LucasBoschinUM/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-LucasBoschinUM/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/39350fd956fd79caf8cc/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-LucasBoschinUM/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/39350fd956fd79caf8cc/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-LucasBoschinUM/test_coverage)

# 📝 Description
This is a project developed for the subject ‘Computing 1’ which consists of the creation of a chess game using Python. The game follows the official rules of chess, and allows players to enjoy games in a virtual environment, with the possibility of using a console interface.

# 📋 Requirements
- Python 3.x...
- 📚Library:

coverage==7.6.1 (included on requirements.txt)

ipdb==0.13.13 (included on requirements.txt)

# 🎮 Game
- Board: An 8x8 cell board with the standard initial configuration of pieces.
- Pieces: Traditional chess pieces are included: king, queen, rooks, bishops, knights and pawns.
- Playability: Players can move their pieces according to the official rules of chess, with move validation.
- Endgame: the game ends when one player runs out of pieces or both players decide to end the game.

# 🛠️ Characteristics
- Game Board: represented by an 8x8 matrix, with the initial positions of the pieces.
- Piece Moves: each type of piece follows its valid moves according to the rules of chess.
- Command Line Interface (CLI): allows you to play by entering commands in the console.

# 👨🏼‍💻 Execution
1- Clone repository:

git clone git@github.com:um-computacion-tm/ajedrez-2024-LucasBoschinUM.git / https://github.com/um-computacion-tm/ajedrez-2024-LucasBoschinUM.git

2- Install dependencies:

pip install -r requirements.txt

3- Play on console:

python3 game/cli.py