from chord_generator import generate_sequence
from midi_generator import play_chord, midi_file

if __name__ == "__main__":
    key = input("Select the desired key for your song: ")
    chord_progression = generate_sequence(key)

    for chord in chord_progression:
        play_chord(chord)

    with open("generated_song.mid", "wb") as output_file:
        midi_file.writeFile(output_file)
