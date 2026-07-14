# Morse Code Translator — Audio Tone Generator

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![SoundDevice](https://img.shields.io/badge/SoundDevice-0.5-00ADD8?logo=python&logoColor=white)

A Python program that converts text messages to **Morse code** and plays the corresponding **audio tones** (sine wave beeps) through the computer's speakers.

## Features

- **Text-to-Morse Conversion** — complete A–Z and 0–9 dictionary
- **Audio Playback** — generates sine wave beeps for dots and dashes
- **Configurable Parameters** — sample rate (48kHz), frequency (880Hz), amplitude, duration
- **Interactive Loop** — type messages, hear Morse code in real time
- **Console Display** — shows the Morse code representation while playing
- **Punctuation Handling** — automatically strips punctuation, normalizes case

## Tech Stack

Python, numpy (sine wave generation), sounddevice (audio playback)

## Architecture

Single-file program (`main.py`):

```
WaveGen class
├── short_tone()    → dot (.) — short beep
├── long_tone()     → dash (-) — long beep
├── silence()       → gap between symbols
└── playsound()     → concatenates and plays full sequence

morse_dict()         → A-Z, 0-9 mapping to Morse symbols

Main loop:
  input → normalize → map to Morse → display → play audio
```

## Usage

```bash
pip install numpy sounddevice
python main.py
```

Type any message and hear it in Morse code. Press Ctrl+C to exit.
