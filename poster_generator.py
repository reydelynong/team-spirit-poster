from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_combined_poster(asset_filename, output_path):
    assets = Path('assets')
    src = assets / asset_filename
    if not src.exists():
        raise FileNotFoundError(f"Asset not found: {src}")
    base = Image.open(src).convert('RGBA')
    w, h = base.size
    banner_h = int(h * 0.08)
    banner = Image.new('RGBA', (w, banner_h), (0,0,0,200))
    draw = ImageDraw.Draw(banner)
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', size=int(banner_h*0.4))
    except Exception:
        font = ImageFont.load_default()
    text = 'CCIS Phantoms — Team Spirit Poster | Concept: Unseen but Unstoppable'
    tw, th = draw.textsize(text, font=font)
    draw.text(((w-tw)/2, (banner_h-th)/2), text, fill=(255,105,180,255), font=font)
    combined = Image.new('RGBA', (w, h + banner_h), (0,0,0,255))
    combined.paste(base, (0,0))
    combined.paste(banner, (0, h), banner)
    combined.convert('RGB').save(output_path, format='PNG')
    print(f"Saved combined poster to {output_path}")

if __name__ == '__main__':
    for fname in ['A_digital_graphic_design_poster_features_the_CCIS_.png', 'A_poster_for_the_CCIS_Phantoms_team_features_bold_.png']:
        try:
            make_combined_poster(fname, 'combined_' + fname)
        except Exception as e:
            print(e)
