# Real-Time Single-Camera Vehicle Distance Measurement for Autonomous Vehicles


## Introduction
Autonomous vehicles need to maintain a safe distance from other vehicles to avoid collisions. This paper presents a method to measure the distance between vehicles (cars and motorbikes) using a single camera instead of multiple expensive sensors like radar or lidar.

### Key Concepts:
- **CNN Deep Learning**: Used for detecting and classifying vehicles in real-time.
- **Triangle Similarity & Pixel Comparison**: Techniques applied to estimate the distance of detected vehicles.

### Problem with Traditional Sensors:
- **Radar**: Struggles to differentiate between multiple objects and is expensive.
- **Lidar**: Performance drops in bad weather (rain, fog, etc.) and it’s also expensive.
- **Stereo Cameras**: Require complex calibration and are highly sensitive to positioning.

This method eliminates these issues by using just one camera, offering an accuracy of up to **94%** in all weather conditions, including day, night, and rain.

---

## Method
1. **Image Preprocessing**:  
   - Removes unnecessary parts like the sky, roads, and trees.
   - Image combinations are created through **augmentation** (blurring and darkening) to handle conditions like rain or night.
   
2. **Object Detection**:  
   - **CNN** classifies objects as either cars or motorbikes. The features are extracted and classified using deep learning methods.

3. **Distance Calculation**:  
   - Uses **triangle similarity** and **pixel ratios**.  
   - Formula to calculate focal length:  
   `F = (P × D)/W`  
     Where:
     - P = Apparent width (in pixels)
     - D = Distance between the camera and object
     - W = Known width of the object (e.g., car = 1.8m, motorbike = 0.7m).

---

## Results
### Experiment Setup:
- **Dataset**: 2,500 images of cars and motorbikes captured from Jakarta.
- **Model**: Trained using CNN **ResNet50** architecture.
- **Hardware**: Training done on a laptop with **NVIDIA GeForce 740M GPU** and **i5 CPU**.

### Distance Accuracy:
The method provides accurate distance measurements in various conditions:
- **Day**: 5.2m measured for a car at an actual distance of 5.5m.
- **Night**: 5.5m measured for a car at an actual distance of 5.3m.
- **Rain**: 5.0m measured for a car at an actual distance of 5.3m.

The overall accuracy across different conditions is **94%**.

---

## Conclusion
This paper shows that a single camera can accurately measure the distance between vehicles in an autonomous car system. By doing so, it reduces the need for expensive and complex sensors like lidar and radar, making it a cost-effective solution for real-time vehicle distance measurement.

### Future Work:
Future experiments will explore further improvements in image processing and the integration of this method into fully autonomous driving systems.
