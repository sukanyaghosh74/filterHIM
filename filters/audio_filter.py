# filters/audio_filter.py
import whisper
from moviepy.editor import VideoFileClip
from filters.text_filter import contains_blocked_text

model = whisper.load_model("base")

def transcribe_audio(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, verbose=False, logger=None)
    result = model.transcribe(audio_path)
    return contains_blocked_text(result["text"])
