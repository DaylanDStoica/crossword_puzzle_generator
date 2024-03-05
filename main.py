# main driver for the program

def main():
    return 0

def parse_input( raw_string):
    # parse the input string, splitting at the '.' character, stopping at the first split
    answer, clue = raw_string.split('.', 1)
    #to save space on the answer, remove any spaces
    # answer.strip()
    # answer.remove(" ")
    answer = answer.replace( " ", "")
    return answer, clue