# Rotating Donut in Console

This Python script draws and animates a rotating 3D donut in the console. It uses trigonometric functions to calculate the 3D coordinates of points on the donut, applies a rotation, and projects these points onto a 2D plane. The brightness of each point is calculated to give a realistic 3D appearance, and the entire frame is printed to the console in each iteration to create the animation effect.

## Explanation
### Function to Move Cursor to Top
- `move_cursor_to_top()`: Moves the cursor to the top of the console using an escape sequence.

### Main Drawing Function
- `draw_donut(A)`: Draws a frame of the rotating donut.
  - **Parameters**: `A` (float) - The angle of rotation.

#### Arrays
- `z_buffer`: Stores depth information for each point on the donut to handle which part is in front.
- `b`: Stores characters that will be printed to the console to form the image of the donut.
- `luminance_chars`: A string of characters used to represent different levels of brightness on the donut's surface.

#### Loop Through Points on the Donut
- Iterates over angles `i` and `j` to cover the surface of the donut. These angles represent points in the donut's parametric equations.

#### Calculate Coordinates
- Uses sine and cosine of angles `i`, `j`, and `A` to determine the 3D coordinates of points on the donut and apply the rotation.

#### 3D to 2D Transformation
- Determines the 3D coordinates (`x`, `y`, `z`) of each point on the donut.

#### Rotate Around the Y-axis
- Applies rotation around the Y-axis using the angle `A` to calculate new coordinates (`x_prime`, `z_prime`).

#### Depth Calculation
- Calculates the depth (`D`) to create a perspective effect, making the donut look 3D.

#### Project 3D Coordinates to 2D
- Converts the 3D coordinates to 2D screen coordinates (`xp`, `yp`) and determines the position in the console buffer (`o`).

#### Calculate Luminance
- Calculates the brightness of each point on the donut using a formula and clamps the result to ensure it is within the valid range of the luminance characters.

#### Update Buffers
- Updates the `z_buffer` and `b` arrays if the current point is closer than any previously rendered point at the same screen position.

### Print the Frame
- Moves the cursor to the top and prints the contents of the `b` array to the console to create the frame of the donut.

### Main Loop
- The `main()` function runs an infinite loop that repeatedly calls `draw_donut`, increments `A` to animate the rotation, and adds a short delay with `time.sleep(0.03)` to control the animation speed.

## Summary
This code draws and animates a rotating 3D donut in the console. It uses trigonometric functions to calculate the 3D coordinates of points on the donut, applies a rotation, and projects these points onto a 2D plane. The brightness of each point is calculated to give a realistic 3D appearance, and the entire frame is printed to the console in each iteration to create the animation effect.
