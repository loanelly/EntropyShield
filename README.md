<img src="img/logo/logo.png" align="right" width="150px">


# EntropyShield

**Language:**  <a href="https://github.com/loanelly/EntropyShield/blob/main/README.md"><img src="img/Flags/EN1.png" height="21" align="center"/></a> <a href="https://github.com/loanelly/EntropyShield/blob/main/README_RU.md"><img src="img/Flags/result.png" height="26" align="center"/></a>

A professional hardware-based **True Random Number Generator (TRNG)** that harvests pure, unpredictable physical entropy from thermal/shot noise (avalanche breakdown in a reverse-biased p-n junction). 

The system features an embedded firmware core utilizing a cryptographic **Von Neumann Extractor** to eliminate hardware bias, coupled with a highly defensive Python client to securely deliver cryptographic keys (e.g., **AES-256**) to host applications.

---

## ⚡ Key Features

- **Quantum Physics Entropy Source:** Captures raw avalanche noise from a hardware transistor junction — immune to mathematical or AI/ML predictive analysis.
- **Von Neumann Debiasing:** Embedded real-time bit purging ensures an exact 50/50 statistical distribution of `0`s and `1`s.
- **Dual Operating Modes:** Preprocessor pre-compiled toggle allows effortless switching between browser-based **Wokwi Simulation** and high-speed **Physical Hardware Production**.
- **Production-Grade Client:** Python backend protected against serial stream corruption, auto-flushes buffers, and handles bad data safely.

---

## 📂 Repository Structure & Documentation Index

The repository follows a clean, professional architecture separating source code from assets and engineering specifications:

```text
├── src/
│   ├── arduino/
│   │   └── entropy_shield.ino      # Microcontroller firmware (C++) with Preprocessor Toggles
│   ├── python/
│   │   └── main.py                 # Safe COM-Port Host Client & Cryptographic Key Assembler
│   └── documentation/
│       ├── connection_guide.txt    # [EN/RU] Step-by-step physical circuit wiring matrix
│       ├── documentation_en.txt    # [EN] Exhaustive technical and mathematical report
│       ├── documentation_ru.txt    # [RU] Подробный научно-технический отчет по проекту
│       ├── wokwi_simulation.txt    # [EN/RU] Instant web-simulator direct links
│       └── schematic.png           # Visual circuit reference and operational wiring diagram
├── .gitignore                      # Multi-language build artifacts filter
└── README.md                       # Main documentation portal (This file)
```

For ultra-deep technical breakdowns, please refer directly to the dedicated files inside the **[src/documentation/](src/documentation/)** directory.

---

## 🔬 How It Works (High-Level Overview)

1. **The Chaos Stage:** A physical transistor (e.g., BC547) is subjected to reverse-bias voltage, creating an unpredictable avalanche breakdown of charge carriers.
2. **The Boost Stage:** An operational amplifier (LM358) scales microvolt-level physical fluctuations into solid 0V–5V logic bounds.
3. **The Purge Stage:** The Arduino samples the Least Significant Bit (LSB). The **Von Neumann Filter** inspects incoming bits in pairs:
   - `10` → Validated as `1`
   - `01` → Validated as `0`
   - `00` or `11` → Instantly dropped to kill hardware anomalies or power grid 50Hz hum.
4. **The Assembly Stage:** The Python script reads the processed stream, checks byte validity against hexadecimal matrixes, and formats the output into structural keys.

---

## 🚀 Installation & Setup Guide

### 1. Interactive Browser Testing (No Hardware Needed)
To instantly test the pipeline without buying components:
1. Open the direct link provided inside **[src/documentation/wokwi_simulation.txt](src/documentation/wokwi_simulation.txt)**.
2. Ensure `#define WOKWI_EMULATION_MODE true` is active at the top of the firmware code.
3. Click **Start Simulation** ⏱️. Open the built-in *Serial Monitor* on the bottom right to see the live high-entropy HEX output.

### 2. Flashing the Microcontroller Firmware
To deploy the project onto an actual hardware chip:
1. Connect your device (Arduino Nano / Uno / Pro Micro) to your workstation via USB.
2. Open **[src/arduino/entropy_shield.ino](src/arduino/entropy_shield.ino)** in Arduino IDE or PlatformIO.
3. Set the operation flag to production mode:
   ```cpp
   #define WOKWI_EMULATION_MODE false
   ```
4. Select the correct board model and COM-port, then hit **Upload**.

### 3. Setting Up the Python Cryptographic Client
The host python client handles secure collection from the system bus.

1. Navigate into your local project root and install the hardware communication layer:
   ```bash
   pip install pyserial
   ```
2. Open **[src/python/main.py](src/python/main.py)** and verify the `SERIAL_PORT` variable matches your operating system configuration:
   - **Windows:** `'COM3'`, `'COM4'`, etc.
   - **Linux / macOS:** `'/dev/ttyUSB0'`, `'/dev/ttyACM0'`
3. Execute the generator engine to harvest a secure 256-bit key:
   ```bash
   python src/python/main.py
   ```

---

## 🧱 Physical Assembly (Hardware Mode)

When transitioning to real-world deployment (`WOKWI_EMULATION_MODE false`), the hardware layer requires isolated amplification. 

Below is an abstract reference of the layout. For exact resistor values and safety decoupling parameters, consult the comprehensive **[src/documentation/connection_guide.txt](src/documentation/connection_guide.txt)**.

```text
 [12V/9V Rail] ───[100kΩ]───┐
                            │
                      (BC547 NPN) ───[Collector Floating 💨]
                            │
   [GND] ───────────────────┴───[100nF Cap]───► [LM358 Op-Amp] ───► Arduino [A0]
```
*A pre-rendered wiring blueprint is available for inspection at `src/documentation/schematic.png`.*

---

## 🛡️ License & Disclaimer
Distributed under the MIT License. This software and hardware reference architecture is developed strictly for educational, defensive security research, and personal cryptographic experimentation. 

***
<div align="center">
  <p>🛠️ <b><a href="https://github.com/LNL-Engineering">LNL-Engineering</a></b> — <i>Building secure architectures through physical entropy.</i></p>
  <p>📬 <b>Personal Profile:</b> <a href="https://github.com/loanelly">@loanelly</a></p>
</div>
