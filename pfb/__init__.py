from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import CommandShortcut, add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def pfb(images, texts: list[str], args):
    frame = BuildImage.open(img_dir / "pfb.png")

    def draw(pos: tuple[float, float, float, float], text: str):
        try:
            frame.draw_text(
                pos,
                text,
                max_fontsize=30,  # 由于图片较小，减小最大字体大小
                min_fontsize=10,  # 减小最小字体大小
                allow_wrap=True,
                fill="white",
                stroke_fill="black",
                stroke_ratio=0.05,
            )
        except ValueError:
            raise TextOverLength(text)

    # 左上文本框位置和大小调整
    top_left_pos = (0, -10, 165, 70)
    # 右下文本框位置和大小调整
    bottom_right_pos = (30, 170, 130, 200)

    if len(texts) >= 1:
        draw(top_left_pos, texts[0])
    if len(texts) >= 2:
        draw(bottom_right_pos, texts[1])

    return frame.save_jpg()


add_meme(
    "pfb",
    pfb,
    min_texts=2,
    max_texts=2,
    default_texts=["评分13.0，你是MVP！", "评分表"],
    keywords=["躺赢狗", "评分表"],
    shortcuts=[
        CommandShortcut(
            key=r"评分表\s+(?P<top_left>\S+)\s+(?P<bottom_right>\S+)",
            args=["{top_left}", "{bottom_right}"],
            humanized="评分表 左上话语 右下话语",
        ),
    ],
    date_created=datetime(2022, 6, 12),
    date_modified=datetime(2024, 8, 12),
)
