from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def qikas(images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "10003.png")
    try:
        frame.draw_text(
            (5, 0, 195, 60),
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
    "qikas",
    qikas,
    min_texts=1,
    max_texts=1,
    default_texts=["不要啊！"],
    keywords=["千咲说","qikas"],
    date_created=datetime(2025, 6, 25),
    date_modified=datetime(2025, 6, 25),
)