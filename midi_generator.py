from midiutil import MIDIFile

note_start_time = 0
track = 0
channel = 0
duration = 0.5
velocity = 127
tempo = 170

midi_notes = {
    "C":    48,
    "C#":   49,
    "D":    50,
    "D#":   51,
    "E":    52,
    "F":    53,
    "F#":   54,
    "G":    55,
    "G#":   56,
    "A":    57,
    "A#":   58,
    "B":    59,
}

midi_file = MIDIFile(1)
midi_file.addTempo(track, note_start_time, tempo)


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
        midi_file.addNote(track, channel, root_note, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 3, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 3, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        note_start_time += 1


def play_major_chord(root_note: int):
    global note_start_time

    for i in range(2):
        midi_file.addNote(track, channel, root_note, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        note_start_time += 1


def play_seventh_chord(root_note: int):
    global note_start_time

    for i in range(2):
        midi_file.addNote(track, channel, root_note, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 10, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note - 5, note_start_time, duration,  velocity)
        note_start_time += 1
        midi_file.addNote(track, channel, root_note + 4, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 7, note_start_time, duration,  velocity)
        midi_file.addNote(track, channel, root_note + 10, note_start_time, duration,  velocity)
        note_start_time += 1
