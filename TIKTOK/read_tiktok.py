import moviepy.editor as mp
import speech_recognition as sr

def extract_text_from_video(video_path):
    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Extract audio from the video
    audio = video.audio

    # Save the audio as a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path)

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # Recognize speech from the audio file
    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return ""

def save_text_to_file(text, output_file):
    with open(output_file, "w") as f:
        f.write(text)

if __name__ == "__main__":
    # Path to the TikTok video
    video_path = "Download.mp4"

    # Extract text from the video
    extracted_text = extract_text_from_video(video_path)

    # Save the extracted text to a file
    output_file = "extracted_text.txt"
    save_text_to_file(extracted_text, output_file)

    print("Text extracted from the video has been saved to", output_file)
