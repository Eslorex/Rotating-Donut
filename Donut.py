import math
import sys
import time

def move_cursor_to_top():
    sys.stdout.write("\x1b[H")
    sys.stdout.flush()

def draw_donut(A):
    z_buffer = [0] * 1760
    b = [' '] * 1760
    luminance_chars = '.,-~:;=!*#$@'

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            sin_i = math.sin(i)
            cos_i = math.cos(i)
            sin_j = math.sin(j)
            cos_j = math.cos(j)
            sin_A = math.sin(A)
            cos_A = math.cos(A)
            
            # Calculate donut coordinates in 3D space
            x = cos_i * (cos_j + 2)
            y = sin_i * (cos_j + 2)
            z = sin_j
            

            # # Rotate around the X-axis (horizontal axis)
            # y_prime = y * cos_A - z * sin_A
            # z_prime = y * sin_A + z * cos_A
            # # x remains unchanged
            # x_prime = x

            # Rotate around the Y-axis (donut's vertical axis)
            x_prime = x * cos_A + z * sin_A
            z_prime = -x * sin_A + z * cos_A
            # y remains unchanged
            y_prime = y

            # # Rotate around the Z-axis (donut's axis)
            # x_prime = x * cos_A - y * sin_A
            # y_prime = x * sin_A + y * cos_A
            # # z remains unchanged
            # z_prime = z

          
            # Calculate the depth
            D = 1 / (z_prime + 5)
            
            # Project 3D coordinates to 2D
            xp = int(40 + 30 * D * x_prime)
            yp = int(12 + 15 * D * y_prime)
            o = int(xp + 80 * yp)
            
            # Calculate luminance
            luminance_index = int(8 * ((cos_j * sin_i - sin_i * cos_j * cos_A) * cos_i - sin_i * cos_j * sin_A - cos_j * cos_A))
            luminance_index = max(0, min(len(luminance_chars) - 1, luminance_index))
            if 0 <= o < 1760 and D > z_buffer[o]:
                z_buffer[o] = D
                b[o] = luminance_chars[luminance_index]

    move_cursor_to_top()
    for k in range(1760):
        sys.stdout.write(b[k])
        if k % 80 == 79:
            sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    A = 0
    while True:
        draw_donut(A)
        A += 0.04
        time.sleep(0.03)

if __name__ == "__main__":
    main()
