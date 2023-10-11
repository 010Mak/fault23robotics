import time
from colorama import init, Fore, Back, Style
from math import sin, cos, pi

init(autoreset=True)

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
            if char != ' ':  # Only color the non-space characters
                print(rgb_to_ansi(*colors[(i+j) % len(colors)]) + char, end='', flush=True)
            else:
                print(char, end='')
        print()

if __name__ == "__main__":
    # Define the ASCII square artwork
    square_art = [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ]

    phase = 0
    try:
        while True:
            # Increment the phase to give appearance of shifting colors
            phase += pi / 30
            colors = rainbow_gradient(10, phase, 2)  # 10 colors to cycle through for the square
            print_colorful_artwork(square_art, colors)
            time.sleep(0.1)  # Adjust this for faster/slower shifting of colors
            # Clear the console to redraw the square
            print('\033c', end='')  
    except KeyboardInterrupt:
        pass

    choice = input("Would you like to use a custom word? (y/n): ").strip().lower()
    while choice == 'y':
        word = input("Enter the word: ")
        speed = float(input("Enter the speed (e.g., 0.5): "))
        colors = rainbow_gradient(len(word))
        for char in word:
            print(rgb_to_ansi(*colors[word.index(char) % len(colors)]) + char, end='', flush=True)
            time.sleep(speed)
        print(Style.RESET_ALL)  # Reset the style and move to the next line
        choice = input("Would you like to use another custom word? (y/n): ").strip().lower()