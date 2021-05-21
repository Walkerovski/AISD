def find(string, text):
    if string == "":
        return -1
    if text == "":
        return -1
    if len(string) > len(text):
        return -1
    i = 0
    j = 0
    while i < len(text):
        while j < len(string):
            if text[i + j] != string[j]:
                break
            if j == len(string) - 1 and text[i + j] == string[j]:
                return i
            j += 1
        i += 1
    return -1
