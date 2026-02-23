### nts_mido_control.py - MIDI Random Arpeggiator (Python)
A Python-based MIDI Arpeggiator that generates algorithmic sequences. While optimized for the KORG Nu:Tekt NTS-1, it is compatible with any hardware or software synthesizer.

#### 🚀 Overview
The script creates a fast-paced, evolving arpeggio by combining a fixed scale with random octave jumps and real-time parameter modulation (Control Change).

#### Key Features
* Blues Minor Scale: Constrains notes to a blues-based pentatonic structure for a cohesive sound.
* Octave Shifting: Randomly selects between 4 octaves (-12, 0, 12, 24).
* Real-time Mod: Dynamically changes the Shape parameter (CC 54) on every note for shifting textures.
* KORG NTS-1 Ready: Pre-configured to select the "Waves" oscillator (CC 53) on startup.

#### 🛠️ Requirements
You will need Python 3.x and the mido library with a MIDI backend (like python-rtmidi).

#### 📖 Usage
Run the script with default settings (Port: "NTS", Channel: 1):

  ```bash
  python nts_mido_control.py
  ```
##### Custom Arguments
Specify your MIDI device name or channel via terminal flags:
  
  ```bash
  python nts_mido_control.py --port "YourDeviceName" --channel 2
  ```

#### 🎹 Technical Configuration
You can easily tweak these variables inside the script:

* Base Note: 53 (F3).
* Arp Speed: 0.15s per note (~400 BPM).
* Initial Setup: Sends a Control Change (CC 53) with value 72 to set the oscillator.
* Dynamic Shape: Sends a random value (0-127) to CC 54 before every note.

Tip: To stop the arpeggiator, press Ctrl + C. The script includes a safety handler to send a Note Off message, preventing "stuck" notes on your synthesizer
