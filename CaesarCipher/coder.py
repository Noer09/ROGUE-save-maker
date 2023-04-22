# Caesar alphabet
alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a",
            "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y",
            "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "[",
            "]", "{", "}", "-", "_", "=", "+", "(", ")", "*", "&", "%", "$", "#", "@", "!", "?", "<", ">", ".", ",",
            ":", "^", " "]


def decode(string):
    """Return decoded Caesar cipher

    Decode a Caesar cipher by using a predefined alphabet

    Args:
        string (str): The Caesar cipher to be decoded

    Returns:
        string (str): Decoded version of the given Caesar cipher
    """
    return coder(string, False)


def encode(string):
    """Return encoded string using the Caesar algorithm

    Encode a string using the Caesar algorithm by using a predefined alphabet

    Args:
        string (str): The string to be encoded

    Returns:
    string (str): Encoded version of the given string as a Caesar cipher
    """
    return coder(string)


def coder(string=None, encoding=True):
    """Return encoded/decoded string using the Caesar algorithm

    Encodes or decodes a given string depending on whether

    Args:
        string (str): The string to be encoded/decoded
        encoding (bool): Encoding mode (default)

    Returns:
        string (str): Encoded/Decoded version of the given string
    """

    if len(string) is 0:
        return ""

    charred_array = [char for char in string]

    alphabet_len = len(alphabet)
    string_len = len(string)
    coded = ""

    for i, v in enumerate(charred_array):
        try:
            pos_in_alphabet = alphabet.index(v)
        except ValueError:
            print("ERROR: Caesar alphabet does not contain " + v + "!")
            continue

        move_by = string_len + (i * 4)
        if not encoding:
            move_by = -move_by
        moved_pos = (pos_in_alphabet + move_by) % alphabet_len

        while moved_pos < 0:
            moved_pos = ((moved_pos + alphabet_len) % alphabet_len)

        coded += alphabet[moved_pos]

    return coded