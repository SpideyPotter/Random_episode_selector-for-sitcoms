# Random Episode Selector

A Python script to randomly select and play episodes from your favorite TV shows, especially great for sitcoms!

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Why It's Great for Sitcoms](#why-its-great-for-sitcoms)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Windows](#windows)
  - [macOS and Linux](#macos-and-linux)
  - [macOS Automator App](#macos-automator-app)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Future](#Future)

## Overview

Random Episode Selector is a Python script designed to enhance your TV show watching experience. It randomly selects and plays an episode from your TV show directory using VLC media player. The script is optimized for TV shows organized into season-wise subfolders within a main show folder.

## Features

- Randomly selects an episode from your TV show collection
- Prioritizes unwatched episodes for a fresh viewing experience
- Keeps track of watched episodes to avoid repetition
- Automatically opens the selected episode in VLC media player
- Works seamlessly on Windows, macOS, and Linux

## Why It's Great for Sitcoms

This script is particularly well-suited for sitcoms for several reasons:

1. **Non-linear viewing**: Most sitcoms don't require watching episodes in order, making random selection ideal.
2. **Quick entertainment**: Perfect for when you want a quick laugh without committing to a specific episode.
3. **Rediscovery**: Helps you rediscover forgotten episodes in long-running series.
4. **Mood-based watching**: Lets you enjoy your favorite show without the pressure of following a storyline.
5. **Binge-watching alternative**: Provides a more varied viewing experience compared to watching episodes sequentially.

## Requirements

- Python 3.x
- VLC media player installed
- TV show episodes organized in the following structure:
  ```
  TV_Show_Folder/
  ├── Season 1/
  │   ├── Episode1.mp4
  │   ├── Episode2.mp4
  │   └── ...
  ├── Season 2/
  │   ├── Episode1.mp4
  │   ├── Episode2.mp4
  │   └── ...
  └── ...
  ```

## Installation

1. Clone this repository or download the script to your TV show's main folder.
2. Ensure you have Python 3.x installed on your system.
3. Install VLC media player if you haven't already.

## Usage

### Windows

1. Save the `random_episode_selector.py` and `run_random_episode.bat` files in your TV show's main folder.
2. Double-click the `run_random_episode.bat` file to run the script.

### macOS and Linux

1. Save the `random_episode_selector.py` and `run_random_episode.sh` files in your TV show's main folder.
2. Open a terminal and navigate to your TV show's folder.
3. Make the shell script executable:
   ```
   chmod +x run_random_episode.sh
   ```
4. Run the script:
   ```
   ./run_random_episode.sh
   ```

### macOS Automator App

1. Open Automator and create a new "Application".
2. Add a "Run Shell Script" action.
3. Enter the following command, replacing `/path/to/your/script.py` with the actual path:
   ```
   python3 /path/to/your/script.py
   ```
4. Save the application in your TV show's main folder.
5. Double-click the Automator app to run the script.

## How It Works

1. The script scans the TV show folder and its season subfolders for video files.
2. It randomly selects an episode, prioritizing unwatched episodes.
3. The selected episode is opened in VLC media player.
4. The script updates a `watch_history.json` file to keep track of watched episodes.

## Customization

You can modify the `random_episode_selector.py` script to change:
- Supported video file extensions
- The media player used (currently set to VLC)
- The algorithm for selecting episodes

## Troubleshooting

- Ensure Python is installed and added to your system's PATH.
- Verify that VLC is installed in the default location or accessible via command line.
- Check that your folder structure matches the expected format.
- Make sure you have read and write permissions in the TV show folder.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/SpideyPotter/random-episode-selector/issues) if you want to contribute.

## Future
The following are possible updates:
- Add a clean GUI with an option of different TV-Series.When the TV series is pressed ,a random episode is shown.
- Give the episode as an option.
