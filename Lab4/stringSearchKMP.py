def find(string, text):
    if string == "":
        return -1
    if text == "":
        return -1
    if len(string) > len(text):
        return -1
    results = []
    longest = [0] * len(string)
    j = 0
    makeArray(string, longest)
    i = 0
    while i < len(text):
        if string[j] == text[i]:
            j += 1
            i += 1
        if j == len(string):
            results.append(i - j)
            j = longest[j - 1]
        elif i < len(text) and string[j] != text[i]:
            if j != 0:
                j = longest[j - 1]
            else:
                i += 1
    if len(results) == 0:
        return -1
    else:
        return results


def makeArray(string, longest):
    length = 0
    i = 1
    while i < len(string):
        if string[i] == string[length]:
            length += 1
            longest[i] = length
            i += 1
        else:
            if length != 0:
                length = longest[length - 1]
            else:
                longest[i] = 0
                i += 1
