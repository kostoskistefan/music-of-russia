import os
from common import keys
from midi2audio import FluidSynth
from chord_generator import generate_sequence
from midi_generator import add_chord, midi_file


if __name__ == "__main__":
    key = input("Select the desired key for your song (" + ' '.join(keys) +  "): ").upper();

    if key not in keys:
        print("The key you have entered is not valid. Exiting...")
        exit(2)

    chord_progression = generate_sequence(key)

    with open(os.getcwd() + "/output/chord_progression.txt", "w") as output_file:
        for chord in chord_progression:
            add_chord(chord)
            output_file.write(chord + '\n')
    
    with open(os.getcwd() + "/output/generated_song.mid", "wb") as output_file:
        midi_file.writeFile(output_file)

    fs = FluidSynth(os.path.realpath("soundfont.sf2"))
    fs.midi_to_audio(os.getcwd() + "/output/generated_song.mid", os.getcwd() + "/output/generated_song.wav")