# Autonomous Vehicle with Emergency Braking System  
article link:https://www.mdpi.com/2076-3417/12/17/8458

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

# System Overview

This system plays a crucial role in making modern vehicles safer by preventing accidents or reducing their severity.

## Literature Review

The article presents a recognition model for the front wheel of the car which is dependent upon the backpropagation (BP) neural network and hidden Markov model. In this proposed system, the inputs include the brake pedal, accelerator pedal, and vehicle speed data, which are used to examine the driver’s intention. The AEB controller is designed with collision avoidance, driver characteristics, and ride comfort variables in mind. The variables used to build the state equation are the separation between the two vehicles, their relative velocities, and the ego vehicle’s velocities and accelerations.

Later, a new system was proposed to improve the tracking prediction, data association, and motion categorization of the previous system. It updated the previous motion and observation models to include active sensors and vision sensors. The vision module in the new system recognizes bikers, pedestrians, and cars and generates a vision target for them. Its purpose was to investigate the design and operation of an AEBS using the many fundamentals of mechanical and electronic engineering, commonly referred to as Mechatronics. An ultrasonic sensor combined with a stereo camera identifies an impediment in front of the car and provides information about the relative distances between the object and the vehicles in this system. The ECU will then determine whether or not an accident is likely to occur, and the brake will be deployed autonomously as a result of this approach. Time-to-collision (TTC) is one of the most extensively used time-based approaches presented and it was designed to evaluate the time it will take for an accident to occur between a preceding and a following vehicle.

![TTC Algorithm](https://github.com/user-attachments/assets/b5b10772-cbcd-4a30-a1e0-f5dd7e8fe991)

In Equation (1), `h` stands for the distance between the preceding and following vehicles, `VF` and `VP` stand for the speed of the following and preceding vehicles, and `L` stands for the length of the preceding vehicle. To address the shortcomings of the previous method, the researchers proposed new stopping distance-based algorithms (SDAs). Calculating a safe stopping distance is one of the most effective ways to monitor the possibility of a rear-end accident. SDA-based techniques for assessing rear-end collision risk are based on the assumption that in a car-following position, the leading car’s friction coefficient must be higher than the pursuing car’s. An overview of the SDA is shown below.

![Stopping Distance Algorithm](https://github.com/user-attachments/assets/22ca44ed-c9d2-419c-bc54-613cc8407ff9)

When you're driving and need to stop, if it takes you longer to react, the distance your car travels before stopping (called "thinking distance") increases. But if you can react quickly and make decisions faster, collisions can still happen, though at shorter reaction times.

Many researchers are using a new technology called Artificial Neural Networks (ANNs) to help cars avoid rear-end collisions. The benefit of ANNs is that they can handle very complex problems that are hard to predict, making them more useful than older methods that couldn't account for things like how long a person takes to react.

These researchers also created systems to help cars avoid crashes from different directions, not just from behind. They use neural networks and fuzzy logic to improve decision-making. Recently, they combined these methods with GPS data to make cars drive more safely on highways by accurately knowing their position and surroundings.

In short, ANNs help make cars smarter at avoiding crashes by solving complex, hard-to-see problems and using real-time data to make safer decisions.

## Specific Approaches

1. **[25]**: The authors created a system for Autonomous Emergency Braking (AEB) to protect pedestrians using radar and camera sensors. These sensors work together to track people and predict when a collision might happen. By calculating how fast the car is moving and how far it needs to stop, they made the system better at avoiding accidents. They tested these ideas using the EuroNCAP safety protocols.

2. **[26]**: They built an AEB system using MATLAB with two radar sensors: one for short-range and one for long-range detection. The system checks how quickly an obstacle (like a pedestrian) is detected and how fast the car is going.

3. **[27]**: Another system was proposed using stereo vision—two cameras spaced apart that watch the area. When a pedestrian is seen, the system calculates the stopping distance. If it's too short to stop safely, it automatically applies the brakes.

4. **[28]**: Lidar sensors (which measure distance with lasers) and infrared cameras (which detect heat) were used to make obstacle detection better, especially in bad weather. They tested this method using RC cars (small remote-controlled cars) to simulate how autonomous cars could avoid collisions with pedestrians.

5. **[29]**: Another system used ultrasonic sensors (eight in total) to detect different objects. The car operates normally until these sensors detect a potential danger, improving vehicle safety.

The authors noticed that older AEB systems often failed to spot pedestrians or vehicles in the dark or bad weather, and sometimes gave false alarms (false positives), which could cause disruptions or accidents.

In this paper, they propose a more reliable system that uses three types of sensors—radar, lidar, and vision—to improve accuracy. The system calculates stopping time and uses a better speed control method to avoid collisions. They also developed a smart algorithm to balance performance and prevent false alarms, making AEB more accurate and safer for pedestrians.


