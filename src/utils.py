def load_image(file_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def load_font(font_path, size):
    """Load a font from the specified file path with the given size."""
    try:
        font = pygame.font.Font(font_path, size)
        return font
    except FileNotFoundError:
        print(f"Font file not found: {font_path}")
        return None

def draw_text(surface, text, font, color, position):
    """Draw text on the given surface at the specified position."""
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def load_sound(file_path):
    """Load a sound from the specified file path."""
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound
    except pygame.error as e:
        print(f"Unable to load sound at {file_path}: {e}")
        return None