# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [4.1.0] - 04-09-24
...

## [4.1.0] - 03-09-24
...

## [4.1.0] - 02-09-24
...

## [4.1.0] - 01-09-24
...

## [4.1.0] - 31-08-24
...

## [4.2.0] - 30-08-24
- The following changes were made on tests/test_pieces.py: Added module imports ; Created Board instance ; Added parameters in Piece constructor ; Added additional dependencies

## [4.1.0] - 29-08-24
- The following changes were made on tests/test_rook.py: Imports and dependencies changed ; Initial configuration changed ; more specific tests added ; Use of Board added
- Added "coverage.xml"

## [4.0.0] - 27-08-24
#--------------Primer Sprint----------------
- In ".coveragerc" changed source = main to source = game
- The following changes were made on tests/test_pieces.py: Changed access and support for private attributes ; Fixed potential bugs ; Changed naming conventions
- The following changes were made on tests/test_rook.py: Bugs fixed ; Initial settings changed in setUp ; Rook's initial position changed
- The following changes were made on tests/test_chess.py: Changed board initialization ; Added access to private attributes ; Changed dependency on Chess class ; Reduced potential test failures
- The following changes were made on game/class_rook.py: Added a constructor ; Added initialization of the color attribute in the constructor ; Extended and clarified the code
- The following changes were made on game/class_pieces.py: Added inheritance ; Added additional methods ; Added super() in Rook's constructor

## [3.6.3] - 26-08-24
- The following changes were made on game/class_rook.py: Modified the import module ; Added a __str__ method ; Added a string representation
- New methods added on game/class_chess.py

## [3.5.3] - 25-08-24
- The following changes were made on tests/test_board.py: Removed Rook class import ; Modified test configuration ; Modified test methods ; Removed private attribute accesses

## [3.4.2] - 24-08-24
- The following changes were made on tests/test_cli.py: Changed the number of tests ; Fixed the use of patch ; Added additional mocks ; Added assertions ; Added comments

## [3.3.1] - 23-08-24
The followings changes were made on game/class_board.py: Modified module import ; Added __str__ method, Added access to __positions__ in get_piece ; Added comments in piece initialization

## [3.2.1] - 22-08-24
- The following changes were made on game/cli.py code: The show_instructions function was removed ; The call to show_instructions was removed in the if __name__ == __main__: block ; The print(chess.show_board()) line in the play function was uncommented ; The print("Move successful!") message after a move is made was removed ; The instruction block explaining how to play was removed.

## [3.1.1] - 21-08-24
- game/exceptions.py was added

## [3.0.1] - 20-08-24
- .venv/ on .gitignore was added
- "changelog.md" was added
- Test added in tests/test_cli.py
- ".__Init__.py" in folders were changed to "__init__.py"
- "requirements.txt" was modified (added ipdb)
- In game/cli.py the module import and loop condition in main were modified
- Modified importing modules in the /game folder & /tests folder (example: from ClassPieces import Rook --> from game.class_pieces import Rook)
- Class names in /game have been changed (example: "ClassPawn.py" to "class_pawn.py")

## [3.0.0] - 19-08-24
- "Main.py" was added on /game ; then changed to "Cli.py" & "Main.py" was removed
- The import of modules in the /tests folder was changed from /clases to /game
- The name of /clases folder was changed to /game & then /clases was removed
- Settings in ".coverage" have been changed
- "README.txt" was removed and only "README.md" remained

## [2.5.0] - 18-08-24
- Added /tests folder with all corresponding tests (Module Name: /tests; with files: ".__Init__.py", "TestBoard.py", "TestChess.py", "TestPieces.py", "TestRook.py")

## [2.4.0] - 17-08-24
- Added /classes folder with all corresponding classes (Module Name: /clases; with files: ".__Init__.py", "ClassBoard.py", "ClassChess.py", "ClassPawn.py", "ClassPieces.py", "ClassRook.py")

## [2.3.0] - 16-08-24
- Configured and added "Dockerfile"

## [2.2.0] - 15-08-24
- Instructions added on "Main.py"

## [2.1.0] - 14-08-24
- "Main.py" added

## [1.1.1] - 13-08-24
- Changed "README.txt" to "README.md"
- ".gitignore" added (__pycache__/ & .coverage)
- CircleCI, Maintability, Test Coverage & CodeClimate badges added

## [1.0.0] - 12-08-24
- "requirements.txt" added (coverage==7.6.1)
- Configured and added ".coveragerc"
- Configured and added ".codeclimate.yml"
- Configured and added /.circleci on "config.yml"
- Configured and added CircleCI, Maintainability, Test Coverage on "README.txt"