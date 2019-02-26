#__author__ = ritvikareddy2
#__date__ = 2019-02-25

import re

VOWELS = ('a', 'e', 'i', 'o', 'u')
PUNCTUATIONS = (',', '.', '!', '?')


def split_words(sentence):
    """
    split the given sentence into words on space and other punctuations and return list of words
    :param sentence: english sentence
    :type sentence: str
    :return: list of words
    :rtype: list
    """
    return sentence.split()


def split_punctuation(word):
    """

    :param word:
    :type word:
    :return:
    :rtype:
    """

    if word[-1] in PUNCTUATIONS:
        return word[:-1], word[-1]
    else:
        return word, ''


def is_capitalized(word):
    """
    returns True if word is starts with an upper case letter
    :param word: word
    :type word: str
    :return: true or false
    :rtype: bool
    """
    return word.istitle()


def starts_with_vowel(word):
    """

    :param word:
    :type word:
    :return:
    :rtype:
    """
    return re.match(r"^[aeiou]", word)


def change_word(word):
    """
    take the chars before the first vowel occurrence and append them to the end of the word
    :param word:
    :type word: str
    :return:
    :rtype: str
    """
    # consider y also as a vowel for words not containing any vowels
    match = re.search(r"[aeiouy]", word)

    match_index = match.start()

    match_char = word[match_index]
    prev_char = word[match_index - 1] if match_index > 0 else None

    # handle cases where y is to be considered a consonant and not a vowel and cases where 'qu'
    # is considered as a single syllable
    if (match_char == 'u' and prev_char == 'q') or (match_char == 'y' and match_index == 0):
        match_index += 1

    consonants = word[:match_index]
    return word[match_index:]+consonants


def add_prefix(word):
    """
    take the translated word and add 'ay' to the end
    :param word: word
    :type word: str
    :return: pig latin word
    :rtype: str
    """
    return word+'ay'


def get_translated_string(english_sentence):
    """
    return pig latin version of given english sentence
    :param english_sentence: english sentence
    :type english_sentence: str
    :return: pig latin sentence
    :rtype: str
    """
    eng_words = split_words(english_sentence)
    pg_words = []
    for word in eng_words:
        if word in PUNCTUATIONS:
            pg_words.append(word)
        else:
            # flag to keep track of capitalized words
            capitalize = is_capitalized(word)

            word = word.lower()

            # split word and save the punctuation if any
            word, punc = split_punctuation(word)

            # change the word based on whether it starts with a vowel or not
            translated_word = word if starts_with_vowel(word) else change_word(word)

            # add the 'ay' suffix to the translated word
            translated_word = add_prefix(translated_word)

            # add back the punctuation if any
            translated_word += punc

            # capitalize the translated word if original word was capitalized
            translated_word = translated_word.capitalize() if capitalize else translated_word

            pg_words.append(translated_word)

    return ' '.join(pg_words)


# print(get_translated_string('quiet yellow sty Hello, my name is Alice.'))