"""

Learning list functions
@eltonaloys

"""

def list_copy(l):
    """ Copy of a list"""
    return [item for item in l]

def list_intersect(l1,l2):
    """ If the Items of list first and second are same"""
    return [item for item in l1 if item in l2]
    
def list_difference(l1,l2):
    """ If the items in first list is not in the second list"""
    return [item for item in l1 if item not in l2]

def remove_vowels(string):
    """ to delete a vowel """
    return "".join([character for character in string if character not in ['a','e','i','o','u','A','E','I','O','U']])

def check_pwd(password):
    """ Function to check condition of a password """
    return all([any(character.isupper() for character in password), any(character.islower() for character in password), password.endswith(('0','1','2','3','4','5','6','7','8','9',))])

def insertion_sort(l):
    """ The following function will do insertion sorting """
    result = []
    for item1 in l:
        if len(result) == 0:
            result.append(item1)
            continue

        for item2 in result:
            if item2 >= item1:
                result.insert(result.index(item2), item1)
                break
        else:
            result.append(item1)
    return result



