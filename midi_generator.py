from common import midi_notes
from midiutil import MIDIFile

note_start_time = 0
track = 0
channel = 0
duration = 0.5
velocity = 127
tempo = 200

midi_file = MIDIFile(1)
midi_file.addTempo(track, note_start_time, tempo)


def add_chord(chord: str):
    if "m" in chord:
        generate_midi(midi_notes.get(chord.split("m")[0]), 3)

    elif "7" in chord:
        generate_midi(midi_notes.get(chord.split("7")[0]), 4, 10)

    else:
        generate_midi(midi_notes.get(chord), 4)


def add_upper_chord_part(root_note: int, second_note_index: int, fourth_note_index: int = None):
    global note_start_time

    midi_file.addNote(track, channel, root_note + second_note_index, note_start_time, duration,  velocity)
    midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)

    if fourth_note_index:
        midi_file.addNote(track, channel, root_note + fourth_note_index, note_start_time, duration,  velocity)

    note_start_time += 1


def add_chord_bass_note(root_note: int):
    global note_start_time

    midi_file.addNote(track, channel, root_note, note_start_time, duration, velocity)
    note_start_time += 1


def generate_midi(root_note: int, second_note_index: int, fourth_note_index: int = None):
    global note_start_time

    for i in range(2):
        add_chord_bass_note(root_note)
        add_upper_chord_part(root_note, second_note_index, fourth_note_index)
        add_chord_bass_note(root_note - 5)
        add_upper_chord_part(root_note, second_note_index, fourth_note_index)
