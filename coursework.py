import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.']

def genRandText():
    """
    Randomly generates a string containing 62 characters comprising of a - z's, full stops and spaces.

    Returns
    __________
     
    S, string.
    """
    S = ''
    for i in range(62):
        S += random.choice(characters)
    return S


def score(S):
    """
    Each position of a string S is compared to the target T.

    Returns 
    __________

    score, integer.
    """
    T = "he who seeks rest finds boredom. he who seeks work finds rest."
    # If the following statement is false, the program should terminate
    assert len(S) == len(T)
    score = 0
    for i in range(62):
        if S[i] == T[i]:
            score += 1
    return score



def repetitions():
    """
    Repetedly generates strings and breaks if S occurs or iteration limit is reached.
    
    User Input
    __________

    Iteration limit, integer.

    Prints
    __________

    Best value, worst value and average scores, string.

    Returns
    __________

    All iteration scores, list

    """
    iteration_limit = int(input('Please state your desired iteration limit >> '))
    iteration_score = 0
    iteration = 0
    total_score = 0
    best_score = 0
    worst_score = 62
    average_score = 0
    all_iterations = []

    while iteration_score < 62 and iteration < iteration_limit:
        iteration += 1
        iteration_score = score(genRandText())
        total_score += iteration_score
        all_iterations.append(iteration_score)

        if iteration_score > best_score:
            best_score = iteration_score

        if iteration_score < worst_score:
            worst_score = iteration_score

    average_score = total_score / iteration

    print('Best score:', best_score, ', Worst score:', worst_score, ', Average score: ', average_score)

    return all_iterations
  

import matplotlib.pyplot as plt

scores = repetitions() 
iterations = range(1, len(scores) + 1)


plt.bar(iterations, scores)
plt.xlabel('Iteration')
plt.ylabel('Score')
plt.show()

def mutate(S):
    position = random.choice(range(62))
    new_character = random.choice(range(62))

    new_S = S[:position] + new_character + S[position +1:]

    return new_S


