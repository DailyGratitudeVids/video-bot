# edit.py
import subprocess
import os

def process_video(url, input_path, output_path):
    try:
        # Download
        subprocess.run(["yt-dlp", "-f", "mp4", "-o", input_path, url], check=True)

        # Crop + scale
        cropped_path = "cropped.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-i", input_path,
            "-vf", "crop=ih*9/16:ih,scale=1080:1920,setsar=1",
            "-t", "59", cropped_path
        ], check=True)

        # Transcribe with Whisper
        subprocess.run(["whisper", cropped_path, "--model", "base", "--output_format", "srt"], check=True)

        # Burn captions
        subprocess.run([
            "ffmpeg", "-y", "-i", cropped_path,
            "-vf", "subtitles=cropped.srt:force_style='FontSize=24'",
            output_path
        ], check=True)

        return True

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False
