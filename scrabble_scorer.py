# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}
simple_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  1: ['D', 'G'],
  1: ['B', 'C', 'M', 'P'],
  1: ['F', 'H', 'V', 'W', 'Y'],
  1: ['K'],
  1: ['J', 'X'],
  1: ['Q', 'Z']
}
vowel_bonus_point_structure = {
    1: ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z'],
    3: ['A','E','I','O','U','Y']
}
def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   users_word = input('Enter a word to score: ')
   return(users_word)



def simple_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in simple_point_structure:

            if char in simple_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

def vowel_bonus_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in vowel_bonus_point_structure:

            if char in vowel_bonus_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

def scrabble_scorer():
    return

scoring_algorithms = ({'Name':'Simple Score','Description': 'Each letter is worth 1 point.',"scorer_function":simple_scorer()},{'Name':'Bonus Vowels','Description': 'Vowels are 3 pts, consonants are 1 pt.',"scorer_function":vowel_bonus_scorer()},{'Name':'Scrabble','Description': 'The traditional scoring algorithm.',"scorer_function":old_scrabble_scorer()})

def scorer_prompt(word):
    print('Which scoring algorithm would you like to use?\n0 -' + scoring_algorithms[0]['Name'] + scoring_algorithms[0]['Description'] + '\n1 - ' + scoring_algorithms[1]['Name'] + scoring_algorithms[1]['Description'] + '\n2 - ' + scoring_algorithms[2]['Name'] + scoring_algorithms[2]['Description'])
    scorer_choice  = input('Enter 0, 1, or 2:')
    scorer_choice= int(scorer_choice)
    scoring_function = scoring_algorithms[scorer_choice]["scorer_function"]
    return scoring_function(word)

def transform():
    return

def run_program():
    word = initial_prompt()
    score = scorer_prompt(word)
    print.__format__(score)
