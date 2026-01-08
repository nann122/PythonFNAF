import urllib.request
import os

os.makedirs('fonts', exist_ok=True)

def download_font(url, filename):
    """Download font from URL"""
    try:
        urllib.request.urlretrieve(url, f'fonts/{filename}')
        print(f"✅ Downloaded {filename}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")

# Download free fonts suitable for horror game
fonts = [
    # You can replace these with actual font URLs or use system fonts
    # For now, we'll create a simple font list
]

# Create font configuration file
font_config = """# Pizza Nights Font Configuration

DEFAULT_FONT = "fonts/Orbitron-Regular.ttf"
TITLE_FONT = "fonts/Orbitron-Bold.ttf"
UI_FONT = "fonts/Orbitron-Medium.ttf"

# Fallback to system fonts if custom fonts not available
FALLBACK_FONTS = [
    "Arial",
    "Helvetica",
    "Courier New"
]

# Font sizes
FONT_SIZES = {
    'small': 18,
    'medium': 24,
    'large': 36,
    'xlarge': 48,
    'title': 72
}
"""

with open('fonts/font_config.py', 'w') as f:
    f.write(font_config)

print("📝 Font configuration created")
