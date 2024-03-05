# crossword_puzzle_generator
Create application, that allows user to create their own crossword puzzles.

given options at time of start, a new window will be opened, showing the puzzle being created.
The user will provide an answer, and a clue. Separated by some spacer character for syntax.
The length of the answer will be extracted, and a row of equal length will be added to the puzzle window live, showing the puzzle grow as the user provides input. 

As the answer is given, the program will search for prior answers in the puzzle, for shared characters, and the new answer will be connected at a perpendicular view to the pre-existing space. 

The new answer may be written as column or row.
Future versions may include the ability to reconfigure retroactively to optimize the window size, in the form of each answer being able to share characters with multiple other answers.

Use a database to store the UniqueID, Answer, Corresponding Clue(s).length, CoordinatesX, CoordinatesY
