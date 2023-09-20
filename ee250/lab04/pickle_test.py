import pickle

notes = []

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
with open('mail.pickle', 'rb') as contents:
    notes = pickle.load(contents)

# B. Print out notes
print(notes)

# C. Read in a string from the user using input() and append it to notes
userInput = input("Write a string to add to notes: ")
notes.append(userInput)

# D. Save notes to notes.pickle
with open('mail.pickle', 'wb') as contents:
    pickle.dump(notes, contents, protocol = pickle.HIGHEST_PROTOCOL)

