from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def pbs(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (0, 5, 180, 75),
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
    "pbs",
    pbs,
    min_texts=1,
    max_texts=1,
    default_texts=["嘟嘟嘟\n说什么呢"],
    keywords=["菲比说"],
    date_created=datetime(2025, 3, 17),
    date_modified=datetime(2025, 3, 17),
)