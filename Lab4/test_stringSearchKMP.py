import stringSearchKMP
import stringSearchN
import random


def test_typicalKMP():
    text = "abcbabc"
    string = "cba"
    result = stringSearchKMP.find(string, text)
    assert(result == [2])


def test_multipleMatchesKMP():
    text = "abcbabc"
    string = "ab"
    result = stringSearchKMP.find(string, text)
    assert(result == [0, 4])


def test_emptyStringKMP():
    text = "abcbabc"
    string = ""
    result = stringSearchKMP.find(string, text)
    assert(result == -1)


def test_emptyTextKMP():
    text = ""
    string = "cba"
    result = stringSearchKMP.find(string, text)
    assert(result == -1)


def test_bothEmptyKMP():
    text = ""
    string = ""
    result = stringSearchKMP.find(string, text)
    assert(result == -1)


def test_longerStringKMP():
    text = "abcbabc"
    string = "cbaaaaaaaaa"
    result = stringSearchKMP.find(string, text)
    assert(result == -1)


def test_textIsStringKMP():
    text = "abcbabc"
    string = "abcbabc"
    result = stringSearchKMP.find(string, text)
    assert(result == [0])


def test_notInTextKMP():
    text = "abcbabc"
    string = "ddd"
    result = stringSearchKMP.find(string, text)
    assert(result == -1)


def test_randomKMP1():
    string = ""
    text = ""
    for i in range(10):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKMP.find(string, text)
    assert(result == expected)


def test_randomKMP2():
    string = ""
    text = ""
    for i in range(80):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKMP.find(string, text)
    assert(result == expected)


def test_randomKMP3():
    string = ""
    text = ""
    for i in range(2):
        string += random.choice(['a', 'b'])
    for i in range(100):
        text += random.choice(['a', 'b'])
    expected = stringSearchN.find(string, text)
    result = stringSearchKMP.find(string, text)
    assert(result == expected)
