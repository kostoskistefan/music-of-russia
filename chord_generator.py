import numpy as np

keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
possible_options = []


def generate_possible_options(key_index: int):
    options = []
    progression_indexes = [0, 5, 7, 10, 3]

    for i in range(len(progression_indexes)):
        current_index = (key_index + progression_indexes[i]) % 12
        options.append(keys[current_index])

    return options


def predict_next_state(note: str):
    global possible_options
    note_index = possible_options.index(note)

    probabilities = []

    if note_index == 0:
        probabilities.append(0.00)
        probabilities.append(0.50)
        probabilities.append(0.35)
        probabilities.append(0.10)
        probabilities.append(0.05)

    elif note_index == 1:
        probabilities.append(0.30)
        probabilities.append(0.00)
        probabilities.append(0.35)
        probabilities.append(0.20)
        probabilities.append(0.15)

    elif note_index == 2:
        probabilities.append(0.35)
        probabilities.append(0.40)
        probabilities.append(0.00)
        probabilities.append(0.10)
        probabilities.append(0.15)

    elif note_index == 3:
        probabilities.append(0.15)
        probabilities.append(0.15)
        probabilities.append(0.25)
        probabilities.append(0.00)
        probabilities.append(0.45)

    elif note_index == 4:
        probabilities.append(0.20)
        probabilities.append(0.10)
        probabilities.append(0.45)
        probabilities.append(0.25)
        probabilities.append(0.00)

    return np.random.choice(possible_options, p = probabilities)


def generate_sequence(chord: str, length: int = 30):
    original_chord = chord
    length -= 2

    global possible_options
    possible_options = generate_possible_options(keys.index(original_chord))

    chords = []
    chords.append(chord)

    for n in range(length):
        chords.append(predict_next_state(chord))
        chord = chords[-1]

    chords.append(original_chord)

    for chord in chords:
        if possible_options.index(chord) <= 1:
            chords[chords.index(chord)] += "m"

        elif possible_options.index(chord) == 2:
            chords[chords.index(chord)] += "7"

    return chords
