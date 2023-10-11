import time
from colorama import init, Fore, Back, Style

init(autoreset=True)

def rainbow_gradient(n, cycles=1):
    """Generate n colors as a gradient in the format of RGB."""
    colors = []
    for i in range(n):
        angle = (i / n) * 2 * 3.1415926 * cycles
        r = int((1 + (0.5 * (1 + -sin(angle))) * -1) * 255)
        g = int((0.5 * (1 + cos(angle))) * 255)
        b = int((1 - (0.5 * (1 + sin(angle))) ** 2) * 255)
        colors.append((r, g, b))
    return colors

def rgb_to_ansi(r, g, b, background=False):
    """Convert RGB to an ANSI color code."""
    return f'\033[{48 if background else 38};2;{r};{g};{b}m'

def print_colorful(text, colors, background_colors, speed):
    """Print text with each letter in the next color of the gradient."""
    for i, char in enumerate(text):
        print(rgb_to_ansi(*colors[i % len(colors)]) + rgb_to_ansi(*background_colors[i % len(background_colors)], background=True) + char, end='', flush=True)
        time.sleep(speed)
    print(Style.RESET_ALL)  # Reset the style and move to the next line.

if __name__ == "__main__":
    word = input("Enter the word: ")
    speed = float(input("Enter the speed (e.g., 0.5): "))
    colors = rainbow_gradient(len(word), 2)  # two color cycles through the word
    background_colors = rainbow_gradient(len(word), 1)  # one color cycle through the word
    print_colorful(word, colors, background_colors, speed)