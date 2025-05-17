# 📷 Hanimex 415 Revival – Raspberry Pi Camera Capture

Hanimex 415 Revival is a creative project that aims to resurrect the classic Hanimex 415 point-and-shoot camera, which became unusable due to the discontinuation of disc film, a crucial component for its operation. 
By using a Raspberry Pi Zero 2 and a custom Python script, this project merges modern electronics with vintage design, giving new life to forgotten hardware.
---

## 🛠 Project Overview

- **Original Camera Model:** Hanimex 415 (repurposed shell)
- **Core Components:** Raspberry Pi Zero 2 W, Raspberry Pi Camera Module
- **Programming Language:** Python
- **Key Libraries:** `opencv-python`, `os`, `datetime`

The script captures an image using the Raspberry Pi camera, automatically names the file using the current timestamp, and saves it in a directory named after the original camera — `HANIMEX-REV`.

---

## 🔧 Requirements

Make sure you have the following installed:

- Python 3
- Raspberry Pi OS
- Raspberry Pi Camera Module (enabled via `raspi-config`)
- Required Python packages:

```bash
pip install opencv-python
````

Optional but recommended:

* A button connected via GPIO for manual capture
* An LED indicator for capture feedback

---

## 🚀 How to Use

1. Connect your Raspberry Pi Camera Module to the Pi Zero 2.

2. Enable the camera using:

   ```bash
   sudo raspi-config
   ```

3. Clone or copy the project files to your Raspberry Pi.

4. Run the main script:

   ```bash
   python main.py
   ```

5. What happens:

   * The script checks if the directory `HANIMEX-REV` exists (creates it if not)
   * Captures an image from the camera
   * Displays the image in a preview window
   * Saves the image with a timestamped name, e.g., `17052025_142430HANIMEX-REV.jpg`

---

## 💡 Motivation

The **Hanimex 415** was a no-frills film camera known for its simplicity. With this project, the physical body of the Hanimex is reused, while its internals are modernized using a Raspberry Pi and a camera sensor.

---

## 📸 Planned Enhancements

* ✅ Script for image capture
* ⏳ Test compatibility with Raspberry Pi Zero 2
* ⏳ Validate camera module functionality
* ⏳ Add physical capture button via GPIO
* ⏳ Add LED status indicator (ready/capture)
* ⏳ Create flashable Pi image with pre-installed software
* ⏳ Full integration into Hanimex 415 camera body

---