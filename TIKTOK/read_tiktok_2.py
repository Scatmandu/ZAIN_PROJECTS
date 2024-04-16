from pocketsphinx import Decoder
import moviepy.editor as mp

def extract_text_from_video(video_path):
    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Extract audio from the video
    audio = video.audio

    # Save the audio as a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path)

    # Initialize CMU Sphinx Decoder
    config = Decoder.default_config()
    config.set_string('-hmm', 'en-us')
    config.set_string('-lm', 'en-us.lm.bin')
    config.set_string('-dict', 'cmudict-en-us.dict')
    decoder = Decoder(config)

    # Process the audio file
    decoder.start_utt()
    stream = open(temp_audio_path, 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
    decoder.end_utt()

    # Get the decoded text
    decoded_text = decoder.hyp().hypstr

    return decoded_text

def save_text_to_file(text, output_file):
    with open(output_file, "w") as f:
        f.write(text)

if __name__ == "__main__":
    # Path to the TikTok video
    video_path = "Download.mp4"

    # Extract text from the video using CMU Sphinx
    extracted_text = extract_text_from_video(video_path)

    # Save the extracted text to a file
    output_file = "extracted_text.txt"
    save_text_to_file(extracted_text, output_file)

    print("Text extracted from the video has been saved to", output_file)
