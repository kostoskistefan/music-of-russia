from os import getcwd
from os.path import realpath
from midi2audio import FluidSynth
from chord_generator import generate_sequence
from midi_generator import add_chord, midi_file


if __name__ == "__main__":
    key = input("Select the desired key for your song: ")
    chord_progression = generate_sequence(key)

    for chord in chord_progression:
        add_chord(chord)

    with open("generated_song.mid", "wb") as output_file:
        midi_file.writeFile(output_file)

    fs = FluidSynth(realpath("soundfont.sf2"))
    fs.midi_to_audio(realpath("generated_song.mid"), getcwd() + "/generated_song.wav")