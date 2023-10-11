import time
import os
from math import sin, cos, pi

def rainbow_gradient(n, phase=0, cycles=1):
    """Generate n colors as a gradient in the format of RGB based on phase."""
    colors = []
    for i in range(n):
        angle = (i / n) * 2 * pi * cycles + phase
        r = int((1 + (0.5 * (1 + -sin(angle))) * -1) * 255)
        g = int((0.5 * (1 + cos(angle))) * 255)
        b = int((1 - (0.5 * (1 + sin(angle))) ** 2) * 255)
        colors.append((r, g, b))
    return colors

def rgb_to_ansi(r, g, b, background=False):
    """Convert RGB to an ANSI color code."""
    return f'\033[{48 if background else 38};2;{r};{g};{b}m'

def print_colorful_artwork(artwork, colors):
    """Print colorful ASCII artwork."""
    for i, line in enumerate(artwork):
        for j, char in enumerate(line):
            print(rgb_to_ansi(*colors[(i+j) % len(colors)]) + char, end='', flush=True)
        print()

if __name__ == "__main__":
    with open("artwork.txt", "r") as file:
        artwork = file.readlines()

    phase = 0
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            phase += pi / 30
            colors = rainbow_gradient(max(len(line) for line in artwork) + len(artwork), phase, 2)
            print_colorful_artwork(artwork, colors)
            time.sleep(0.1)  # Adjust this for faster/slower shifting of colors
    except KeyboardInterrupt:
        pass
