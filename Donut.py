import math
import sys
import time

def move_cursor_to_top():
    """
    Moves the cursor to the top of the console.
    This function uses an escape sequence to move the cursor to the top of the console.
    It ensures that the new frame overwrites the previous one, creating the illusion of animation.
    """
    sys.stdout.write("\x1b[H")
    sys.stdout.flush()

def draw_donut(A):
    """
    Draws a frame of the rotating donut.
    
    Parameters:
    A (float): The angle of rotation.

    The function works as follows:
    1. Initialize buffers:
       - `z_buffer` is used to store depth information for each point on the donut to determine which parts are visible.
       - `b` is used to store characters that will form the donut's image.
       - `luminance_chars` contains characters that represent different levels of brightness.
    2. Iterate over angles `i` and `j` to cover the surface of the donut:
       - The outer loop iterates over the angle `j`, representing the circle around the donut.
       - The inner loop iterates over the angle `i`, representing the tube of the donut.
    3. Calculate 3D coordinates:
       - For each combination of `i` and `j`, calculate the 3D coordinates (`x`, `y`, `z`) using trigonometric functions.
       - `i` and `j` are angles in radians, and the calculations use sine and cosine functions.
    4. Apply rotation around the Y-axis:
       - The 3D coordinates are rotated by angle `A`.
       - The new coordinates (`x_prime`, `z_prime`) are computed using the rotation formulas:
         - x_prime = x * cos(A) + z * sin(A)
         - z_prime = -x * sin(A) + z * cos(A)
    5. Calculate the depth:
       - Calculate the depth value `D` to create a perspective effect:
         - D = 1 / (z_prime + 5)
       - This ensures that points farther from the viewer appear smaller.
    6. Project 3D coordinates to 2D:
       - Project the 3D coordinates onto a 2D plane:
         - xp = 40 + 30 * D * x_prime
         - yp = 12 + 15 * D * y
       - The resulting 2D coordinates (`xp`, `yp`) are used to find the position in the console buffer (`o`).
    7. Calculate luminance:
       - Calculate the brightness of each point using a formula considering the angles and rotations.
       - Clamp the result to ensure it is within the valid range of `luminance_chars`.
    8. Update buffers:
       - If the current point is closer to the viewer than any previously rendered point at the same screen position, update the `z_buffer` and `b` arrays.
       - This ensures that only the visible parts of the donut are rendered.
    9. Print the frame:
       - Move the cursor to the top of the console.
       - Print the contents of the `b` array to the console, forming the frame of the donut.
    """
    # Initialize buffers
    z_buffer = [0] * 1760  # Buffer for depth information
    b = [' '] * 1760  # Buffer for storing the characters to be displayed
    luminance_chars = '.,-~:;=!*#$@'  # Characters representing different levels of brightness

    # Loop through the angles for the points on the donut
    for j in range(0, 628, 7):  # Outer loop for the circle
        for i in range(0, 628, 2):  # Inner loop for the tube
            # Calculate the 3D coordinates of the donut points
            sin_i = math.sin(i)
            cos_i = math.cos(i)
            sin_j = math.sin(j)
            cos_j = math.cos(j)
            sin_A = math.sin(A)
            cos_A = math.cos(A)
            
            # Calculate donut coordinates in 3D space
            x = cos_i * (cos_j + 2)  # X coordinate
            y = sin_i * (cos_j + 2)  # Y coordinate
            z = sin_j  # Z coordinate
            
            # Rotate around the Y-axis (donut's vertical axis)
            x_prime = x * cos_A + z * sin_A
            z_prime = -x * sin_A + z * cos_A
            
            # Calculate the depth
            D = 1 / (z_prime + 5)
            
            # Project 3D coordinates to 2D
            xp = int(40 + 30 * D * x_prime)
            yp = int(12 + 15 * D * y)
            o = int(xp + 80 * yp)
            
            # Calculate luminance
            luminance_index = int(8 * ((sin_j * sin_A - sin_i * cos_j * cos_A) * cos_i - sin_i * cos_j * sin_A - cos_j * cos_A))
            luminance_index = max(0, min(len(luminance_chars) - 1, luminance_index))
            if 0 <= o < 1760 and D > z_buffer[o]:
                z_buffer[o] = D
                b[o] = luminance_chars[luminance_index]

    # Move the cursor to the top and print the frame
    move_cursor_to_top()
    for k in range(1760):
        sys.stdout.write(b[k])
        if k % 80 == 79:
            sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    """
    Runs the main animation loop.
    The main function initializes the angle of rotation `A` to 0.
    It then runs an infinite loop where it repeatedly calls `draw_donut`, increments `A` to animate the rotation, and adds a short delay with `time.sleep(0.03)` to control the animation speed.
    """
    A = 0  # Initialize rotation angle
    while True:
        draw_donut(A)
        A += 0.04  # Increment the angle for the next frame
        time.sleep(0.03)  # Delay to control the speed of the animation

if __name__ == "__main__":
    main()
