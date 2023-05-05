from music21 import stream, note, chord, clef, key, meter, instrument, tempo
import random

def create_melody():
    pitches = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
    melody = [random.choice(pitches) for _ in range(8)]
    return melody

def create_piece():
    piece = stream.Score()

    # Instruments
    violin = stream.Part()
    violin.insert(0, instrument.fromString("Violin"))

    piano = stream.Part()
    piano.insert(0, instrument.fromString("Piano"))

    cello = stream.Part()
    cello.insert(0, instrument.fromString("Cello"))

    flute = stream.Part()
    flute.insert(0, instrument.fromString("Flute"))

    # Time signature
    time_sig = meter.TimeSignature('4/4')

    # Key signature
    key_sig = key.Key('G', 'major')

# Tempo
    tempo_mark = tempo.MetronomeMark(number=80)

    # Create multiple sections to extend the playtime
    num_sections = 8

    for _ in range(num_sections):
        # Melody
        melody = create_melody()
        for pitch in melody:
            violin.append(note.Note(pitch, quarterLength=1))

        # Harmony
        for chord_pitch in melody:
            piano_chord = chord.Chord([chord_pitch, 'G2', 'D3'])
            piano_chord.quarterLength = 1
            piano.append(piano_chord)

        # Cello line
        for bass_pitch in melody:
            cello_note = note.Note(bass_pitch.replace('5', '3'), quarterLength=1)
            cello.append(cello_note)

    # Flute solo
    flute_solo = create_melody()
    for pitch in flute_solo:
        flute.append(note.Note(pitch.replace('5', '4'), quarterLength=0.5))

    # Add time signature, key signature, and tempo
    for part in [violin, piano, cello, flute]:
        part.insert(0, time_sig)
        part.insert(0, key_sig)
        part.insert(0, tempo_mark)
        piece.insert(0, part)

    return piece

if __name__ == "__main__":
    piece = create_piece()
    piece.show('midi')
    piece.write('midi', fp='generated_piece.mid')
    piece.write('musicxml', fp='generated_piece.xml')

