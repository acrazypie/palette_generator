import colorsys
from typing import Optional, List


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB to hex color."""
    return f"#{r:02x}{g:02x}{b:02x}"


def hsv_to_hex(h: float, s: float, v: float) -> str:
    """Convert HSV to hex color."""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return rgb_to_hex(int(r * 255), int(g * 255), int(b * 255))


def analogous(base_hex: str, count: int = 5) -> List[str]:
    """Generate analogous color palette (adjacent colors on the color wheel).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 5)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []
    step = 1.0 / count
    for i in range(count):
        shift = (i - count // 2) * step * 0.1
        nh = (h + shift) % 1
        palette.append(hsv_to_hex(nh, s, v))

    return palette


def complementary(base_hex: str, count: int = 5) -> List[str]:
    """Generate complementary color palette (opposite on color wheel).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 5)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []
    comp_h = (h + 0.5) % 1

    for i in range(count):
        if i < count // 2:
            nh = (h + (i / count) * 0.2) % 1
        else:
            nh = (comp_h + ((i - count // 2) / count) * 0.2) % 1
        palette.append(hsv_to_hex(nh, s, v))

    return palette


def triadic(base_hex: str, count: int = 9) -> List[str]:
    """Generate triadic color palette (3 colors equally spaced 120° apart).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 9)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []
    colors_per_section = count // 3

    for section in range(3):
        base_hue = (h + section * (1 / 3)) % 1
        for i in range(colors_per_section):
            shift = (i - colors_per_section // 2) * 0.05
            nh = (base_hue + shift) % 1
            palette.append(hsv_to_hex(nh, s, v))

    return palette


def tetradic(base_hex: str, count: int = 8) -> List[str]:
    """Generate tetradic color palette (4 colors forming a rectangle).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 8)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []
    colors_per_section = count // 4

    for section in range(4):
        base_hue = (h + section * 0.25) % 1
        for i in range(colors_per_section):
            shift = (i - colors_per_section // 2) * 0.04
            nh = (base_hue + shift) % 1
            palette.append(hsv_to_hex(nh, s, v))

    return palette


def monochromatic(base_hex: str, count: int = 5) -> List[str]:
    """Generate monochromatic color palette (variations of saturation and value).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 5)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []

    for i in range(count):
        # Vary saturation and value
        new_s = s * (0.3 + 0.7 * (i / (count - 1)))
        new_v = v * (0.4 + 0.6 * (1 - i / (count - 1)))
        palette.append(hsv_to_hex(h, new_s, new_v))

    return palette


def shades_and_tints(base_hex: str, count: int = 5) -> List[str]:
    """Generate palette with shades and tints (darker and lighter versions).

    Args:
        base_hex: Base color in hex format
        count: Number of colors to generate (default: 5)

    Returns:
        List of hex colors
    """
    r, g, b = hex_to_rgb(base_hex)
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    palette = []

    for i in range(count):
        ratio = i / (count - 1) if count > 1 else 0.5
        new_v = v * (0.2 + 0.8 * ratio)
        palette.append(hsv_to_hex(h, s, new_v))

    return palette


PALETTE_MODES = {
    "analogous": analogous,
    "complementary": complementary,
    "triadic": triadic,
    "tetradic": tetradic,
    "monochromatic": monochromatic,
    "shades_and_tints": shades_and_tints,
}


def generate_palette(
    base_hex: str, mode: str = "analogous", count: int = 5
) -> List[str]:
    """Generate a color palette using the specified mode.

    Args:
        base_hex: Base color in hex format (e.g., '#3498db')
        mode: Generation mode ('analogous', 'complementary', 'triadic', 'tetradic',
            'monochromatic', 'shades_and_tints'). Default: 'analogous'
        count: Number of colors to generate (default: 5)

    Returns:
        List of hex colors

    Raises:
        ValueError: If mode is not recognized
    """
    if mode not in PALETTE_MODES:
        raise ValueError(
            f"Unknown mode: {mode}. Available modes: {list(PALETTE_MODES.keys())}"
        )

    return PALETTE_MODES[mode](base_hex, count)
