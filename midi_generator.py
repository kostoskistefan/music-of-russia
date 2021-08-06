from midiutil import MIDIFile
from time import sleep

note_start_time = 0
track = 0
channel = 0
velocity = 127

midi_notes = {
    "C": 60,
    "C#": 61,
    "D": 62,
    "D#": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "G": 67,
    "G#": 68,
    "A": 69,
    "A#": 70,
    "B": 71,
}

midi_file = MIDIFile(1)
midi_file.addTempo(0, 0, 120)


def play_chord(chord: str):
    if "m" in chord:
        play_minor_chord(midi_notes.get(chord.split("m")[0]))

    elif "7" in chord:
        play_seventh_chord(midi_notes.get(chord.split("7")[0]))

    else:
        play_major_chord(midi_notes.get(chord))


def play_minor_chord(root_note: int):
    global note_start_time

    for i in range(2):
        midi_file.addNote(track, channel, root_note, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 3, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 3, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        note_start_time += 1


def play_major_chord(root_note: int):
    global note_start_time

    for i in range(2):
        midi_file.addNote(track, channel, root_note, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        note_start_time += 1


def play_seventh_chord(root_note: int):
    global note_start_time

    for i in range(2):
        midi_file.addNote(track, channel, root_note, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 10, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, 1, velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, 1, velocity)
        midi_file.addNote(track, channel, root_note + 10, note_start_time, 1, velocity)
        note_start_time += 1
