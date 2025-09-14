from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_poster(asset_filename):
    # Look for the image inside the 'assets' folder
    assets = Path('assets')
    src = assets / asset_filename

    # Debugging: print where Python is looking for the file
    print("Looking for file at:", src.resolve())

    # Check if the file exists
    if not src.exists():
        raise FileNotFoundError(f"Asset not found: {src}")

    # Open the base image
    base = Image.open(src).convert('RGBA')
    w, h = base.size

    # Create a bottom banner
    banner_h = int(h * 0.08)
    banner = Image.new('RGBA', (w, banner_h), (0, 0, 0, 200))
    draw = ImageDraw.Draw(banner)

    # Load font or use default
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=int(banner_h * 0.4))
    except Exception:
        font = ImageFont.load_default()

    # Text for the banner
    text = 'CCIS Phantoms — Team Spirit Poster | Unseen but Unstoppable'
    tw, th = draw.textsize(text, font=font)
    draw.text(((w - tw) / 2, (banner_h - th) / 2), text, fill=(255, 105, 180, 255), font=font)

    # Combine the base image and the banner
    final_image = Image.new('RGBA', (w, h + banner_h), (0, 0, 0, 255))
    final_image.paste(base, (0, 0))
    final_image.paste(banner, (0, h), banner)

    # Save the final poster
    output_path = "Team_Spirit_Poster_Final.png"
    final_image.convert('RGB').save(output_path, format='PNG')

    print(f"🎉 Poster saved as: {output_path}")

# Run the script
if __name__ == '__main__':
    try:
        # Make sure the filename here matches your actual image filename
        make_poster('Team_Spirit_Poster.png')
    except Exception as e:
        print("❌ Error:", e)
