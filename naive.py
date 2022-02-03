"""
a naive wordle solution
Algorithm as follows:
    - guess a random answer from list
    - have user enter feedback
    - filter answer list
    - repeat
"""
# get the answers as a list
ans_file = open("answers.txt")
answers = ans_file.readlines()
ans_file.close()

# loop until we've got an answer
while len(answers) > 1:
    pass

# we're done... give an answer
print("solution: {}".format(answers))
