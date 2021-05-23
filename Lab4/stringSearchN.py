def find(string, text):
    if string == "":
        return -1
    if text == "":
        return -1
    if len(string) > len(text):
        return -1
    i = 0
    j = 0
    results = []
    while i < len(text):
        j = 0
        while j < len(string):
            if i + j >= len(text):
                break
            if text[i + j] != string[j]:
                break
            if j == len(string) - 1 and text[i + j] == string[j]:
                results.append(i)
            j += 1
        i += 1
    if len(results) == 0:
        return -1
    else:
        return results
