# Hand Pose Estimation

This project demonstrates **real-time hand pose estimation** using [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) and **OpenCV** for video capturing and rendering. The code detects and tracks the hand landmarks, focusing on key points like finger tips and knuckles.

## Table of Contents

- [Demo Video](#demo-video)
- [About MediaPipe](#about-mediapipe)
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Notes](#notes)
- [Future Enhancements](#future-enhancements)

## Demo Video

Check out the working of the hand pose estimation in this demo video below:

[![Watch the video](https://img.youtube.com/vi/Krw_WpgB-X8/0.jpg)](https://youtu.be/Krw_WpgB-X8)

Alternatively, [click here to watch the video on YouTube](https://youtu.be/Krw_WpgB-X8).

## About MediaPipe

[MediaPipe](https://mediapipe.dev/) is a cross-platform machine learning framework for building complex and customizable pipelines for computer vision and other types of ML models.

In this task:
- **MediaPipe Hands** solution is used, which identifies 21 hand landmarks, making it useful for gesture recognition, AR/VR applications, and more.
- MediaPipe ensures fast and accurate hand tracking, even on lower-end devices.

## Project Overview

The **Hand Pose Estimation** project uses **MediaPipe Hands** to identify 21 landmarks per hand in real time. The landmarks are drawn on the webcam feed, allowing for interactive hand gesture recognition and tracking. This can serve as a foundation for building applications like:
- Gesture-controlled interfaces
- Virtual sign language translation
- Hand pose-based gaming

## Features

- Real-time hand landmark detection using **MediaPipe Hands**
- Ability to detect and draw 21 landmarks per hand
- Visualize important hand points like the **index finger tip**
- Support for detecting up to two hands simultaneously

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/DanialSoleimany/hand-pose-estimation.git
   cd hand-pose-estimation
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python mediapipe
   ```

3. Run the code:

   ```bash
   python hand_pose_estimation.py
   ```

## How It Works

1. The project initializes MediaPipe’s **Hands** model to detect hand landmarks.
2. It captures video frames from the webcam using **OpenCV**.
3. Each frame is processed to identify hand landmarks like the wrist, knuckles, and finger tips.
4. The detected hand pose is drawn on the video stream and displayed in real time.

## Notes

1. Press `q` to quit the webcam feed.
2. The project detects up to two hands at a time.
3. The index finger tip is marked with a blue circle and labeled in real time.
4. The image is flipped horizontally to give a mirror effect for a better user experience.

## Future Enhancements

1. Implement gesture recognition to perform specific actions based on hand signs.
2. Add multi-hand tracking for more complex interactions.
3. Optimize performance for mobile devices.
