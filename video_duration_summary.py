import os
from moviepy.editor import VideoFileClip

def get_total_video_duration(folder_path):
    total_duration = 0 
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')): 
            video_path = os.path.join(folder_path, filename)
            with VideoFileClip(video_path) as video:
                total_duration += video.duration 
    
    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600) // 60)
    seconds = int(total_duration % 60)
    return f"H: {hours}, M: {minutes}, S: {seconds}"

folder_paths = [folder for folder in os.listdir() if os.path.isdir(folder)]
for folder_path in folder_paths:
    print("Total duration of videos in {}: {}".format(folder_path, get_total_video_duration(folder_path)))