import numpy as np
import sounddevice as sd 

class WaveGen():
    def __init__(self):
        self.sampleR = 48000 #Hz
        self.wavefreq = 880 #Hz
        self.amplitude = 0.2
        self.duration = .20 #sec

    def short(self):
        num_samples_short = int(self.sampleR*self.duration)
        tshort = np.linspace(start=0, stop=self.duration, num=num_samples_short, endpoint=False)
        sine_short = np.sin(2 * np.pi * self.wavefreq * tshort)
        wave_short = self.amplitude * sine_short
        return wave_short
    
    def long(self):
        duration_long = self.duration * 3 #seconds
        num_samples_long = int(self.sampleR*duration_long)
        tlong = np.linspace(0, duration_long, num_samples_long, endpoint=False)
        sine_long = np.sin(2 * np.pi * self.wavefreq * tlong)
        wave_long = self.amplitude * sine_long
        return wave_long
    
    def silence(self):
        duration_silence = self.duration * 0.05
        num_samples_silence = int(self.sampleR*self.duration)
        silence_array = np.zeros((num_samples_silence, 1), dtype=np.float32)
        return silence_array

def morse_dict():
    MORSE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ' ': ' ', ',':'', '.':''
    }
    return MORSE_DICT

def message():
    msg = input('Write a message to see it in morse code(type exit to quit):\n')
    return msg

wavegen = WaveGen()
samplerate = wavegen.sampleR
shortwave = wavegen.short()
longwave = wavegen.long()
silence = wavegen.silence()

# msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

morse = morse_dict()
while True:
    msg = message()
    msg = msg.replace('.','').replace(',','').upper()
    if msg.upper().strip() == 'EXIT': break
    morse_msg = [morse[C] for C in msg if C in morse]
    print('Playing back your morse code message:')
    for morse_char in morse_msg:
        print(morse_char, end=' ')
    print('')
    for morse_char in morse_msg:
        for morse_pulse in morse_char:
            if morse_pulse == '.':
                sd.play(shortwave, samplerate=samplerate)
                sd.wait()
            elif morse_pulse == ' ':
                sd.play(silence, samplerate=samplerate)
                sd.wait()
            else:
                sd.play(longwave, samplerate=samplerate)
                sd.wait()
                sd.play(silence, samplerate=samplerate)
                sd.wait()