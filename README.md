# Face Detection with Haar Cascade

A real-time face detection application using OpenCV's Haar Cascade classifiers.

## Overview

This project implements a real-time face detection system using a webcam and Haar Cascade classifiers from OpenCV. The application detects faces in the video feed, draws rectangles around them, and displays the count of detected faces. Histogram equalization is applied to improve face detection in varying lighting conditions.

## Features

- Real-time face detection from webcam
- Automatic download of cascade files if not present
- Face count display
- Histogram equalization for improved detection in varying light conditions
- Graceful error handling and webcam initialization

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Requests

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/face-detection-haar-cascade.git
cd face-detection-haar-cascade
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

To run the face detection application:

```
python src/face_detection.py
```

Or open and run the Jupyter notebook:

```
jupyter notebook notebooks/deteksi_lokal.ipynb
```

Press 'q' to exit the application while it's running.

## Project Structure

```
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   └── face_detection.py
└── notebooks/
    └── deteksi_lokal.ipynb
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV team for providing the Haar Cascade classifiers
- Computer vision community for tutorials and resources
