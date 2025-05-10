Playing Pokemon with Hand Gestures

1. Install pyboy using
  ```bash
    pip install pyboy 
  ```

2. Install pysdl2-dll using 
  ```bash
    pip install pysdl2-dll
  ```

3. Install other dependencies
  ```bash
    pip install open-cv cvzone pyautogui mediapipe
  ```

4. Download the Pokemon Red ROM at this link: https://www.emulatorgames.net/roms/gameboy-color/pokemon-red-version/

5. Run the .gb file using 'pyboy /path/to/filename.gb'

6. Run the code to start the webcam tracking and voila, you can now play Pokemon with finger gestures!
  ```bash
    python main.py
  ```

**Note:** Make sure that your IDE or text editor has permission to access your computer's camera, and that it has access to enter key commands on your system! Also, the pyboy window must be in focus for the gesture commands to work.

![Poke-vision-demo](Poke-vision-demo.gif)

**Credit to the creators of pyboy, cvzone, open-cv, and pyautogui for making this fun little project possible**
