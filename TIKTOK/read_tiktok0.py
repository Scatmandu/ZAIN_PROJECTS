import os
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

def save_text_to_file(text, video_number, output_folder):
    output_file = os.path.join(output_folder, f"extracted_text_{video_number}.txt")
    with open(output_file, "w") as f:
        f.write(text)

if __name__ == "__main__":
    videos_folder = "videos"
    output_folder = "extracted_texts"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through every video in the "videos" folder
    for video_number, video_file in enumerate(os.listdir(videos_folder), start=1):
        video_path = os.path.join(videos_folder, video_file)
        
        # Extract text from the video
        extracted_text = extract_text_from_video(video_path)

        # Save the extracted text to a file
        save_text_to_file(extracted_text, video_number, output_folder)

        print(f"Text extracted from video {video_number} has been saved to extracted_texts folder.")
