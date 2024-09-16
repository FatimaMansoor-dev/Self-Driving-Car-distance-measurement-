# Autonomous Vehicle with Emergency Braking System

## Overview
An **Autonomous Vehicle Emergency Braking System** (AEBS) detects potential collisions with cars or pedestrians ahead. It alerts the driver through visual and sound alarms. If the driver does not react in time, the system automatically applies the brakes to avoid an accident.

## Emergency Braking System
Modern emergency braking systems use sensors like **lidar**, **cameras**, and **radar** to detect obstacles. These sensors measure the distance between the vehicle and objects, and calculate their relative speeds. If a collision seems likely, the system applies the brakes automatically.

### How It Works
- **Sensors**: These systems scan the area in front of the car using ultrasonic, video, infrared, or radar sensors.
- **Collision Detection**: The AEBS constantly checks the distance between the vehicle and objects ahead. If the object is too close and the vehicle is moving too fast, the system activates the brakes.
- **Braking Control**: If the driver does not apply the brakes in time or doesn’t press hard enough, the system takes over and applies the brakes with the necessary force.

## Sensor Fusion
**Sensor fusion** combines data from multiple sensors (like cameras, radar, and lidar) to create a detailed and accurate view of the surroundings. Each type of sensor has strengths and weaknesses:
- **Radar**: Great at calculating distance and speed, works well in bad weather.
- **Cameras**: Good at recognizing objects (like cars or pedestrians) and reading signs but can struggle in poor conditions.
- **Lidar**: Very precise at detecting objects but expensive and limited in range.

![AEBS System Diagram](https://github.com/user-attachments/assets/67052d6c-516f-4164-838c-bba78505878d)

By combining data from all sensors, the AEBS provides a more reliable system for avoiding collisions.

## Key Benefits of AEBS
- **Collision Prevention**: Helps reduce or avoid accidents by automatically braking.
- **Improved Safety**: Reduces the impact of accidents if they occur.
- **Reliable Performance**: Combines data from different sensors to improve accuracy and safety.

This system plays a crucial role in making modern vehicles safer by preventing accidents or reducing their severity.
