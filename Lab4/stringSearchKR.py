def search(string, pattern):
    q = 1000000007
    d = 31
    P = [0]
    S = [0]
    D = [1]
    Answer = []

    for i in range(1, max(len(pattern), len(string)) + 1):
        D.append((d * D[i - 1]) % q)

    for i in range(1, len(string) + 1):
        S.append((S[i - 1] + D[i] * ord(string[i - 1])) % q)

    for i in range(1, len(pattern) + 1):
        P.append((P[i - 1] + D[i] * ord(pattern[i - 1])) % q)

    for i in range(len(pattern), len(string)):
        patternhash = P[len(pattern)]
        stringhash = ((S[i] - S[i - len(pattern)] + q) % q)
        patternhash *= D[i - len(pattern)]
        patternhash %= q
        if patternhash == stringhash:
            Answer.apped(str(i - 1))

    if not Answer:
        return -1
    return Answer
