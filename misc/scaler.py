import arcade


def dynamic_font(screen_width, screen_height, size):
    """Makes dynamic font sizes that scale with screen size"""
    return (2 * (screen_width + screen_height)) // size


def dynamic_width(screen_width, size):
    """Makes dynamic x values that scale with the screen"""
    return screen_width // size


def dynamic_height(screen_height, size):
    """Makes dynamic y values that scale with the screen"""
    return screen_height // size
