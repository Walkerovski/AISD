import stringSearchKR


def test_typicalN():
    text = "abcbabc"
    string = "cba"
    result = stringSearchKR.find(string, text)
    assert(result == [2])


def test_multipleMatchesN():
    text = "abcbabc"
    string = "ab"
    result = stringSearchKR.find(string, text)
    assert(result == [0, 4])


def test_emptyStringN():
    text = "abcbabc"
    string = ""
    result = stringSearchKR.find(string, text)
    assert(result == -1)


def test_emptyTextN():
    text = ""
    string = "cba"
    result = stringSearchKR.find(string, text)
    assert(result == -1)


def test_bothEmptyN():
    text = ""
    string = ""
    result = stringSearchKR.find(string, text)
    assert(result == -1)


def test_longerStringN():
    text = "abcbabc"
    string = "cbaaaaaaaaa"
    result = stringSearchKR.find(string, text)
    assert(result == -1)


def test_textIsStringN():
    text = "abcbabc"
    string = "abcbabc"
    result = stringSearchKR.find(string, text)
    assert(result == [0])


def test_notInTextN():
    text = "abcbabc"
    string = "ddd"
    result = stringSearchKR.find(string, text)
    assert(result == -1)
