import wave
import simpleaudio as sa

# Open the .wav file
wave_file = wave.open('speech.wav', 'rb')

# Get the audio data from the file
audio_data = wave_file.readframes(wave_file.getnframes())

# Get the sample rate and audio format
sample_rate = wave_file.getframerate()
sample_width = wave_file.getsampwidth()

# Close the .wav file
wave_file.close()

# Play the audio
play_obj = sa.play_buffer(audio_data, 1, sample_width, sample_rate)

# Wait until the playback finishes
play_obj.wait_done()