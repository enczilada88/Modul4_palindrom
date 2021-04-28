def if_palindrom(word):
    return word == word[::-1]

    """Function checks if given words is palindom
    Arguments:
        word {str} -- checked/given word
    Returns:
        bool -- True if the word is palindrom. Otherwise function returns False
    """
print(if_palindrom('kajak'))
print(if_palindrom('kajtekk'))