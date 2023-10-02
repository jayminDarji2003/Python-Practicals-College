# create a python function to accept python function of dictionary and display the elements

def printDictionary(dict):
    for key in dict:
        print("KEY = ", key, " VALUE = ", dict[key])

dictionary = {
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd',
    5 : 'e',
    6 : 'f',
    7 : 'g'
}

printDictionary(dictionary)