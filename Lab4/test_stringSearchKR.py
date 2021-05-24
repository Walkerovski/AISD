import stringSearchKR
import stringSearchN
import random


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


def test_randomKR1():
    string = ""
    text = ""
    for i in range(10):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKR.find(string, text)
    assert(result == expected)


def test_randomKR2():
    string = ""
    text = ""
    for i in range(80):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKR.find(string, text)
    assert(result == expected)


def test_randomKR3():
    string = ""
    text = ""
    for i in range(2):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKR.find(string, text)
    assert(result == expected)