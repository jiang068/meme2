from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def flls(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "10017.png")
    try:
        frame.draw_text(
            (0, -5, 200, 55),
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
    "flls",
    flls,
    min_texts=1,
    max_texts=1,
    default_texts=["不可以"],
    keywords=["弗洛洛说","flls","fll说"],
    date_created=datetime(2025, 6, 26),
    date_modified=datetime(2025, 6, 26),
)