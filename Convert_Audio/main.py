from moviepy import AudioFileClip
from moviepy import VideoFileClip
import os


def convert_ogg_to_mp3(input_file, output_file):
    try:
        clip = AudioFileClip(input_file)
        clip.write_audiofile(output_file, codec='mp3')
        print("Conversion completed successfully")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    input_file = "Demo.ogg"
    output_file = "Convertido.mp3"
    convert_ogg_to_mp3(input_file, output_file)
