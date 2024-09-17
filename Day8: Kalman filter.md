# Kalman Filter's Role in Sensor Fusion:

Autonomous vehicles rely on many sensors (e.g., lidar, radar, cameras, GPS, IMUs) to gather information about the environment and the car’s motion (e.g., speed, position, acceleration). These sensors provide inputs that the vehicle's control system uses to make decisions, including when and how to apply the brakes.

### Problem with Raw Sensor Data:

Sensors often have noise or inaccuracies. For example, a radar might give slightly fluctuating readings of the distance to an object, or a GPS signal might be slightly off due to atmospheric interference.

### Kalman Filter for Sensor Fusion:

A Kalman filter can be used to combine data from multiple sensors, filter out the noise, and produce a more accurate estimate of the vehicle’s state (e.g., position, velocity, acceleration). This refined state estimate is crucial for making braking decisions, such as when to stop or how much force to apply to the brakes.
