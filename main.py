from colorama import init, Fore

def draw_dodecahedron():
    print(Fore.MAGENTA)  # Set color to purple

    # A more complex attempt to draw a simplified dodecahedron with interior lines
    # Using "*" as a representation of vertices and "-" and "|" as edges
    print("""
          * * * *
      *---------------*
    /  .           .    \\
  /  / \\         / \\    \\
*--*---*---------*---*--*
| \\    |        |    /  |
|  \\   *--------*   /   |
|   \\ /          \\ /    |
|    *------------*     |
|   / \\          / \\    |
|  /   *--------*   \\   |
| /    |        |    \\  |
*--*---*---------*---*--*
  \\  / \\       / \\  /
    \\   '     '    /
      *-----------*
          * * * *
    """)

if __name__ == "__main__":
    init()  # Initialize the colorama
    draw_dodecahedron()
