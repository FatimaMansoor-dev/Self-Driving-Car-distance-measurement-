import cv2
import numpy as np
import time
from skimage.metrics import structural_similarity as ssim  
import astarsearch  
import traversal  

def main(image_filename):
    '''
    Returns:
    1 - List of tuples which are the coordinates for occupied grids.
    2 - Dictionary with information of paths.
    '''

    occupied_grids = []  # List to store coordinates of occupied grids
    planned_path = {}    # Dictionary to store information regarding path planning
    
    # Load the image and define the window width and height
    image = cv2.imread(image_filename)
    (winW, winH) = (60, 60)  # Size of individual cropped images

    obstacles = []  # List to store obstacles (black tiles)
    index = [1, 1]  # Starting point
    # Create a blank image
    blank_image = np.zeros((60, 60, 3), np.uint8)
    # Create an array of 100 blank images
    list_images = [[blank_image for _ in range(10)] for _ in range(10)]  # Array of list of images
    # Empty matrix to represent the grids of individual cropped images
    maze = [[0 for _ in range(10)] for _ in range(10)]

    # Traversal for each square
    for (x, y, window) in traversal.sliding_window(image, stepSize=60, windowSize=(winW, winH)):
        # If the window does not meet our desired window size, ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue

        clone = image.copy()
        # Format square for OpenCV
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        crop_img = image[y:y + winH, x:x + winW]  # Crop the image
        list_images[index[1]-1][index[0]-1] = crop_img.copy()  # Add it to the array of images

        # Calculate average color
        average_color_per_row = np.average(crop_img, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        average_color = np.uint8(average_color)  # Average color of the grids

        # Check if grids are colored (not majorly white)
        if any(i <= 240 for i in average_color):
            maze[index[1]-1][index[0]-1] = 1
            occupied_grids.append(tuple(index))  # These grids are termed as occupied_grids 

        # Check if grids are black in color
        if any(i <= 20 for i in average_color):
            obstacles.append(tuple(index))  # Add to obstacles list

        # Show this iteration
        cv2.imshow("Window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)

        # Iterate
        index[1] += 1
        if index[1] > 10:
            index[0] += 1
            index[1] = 1

    # Get object list
    list_colored_grids = [n for n in occupied_grids if n not in obstacles]  # Grids with objects (not black obstacles)

    # Compare each image in the list of objects with every other image in the same list
    for startimage in list_colored_grids:
        key_startimage = startimage
        img1 = list_images[startimage[1]-1][startimage[0]-1]
        for grid in [n for n in list_colored_grids if n != startimage]:
            img = list_images[grid[1]-1][grid[0]-1]
            # Convert to grayscale
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Compare structural similarity
            s = ssim(gray1, gray2)
            # If they are similar
            if s > 0.9:
                # Perform A* search between both
                result = astarsearch.astar(maze, (startimage[1]-1, startimage[0]-1), (grid[1]-1, grid[0]-1))
                list2 = []
                for t in result:
                    x, y = t[0], t[1]
                    list2.append((x+1, y+1))  # Contains min path + startimage + endimage
                result = list(list2[1:-1])  # Result contains the minimum path required 

                if not result:  # If no path is found
                    planned_path[startimage] = ["NO PATH", [], 0]
                else:
                    planned_path[startimage] = [str(grid), result, len(result) + 1]

    for obj in list_colored_grids:
        if obj not in planned_path:  # If no matched object is found
            planned_path[obj] = ["NO MATCH", [], 0]            

    return occupied_grids, planned_path


def print_planned_path(planned_path):
    """Prints the planned path in a formatted way."""
    print("Planned Path:")
    for start, (end, path, length) in planned_path.items():
        if length > 0:
            print(f"From {start} to {end}:")
            print(f"  Path: {path}")
            print(f"  Path Length: {length}")
        else:
            print(f"From {start}: {end}")


if __name__ == '__main__':
    # Change filename to check for other images
    image_filename = "test_images/test_image1.jpg"
    occupied_grids, planned_path = main(image_filename)

    print("Occupied Grids:")
    print(occupied_grids)
    
    print_planned_path(planned_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
