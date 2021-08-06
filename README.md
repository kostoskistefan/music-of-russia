# Music of Russia [![version](https://img.shields.io/badge/version-1.0-red.svg)](https://semver.org)

**Music of Russia** is a python program designed to generate a song based on a user-selected note (key) by using Markov Chains. It uses one of the most common (Russian chanson) note movements, 1-4-5 with the addition of the 3rd and 7th chord (which is most commonly used in the chorus of Russian songs).

### Note
This script has only been tested on Arch Linux. 

## Requirements
* Python 3
* FluidSynth
* Python Modules:
  * Numpy
  * MIDIUtils
  * Midi2Audio

## Installation and Usage
Clone this repository - `git clone https://github.com/kostoskistefan/music-of-russia.git`

Change to the cloned directory - `cd music-of-russia`

Install the required python modules - `pip install -r requirements.txt`

Install fluidsynth with the package manager of your choice (for Arch Linux use - `pacman -S fluidsynth`).

Run the script - `python generator.py`

## Output
After running the script, you will find 3 generated files in the same directory as the script. 

* **txt** file - contains a list of the generated chords. 
* **wav** file - which you can open with any audio software and listen to the generated song. 
* **mid** file - contains your song in a MIDI format which can be opened in most DAWs or notation software.
