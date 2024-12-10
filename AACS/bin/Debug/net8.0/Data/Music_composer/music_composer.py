from music21 import converter, instrument, note, chord, stream

def generate_music(style, tempo, duration):
  # Load a sample piece of music in the desired style
  sample_music = converter.parse("sample_music.mid")

  # Create a new stream to store the generated music
  generated_music = stream.Stream()

  # Extract musical elements from the sample music
  # ... (Implementation for extracting notes, chords, rhythms, etc.)

  # Generate new music based on the extracted elements and user input
  # ... (Implementation for composing new melodies, harmonies, and rhythms)

  # Set the tempo and duration of the generated music
  generated_music.makeNotation(tempo=tempo)
  generated_music.insert(0, note.Rest(duration=duration))

  # Return the generated music
  return generated_music