# Distance Measurement Using Stereo Cameras

The use of stereo cameras for measuring the distance of an object is a popular and effective method for obstacle avoidance and navigation in autonomous vehicles.

## Methods of Distance Measurement

There are two main methods for measuring distance:

### Active Method

The active method involves sending out signals (like lasers, ultrasound, or light) to measure the distance to an object. These sensors provide detailed information about the surroundings, which is useful in fields such as robotics and self-driving cars. However, active systems can be expensive.

### Passive Method

The passive method uses cameras to capture images and analyze them to calculate distances. This approach is a significant area of research in computer vision and is applied in fields such as robotics, virtual reality, and industrial automation. Passive methods are more affordable because they use low-cost cameras and can operate in various weather and lighting conditions.

A widely used passive technique is stereoscopic measurement, which involves using two cameras. By comparing the positions of an object in both camera images, the system can calculate the object's distance accurately.

## Single Camera vs. Stereo Cameras

Using a single camera is a common approach for creating 3D images. However, a single camera has limitations in determining the exact size or distance of objects, leading to some uncertainty in 3D reconstructions.

This limitation can be problematic for applications that require precise measurements, such as construction or mapping. To address this issue, a stereo camera setup, which uses two cameras, provides a solution. With two cameras, the system can accurately calculate distances and sizes, resulting in much better 3D reconstructions.

## Stereo Vision

In stereo vision, two cameras are configured to capture images of the same scene simultaneously. Each camera provides a 2D image from a slightly different angle. By comparing these two images, the system can determine the 3D details of the scene. This process involves matching points in the two 2D images to the same points in the real-world 3D scene, creating a 3D map of the area.

## Recent Research and Developments

Recent studies have explored using various vision sensors to measure object distances and sizes:

- **Fusion of Stereo and PMD Cameras**: A method combining stereo cameras with a PMD-camera (which measures distances using light) has been developed for mobile robots. This approach balances the strengths and weaknesses of each camera type, producing highly accurate 3D maps of the environment.

- **Error Reduction in Stereo Camera Systems**: Research has focused on reducing errors caused by camera movement in stereo setups. A real-time motion estimation technique was used to correct alignment errors, ensuring accurate 3D data even when the cameras shift.

- **Visual Ego-Motion Estimation for Self-Driving Cars**: A study on estimating a self-driving car's movement using multiple cameras showed that a mathematical method could accurately calculate the car's full movement (direction, speed, etc.). This method was validated with real-world data from a multi-camera system mounted on a car.

- **Using two webcams**: They used image processing techniques in a program written in Matlab to find the distance. However, their method wasn't very accurate and only worked under specific conditions, especially for short distances—anything less than 1.2 meters.

  while current methods for measuring distance are effective, they might not consider all factors that affect accuracy. The proposed method aims to improve this by using stereo vision to provide a more precise measurement by addressing the issues related to lens distance variations.


  ## STEREO IMAGE MEASUREMENT METHOD

  The two cameras were positioned on horizontal base with a distance of 15 cm from each 
  other. The experiment started by allowing the right camera (RC) to take the first picture and 
  left camera (LC) to take the second picture. In order to improve computational speed, images are converted from RGB to grayscale.

 ![image](https://github.com/user-attachments/assets/f2947a31-bbf5-4a7b-9a01-77deee66653c)

 They use trigonometry to calculate the distance D to the object. The formula is:

 ![image](https://github.com/user-attachments/assets/cdc566ac-4092-4970-a3b7-eaa210816b83)

where,
 B is the known distance between the two cameras.
 θ1 and θ2 are the angles the cameras see the object from.

![image](https://github.com/user-attachments/assets/0c42554c-89a7-4358-87d2-6361936f0911)

Result showed that it could detect up to 160 m. In the experiment, B=0.15 is the 15-cm lens distance setup, x0=600 is the pixel width, and is the pixel width, and θ=31.5 is the lens view angle.


