from collections import Counter 

"""

To Practice using List, tuple
Dict ans Sets
@eltonaloys

"""


def anagram_lst(str1, str2):
    """ Function to check Anagrams """
    return sorted(str1.lower()) == sorted(str2.lower()) 



def anagrams_dd(str1, str2):
    """ Function to check Anagrams using Dictionary"""
    dd = {}
    for char in str1.lower():
        keys = dd.keys()
        if char in keys:
            dd[char] += 1
        else:
            dd[char] = 1
    for char in str2.lower():
        if char in keys:
            dd[char] -= 1
        else:
            return -1

    return dd     


def anagrams_cntr(str1, str2):
    """ Function to check Anagrams using Counter"""
    return Counter(str1.lower()) == Counter(str2.lower())


def covers_alphabet(sentence):
    """ Function for covering each alphabet characters in a give string"""
    d = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for a in sentence.lower().replace(" ", ""):
        d[a] = d[a] + 1

    return all(v > 0 for v in d.values())



def book_index(words):
    """ Function to return words and pages of a book index """

    new_lst = []
    for t in words: 
        for in_list in new_lst:
            if t[0] == in_list[0]:

                if t[1] not in in_list[1]:
                    for item in in_list[1]:
                        if item >= t[1]:
                            in_list[1].insert(in_list[1].index(item), t[1])
                            break
                    else:
                        in_list[1].append(t[1])
                break
        else:
            new_lst.append([t[0], [t[1]]])
    
    return sorted(new_lst)



        
                  


            
