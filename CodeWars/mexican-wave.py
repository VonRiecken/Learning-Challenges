def wave(people = None):
    if people:
        wave = []

        for i in range(len(people)):
            if people[i] == " ":
                continue
            waved_word = ""
            for j in range(len(people)):
                if i == j:
                    waved_word += people[j].upper()
                else:
                    waved_word += people[j]
            wave.append(waved_word)

        return wave
    else:
        return []
