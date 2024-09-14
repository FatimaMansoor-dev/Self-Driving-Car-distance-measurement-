# Depth Estimation using MiDaS 
## Overview

This project utilizes MiDaS (Monocular Depth Estimation) models to estimate depth from a video feed in real-time, which is critical in self-driving car systems. The model generates a **depth mask**—a 2D map where each pixel's intensity represents its distance from the camera, allowing the vehicle to understand its environment and detect obstacles.

## MiDaS and Depth Mask

- **MiDaS** is a state-of-the-art model that estimates depth from a single image. This project uses the small version (MiDaS v2.1) for faster inference, making it suitable for real-time applications.
- **Depth mask**: Each pixel in the depth mask represents the relative distance of objects in the scene, with brighter areas being closer and darker areas farther away.

## Importance in Self-Driving Cars

- **Obstacle detection**: Depth masks help self-driving cars identify objects and their proximity, crucial for collision avoidance.
- **Navigation**: Understanding the spatial layout of the environment aids in path planning and decision-making.
  
This approach enables real-time, efficient, and reliable depth perception, enhancing the safety and navigation capabilities of autonomous vehicles.
