# main.py
from download import get_top_wholesome_video
from edit import process_video
# from publish import post_to_instagram  # Enable this when ready

VIDEO_PATH = "video.mp4"
FINAL_PATH = "final_video.mp4"

if __name__ == "__main__":
    url = get_top_wholesome_video()
    if url:
        print(f"Downloading: {url}")
        success = process_video(url, VIDEO_PATH, FINAL_PATH)
        if success:
            print("Video processed successfully!")
            # post_to_instagram(FINAL_PATH)  # Uncomment to enable
        else:
            print("Video processing failed.")
    else:
        print("No new video found.")