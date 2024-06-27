import os
import random
import subprocess
import json

def get_video_files(directory):
    video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.wmv')
    video_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(video_extensions):
                video_files.append(os.path.join(root, file))
    return video_files

def load_watch_history(history_file):
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return {}

def save_watch_history(history_file, history):
    with open(history_file, 'w') as f:
        json.dump(history, f)

def select_random_episode(episodes, watch_history):
    unwatched = [ep for ep in episodes if ep not in watch_history]
    if unwatched:
        return random.choice(unwatched)
    return random.choice(episodes)

def open_video_vlc(file_path):
    vlc_command = 'vlc'
    if os.name == 'nt':  # For Windows
        vlc_command = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
    subprocess.Popen([vlc_command, file_path])

def main():
    directory = os.getcwd()
    
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    history_file = os.path.join(directory, 'watch_history.json')
    watch_history = load_watch_history(history_file)

    episodes = get_video_files(directory)
    if not episodes:
        print("No video files found in the directory or its subdirectories.")
        return

    selected_episode = select_random_episode(episodes, watch_history)
    print(f"Opening episode: {os.path.basename(selected_episode)}")
    
    watch_history[selected_episode] = watch_history.get(selected_episode, 0) + 1
    save_watch_history(history_file, watch_history)

    open_video_vlc(selected_episode)

if __name__ == "__main__":
    main()
