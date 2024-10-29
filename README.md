# Video Duration Calculator

A Python script to calculate the total duration of video files within all folders in the current directory. This script automatically identifies folders containing video files, computes the combined duration of videos in each folder, and displays the results in hours, minutes, and seconds.

## Features
- Automatically detects all subfolders in the current directory and processes video files within each folder.
- Supports common video formats: `.mp4`, `.avi`, `.mkv`, `.mov`.
- Displays total duration in a readable format (hours, minutes, seconds).

## Requirements
- Python 3.x
- [moviepy](https://pypi.org/project/moviepy/) library for video processing

To install the required library, use:
```bash
pip install moviepy
```

## Usage
Place the script in a directory where subfolders contain your video files &
Run the script:
```bash
python video_duration_summary.py
```

The script will output the total duration of video files in each folder.
