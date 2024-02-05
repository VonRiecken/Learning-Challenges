def spin_words(sentence):
    new_sen = ""
    if " " in sentence:
        words = sentence.split()
        for word in words:
            n = len(word)
            new_sen += flip_letters(word, n)
            if word is not words[-1]:
                new_sen += " "
        print(new_sen)
        return new_sen
    else:
        return flip_letters(sentence, len(sentence))


def flip_letters(input, length):
    if length > 4:
        new_word = ""
        for i in range(length):
            new_word += input[(length - 1) - i]
        return new_word
    else:
        return input
