## Stereo Vision Setup

In stereo vision, two cameras are positioned horizontally with a known distance between them, referred to as the **baseline**. This setup mimics human binocular vision, allowing the system to perceive depth by comparing the images from both cameras.

When an object appears in front of the cameras, it will show up in slightly different positions in each image due to the difference in perspective. This difference is called **disparity**. The disparity is larger for objects that are closer to the cameras and smaller for objects that are farther away.

The cameras capture two images—one from the **left camera** and one from the **right camera**. These images are then compared to measure how far apart the object appears in both views. Using this difference, along with the known baseline (the distance between the cameras) and the cameras' **focal length**, we can calculate the distance of the object from the cameras.

### Key Terms:

- **Baseline**: The distance between the two cameras.
- **Disparity**: The difference in the position of the object in the two images. Larger disparities mean the object is closer, and smaller disparities mean the object is farther away.
- **Focal Length**: A property of the camera that helps in calculating the size and position of objects in the image.

## How Depth is Calculated

The basic idea behind stereo vision is that when the same object is seen from two slightly different perspectives (from the two cameras), the system can triangulate the object's position in 3D space. The position difference (**disparity**) between the two images is used to estimate how far away the object is from the cameras.

The object’s distance from the cameras is **inversely proportional to the disparity**. This means that if the object is very close to the cameras, the disparity will be large, and if it is far away, the disparity will be small.

## Practical Use

Stereo vision is widely used in various applications such as **autonomous vehicles**, **robotics**, and **3D mapping**. In autonomous cars, for example, stereo cameras can help measure the distance of nearby objects such as pedestrians or other vehicles, enabling the car to react appropriately by slowing down or steering away to avoid collisions.

By using the left and right images and the known properties of the cameras (baseline and focal length), depth information is calculated in real time, making stereo vision an efficient and reliable way to measure distances in a dynamic environment.

 
![image](https://github.com/user-attachments/assets/95e4ffa3-eef4-469e-9583-6d9f1ea73ab6)

![image](https://github.com/user-attachments/assets/105a17fc-47a2-4da1-b0a8-a193aee55679)

