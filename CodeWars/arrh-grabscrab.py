def grabscrab(said, possible_words):

    pir_counter = {}
    for char in said:
        if char in pir_counter:
            pir_counter[char] += 1
        else:
            pir_counter[char] = 1
    # print(pir_counter)

    word_counter = []
    for word in possible_words:
        dict_word = {}
        for char in word:
            if char in dict_word:
                dict_word[char] += 1
            else:
                dict_word[char] = 1
        word_counter.append(dict_word)
    # print(word_counter)

    list_words = []
    for i in range(len(word_counter)):
        if word_counter[i] == pir_counter:
            list_words.append(possible_words[i])

    # print(list_words)

    return list_words
