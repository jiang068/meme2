from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def jtws(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "10017.png")
    try:
        frame.draw_text(
            (20, 0, 180, 55),
            text,
            fill=(111, 95, 95),
            allow_wrap=True,
            max_fontsize=50,
            min_fontsize=15,
            lines_align="center",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "jtws",
    jtws,
    min_texts=1,
    max_texts=1,
    default_texts=["zako~zako~"],
    keywords=["洁塔薇说","jtws","jtw说"],
    date_created=datetime(2025, 6, 26),
    date_modified=datetime(2025, 6, 26),
)