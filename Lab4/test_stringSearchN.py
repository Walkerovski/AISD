import stringSearchN


def test_typicalN():
    text = "abcbabc"
    string = "cba"
    result = stringSearchN.find(string, text)
    assert(result == [2])


def test_multipleMatchesN():
    text = "abcbabc"
    string = "ab"
    result = stringSearchN.find(string, text)
    assert(result == [0, 4])


def test_emptyStringN():
    text = "abcbabc"
    string = ""
    result = stringSearchN.find(string, text)
    assert(result == -1)


def test_emptyTextN():
    text = ""
    string = "cba"
    result = stringSearchN.find(string, text)
    assert(result == -1)


def test_bothEmptyN():
    text = ""
    string = ""
    result = stringSearchN.find(string, text)
    assert(result == -1)


def test_longerStringN():
    text = "abcbabc"
    string = "cbaaaaaaaaa"
    result = stringSearchN.find(string, text)
    assert(result == -1)


def test_textIsStringN():
    text = "abcbabc"
    string = "abcbabc"
    result = stringSearchN.find(string, text)
    assert(result == [0])


def test_notInTextN():
    text = "abcbabc"
    string = "ddd"
    result = stringSearchN.find(string, text)
    assert(result == -1)
