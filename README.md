# Rotating Donut in Console

This Python script draws and animates a rotating 3D donut in the console. It uses trigonometric functions to calculate the 3D coordinates of points on the donut, applies a rotation, and projects these points onto a 2D plane. The brightness of each point is calculated to give a realistic 3D appearance, and the entire frame is printed to the console in each iteration to create the animation effect.

## Explanation
### Function to Move Cursor to Top
- `move_cursor_to_top()`: Moves the cursor to the top of the console using an escape sequence. This allows the new frame to overwrite the previous one, creating the illusion of animation.

### Main Drawing Function
- `draw_donut(A)`: Draws a frame of the rotating donut.
  - **Parameters**: `A` (float) - The angle of rotation.

#### Arrays
- `z_buffer`: Stores depth information for each point on the donut to handle which part is in front.
- `b`: Stores characters that will be printed to the console to form the image of the donut.
- `luminance_chars`: A string of characters used to represent different levels of brightness on the donut's surface.

### Working Order of `draw_donut`

1. **Initialize Buffers**:
   - `z_buffer` is initialized to store depth information. It is used to determine which parts of the donut are visible.
   - `b` is initialized to store the characters that will form the donut's image.
   - `luminance_chars` is a string containing characters that represent different levels of brightness.

2. **Iterate Over Angles**:
   - The outer loop iterates over the angle `j`, which represents the circle around the donut.
   - The inner loop iterates over the angle `i`, which represents the tube of the donut.

3. **Calculate 3D Coordinates**:
   - For each combination of `i` and `j`, the script calculates the 3D coordinates (`x`, `y`, `z`) using trigonometric functions.
   - `i` and `j` are angles in radians, and the calculations use sine and cosine functions to find the coordinates.

4. **Apply Rotation**:
   - The 3D coordinates are rotated around the Y-axis by angle `A`.
   - The new coordinates (`x_prime`, `z_prime`) are computed using rotation formulas:
     - \( x' = x \cdot \cos(A) + z \cdot \sin(A) \)
     - \( z' = -x \cdot \sin(A) + z \cdot \cos(A) \)

5. **Depth Calculation**:
   - The depth value `D` is calculated to create a perspective effect:
     - \( D = \frac{1}{z' + 5} \)
   - This ensures that points farther from the viewer appear smaller.

6. **Project 3D to 2D**:
   - The 3D coordinates are projected onto a 2D plane:
     - \( x_{\text{screen}} = 40 + 30 \cdot D \cdot x' \)
     - \( y_{\text{screen}} = 12 + 15 \cdot D \cdot y \)
   - The resulting 2D coordinates (`xp`, `yp`) are used to find the position in the console buffer (`o`).

7. **Calculate Luminance**:
   - The brightness of each point is calculated using a formula that considers the angles and rotations.
   - The result is clamped to ensure it is within the valid range of `luminance_chars`.

8. **Update Buffers**:
   - If the current point is closer to the viewer than any previously rendered point at the same screen position, the `z_buffer` and `b` arrays are updated.
   - This ensures that only the visible parts of the donut are rendered.

9. **Print the Frame**:
   - The cursor is moved to the top of the console.
   - The contents of the `b` array are printed to the console, forming the frame of the donut.

### Main Loop
- The `main()` function runs an infinite loop that repeatedly calls `draw_donut`, increments `A` to animate the rotation, and adds a short delay with `time.sleep(0.03)` to control the animation speed.

