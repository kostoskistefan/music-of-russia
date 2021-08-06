import os
from midi2audio import FluidSynth
from chord_generator import generate_sequence, keys
from midi_generator import add_chord, midi_file


if __name__ == "__main__":
    key = input("Select the desired key for your song: ")

    if key not in keys:
        print("The key you have entered is not valid. Exiting...")
        exit(2)

    chord_progression = generate_sequence(key)

    for chord in chord_progression:
        add_chord(chord)

    with open("chord_progression.txt", "w") as output_file:
        output_file.write("\n".join(str(chord) for chord in chord_progression))

    with open("generated_song.mid", "wb") as output_file:
        midi_file.writeFile(output_file)

    fs = FluidSynth(os.path.realpath("soundfont.sf2"))
    fs.midi_to_audio(os.path.realpath("generated_song.mid"), os.getcwd() + "/generated_song.wav")