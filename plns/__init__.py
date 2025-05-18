from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def plns(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "plns.png")
    try:
        frame.draw_text(
            (0, 5, 240, 150),
            text,
            fill=(111, 95, 95),
            allow_wrap=True,
            max_fontsize=80,
            min_fontsize=25,
            lines_align="center",
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "plns",
    plns,
    min_texts=1,
    max_texts=1,
    default_texts=["不要草我\n我给你钱好吗"],
    keywords=["普拉娜说", "plns", "pln说"],
    date_created=datetime(2025, 5, 18),
    date_modified=datetime(2025, 5, 18),
)