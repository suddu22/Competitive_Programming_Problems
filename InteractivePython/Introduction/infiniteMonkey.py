import random
import string


def generate_str():
    # chars = "".join( [random.choice(string.lowercase + " ") for i in xrange(27)])

    alphabet = string.lowercase + " "
    res = ""
    for i in range(28):
        res += alphabet[random.randrange(27)]
    return res


def score_str(target, generated):
    numSum = 0.0
    for i in range(len(target)):
        if target[i] == generated[i]:
            numSum += 1
    return numSum / len(target)

if __name__ == '__main__':
    target = "methinks it is like a weasel"

    gen = generate_str()
    maxScore = 0
    tScore = score_str(target, gen)
    while gen != target:
        gen = generate_str()
        tScore = score_str(target, gen)
        if tScore > maxScore:
            print tScore, gen
            maxScore = tScore
