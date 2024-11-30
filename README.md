# Object Detection with YOLOv5

This project implements a real-time object detection system using the YOLOv5 model. It captures video from a webcam, processes each frame to detect objects, and provides audio feedback on detected objects.

## Features

- Real-time object detection using YOLOv5
- Audio feedback for detected objects
- FPS (Frames Per Second) counter displayed on the video feed

## Requirements

To run this project, you need to have the following packages installed:

- Python 3.x
- PyTorch (version >= 1.7.0)
- OpenCV (version >= 4.1.2)
- NumPy (version >= 1.18.5)
- pyttsx3 (version >= 2.90)

You can install the required packages using pip:

bash
pip install -r requirements.txt


## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/PranitThombare/Vission-Assist
   cd Vission-Assist
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. The webcam will open, and the object detection will start. Press 'q' to exit the video feed.

## Code Structure

- `src/detector/object_detector.py`: Contains the `ObjectDetector` class for handling object detection.
- `src/utils/fps_counter.py`: Implements the `FPSCounter` class to track frames per second.
- `src/detector/position_analyzer.py`: Contains the `PositionAnalyzer` class to analyze the position of detected objects.
- `src/audio/speech_engine.py`: Implements the `SpeechEngine` class for providing audio feedback.
- `main.py`: The entry point of the application that initializes the object detector and handles video capture.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.



## Acknowledgments

- [YOLOv5](https://github.com/ultralytics/yolov5) for the object detection model.
- [OpenCV](https://opencv.org/) for computer vision functionalities.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech conversion.
