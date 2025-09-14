
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_poster(asset_filename):
    assets = Path('assets')
    src = assets / asset_filename

    if not src.exists():
        raise FileNotFoundError(f"Asset not found: {src}")

    base = Image.open(src).convert('RGBA')
    w, h = base.size

    banner_h = int(h * 0.08)
    banner = Image.new('RGBA', (w, banner_h), (0, 0, 0, 200))
    draw = ImageDraw.Draw(banner)

    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=int(banner_h * 0.4))
    except Exception:
        font = ImageFont.load_default()

    text = 'CCIS Phantoms — Team Spirit Poster | Unseen but Unstoppable'
    tw, th = draw.textsize(text, font=font)
    draw.text(((w - tw) / 2, (banner_h - th) / 2), text, fill=(255, 105, 180, 255), font=font)

    final_image = Image.new('RGBA', (w, h + banner_h), (0, 0, 0, 255))
    final_image.paste(base, (0, 0))
    final_image.paste(banner, (0, h), banner)

    output_path = "Team_Spirit_Poster_Final.png"
    final_image.convert('RGB').save(output_path, format='PNG')

    print(f"🎉 Poster saved as: {output_path}")

if __name__ == '__main__':
    try:
        make_poster('Team_Spirit_Poster.png')
    except Exception as e:
        print("❌ Error:", e)
