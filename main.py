# main driver for the program

def main():
    return 0

def parse_input( raw_string):
    # parse the input string, splitting at the '.' character, stopping at the first split
    answer, clue = raw_string.split('.', 1)
    #to save space on the answer, remove any spaces. No whitespace on the board
    # answer.strip()
    # answer.remove(" ")
    # answer = answer.replace( " ", "")
    # return answer, clue
    return Item( answer, clue)

class Item:
    def __init__(self, answer, clue) -> None:
        self.answer = answer # 
        self.clue = clue
        self.answer_lite = self.answer.replace( " ", "") #provide the version of the answer, with spaces removed. This is the version of the answer that will be cacluated and displayed on the table puzzle.
        self.ans_length = len( self.answer_lite) # calculate the length on the puzzle table