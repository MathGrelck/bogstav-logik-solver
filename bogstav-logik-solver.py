import sys, os


class BogstavLogikSolver():
    """
    Solves a "Bogstav Logik" puzzle in which you are given 7 words and 7 numbers. 
    Each number tells you how many letters in the corresponding word are present 
    in the "goal word". With this information, you must uncover the "goal word".

    The puzzle input must be provided as a path to a .txt file. 
    Example of file content:

    M,U,S,E,U,M
    B,A,M,B,U,S
    D,A,M,E,U,R
    M,O,S,E,E,G
    T,V,Æ,R,S,Ø
    T,A,G,R,Y,G
    B,O,G,O,R,M
    2,2,2,1,2,2,2

    The first seven rows are the seven words of the puzzle.
    The 8th row contains the numbers relating to each of the 7 words.
    Given that a solution exists, the result will be printed.
    """
    def __init__(self, puzzle_path):
        # Check if file exists
        if not os.path.exists(puzzle_path):
            raise SyntaxError("Puzzle does not exist. You wrote: "+puzzle_path)

        # Open the puzzle and assign the provided words and numbers to variables
        words = []
        with open(puzzle_path, 'r') as f:
            for word in f:
                word = [letter.strip() for letter in word.split(',')]
                words.append(word)
            number_of_letters = [int(number) for number in words[7]]
            words = words[0:7]

        # Transpose the puzzle. This way we can loop through all the letters of all words.
        # We will check for each "goal word" condidate whether it follows the constraint of the number of letters that must be present from each of the puzzle words. 
        # I hope this makes sense.
        # words_transpose = 
        # [['M', 'B', 'D', 'M', 'T', 'T', 'B'],
        #  ['U', 'A', 'A', 'O', 'V', 'A', 'O'], 
        #  ['S', 'M', 'M', 'S', 'Æ', 'G', 'G'], 
        #  ['E', 'B', 'E', 'E', 'R', 'R', 'O'], 
        #  ['U', 'U', 'U', 'E', 'S', 'Y', 'R'], 
        #  ['M', 'S', 'R', 'G', 'Ø', 'G', 'M']]
        
        words_transpose = list(map(list, zip(*words)))

        for word_1_letter in words_transpose[0]:
            for word_2_letter in words_transpose[1]:
                for word_3_letter in words_transpose[2]:
                    for word_4_letter in words_transpose[3]:
                        for word_5_letter in words_transpose[4]:
                            for word_6_letter in words_transpose[5]:
                                counts = [0]*7
                                q = 0
                                word_possible_solution = [
                                                word_1_letter,
                                                word_2_letter,
                                                word_3_letter,
                                                word_4_letter,
                                                word_5_letter,
                                                word_6_letter
                                ]

                                for letter in word_possible_solution:
                                    for p in range(7):
                                        if letter in words[p][q]:
                                            counts[p] = counts[p] + 1
                                    q = q + 1
                                
                                if counts == number_of_letters:
                                    print(' '.join(word_possible_solution))
                                    return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SyntaxError("Insufficient arguments.")
    if len(sys.argv) > 2:
        raise SyntaxError("Too many arguments.")
    BogstavLogikSolver(sys.argv[1]) # sys.argv[0] will be 'bogstav-logik-solver.py'
