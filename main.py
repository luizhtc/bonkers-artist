import random

from PIL import Image, ImageDraw

IMG_WIDTH = 800
IMG_HEIGHT = 600

COLOR_PALLETE = [
    (12, 177, 242),
    (24, 181, 217),
    (55, 126, 146),
    (208, 74, 60),
]

BACKGROUND_COLOR = (13, 13, 13)

N_SHAPES = 16


def color_picker():
    return COLOR_PALLETE[random.randint(0, len(COLOR_PALLETE) - 1)]


def position_picker(n_coords: int, sort_x: bool = False, sort_y: bool = False):
    if n_coords == 1:
        return (random.randint(0, IMG_WIDTH), random.randint(0, IMG_HEIGHT))

    x_positions = [random.randint(0, IMG_WIDTH) for _ in range(n_coords)]
    y_positions = [random.randint(0, IMG_HEIGHT) for _ in range(n_coords)]

    if sort_x:
        x_positions.sort()
    if sort_y:
        y_positions.sort()

    coords = []
    for x, y in zip(x_positions, y_positions, strict=True):
        coords.append((x, y))
    return coords


im = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(im)

shapes = [
    "circle",
    "polygon",
]

i = 0
while i != N_SHAPES:
    shape = shapes[random.randint(0, len(shapes) - 1)]
    match shape:
        case "circle":
            draw.circle(position_picker(1), random.expovariate(0.05), color_picker())
        case "polygon":
            draw.polygon(position_picker(random.randint(4, 10)), color_picker())
        case _:
            pass
    i += 1

im.save("icon.png")
