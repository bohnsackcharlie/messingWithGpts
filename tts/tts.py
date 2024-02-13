from TTS.api import TTS
import wave
import simpleaudio as sa


def playSpeech():
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


# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

# Text to speech to a file
tts.tts_to_file(text="Hello world! It's nice to speak", speaker=tts.speakers[2], language=tts.languages[0], file_path="speech.wav")

playSpeech()