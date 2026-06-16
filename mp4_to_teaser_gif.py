'''
Convert project teaser mp4s under assets/teaser/<project>/ into small,
loopable gifs, calibrated against assets/teaser/dkt/dkt-teaser.gif
(320px wide, ~10fps, ~500 frames, ~14MB) so new teasers stay light enough
to embed the way index.html does (col-md-3 <img style="width:100%">).
'''

import argparse
import json
import subprocess
from pathlib import Path

WIDTH = 320
MAX_FRAMES = 500
MIN_FPS = 2
MAX_FPS = 10


def probe(src: Path):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=r_frame_rate,duration",
        "-of", "json", str(src),
    ])
    stream = json.loads(out)["streams"][0]
    num, den = stream["r_frame_rate"].split("/")
    orig_fps = float(num) / float(den)
    duration = float(stream["duration"])
    return orig_fps, duration


def convert(src: Path, dst: Path):
    orig_fps, duration = probe(src)
    target_fps = max(MIN_FPS, min(MAX_FPS, MAX_FRAMES / duration, orig_fps))

    vf = f"fps={target_fps:.3f},scale={WIDTH}:-2:flags=lanczos"
    palette = dst.with_suffix(".palette.png")

    subprocess.run([
        "ffmpeg", "-y", "-i", str(src),
        "-vf", f"{vf},palettegen=stats_mode=diff",
        str(palette),
    ], check=True, capture_output=True)

    subprocess.run([
        "ffmpeg", "-y", "-i", str(src), "-i", str(palette),
        "-lavfi", f"{vf}[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle",
        str(dst),
    ], check=True, capture_output=True)

    palette.unlink(missing_ok=True)
    return target_fps


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "inputs", nargs="*",
        help="mp4 files to convert; default: every assets/teaser/*/*.mp4",
    )
    args = parser.parse_args()

    srcs = [Path(p) for p in args.inputs] or sorted(Path("assets/teaser").glob("*/*.mp4"))

    for src in srcs:
        dst = src.parent / f"{src.parent.name}-teaser.gif"
        fps = convert(src, dst)
        size_mb = dst.stat().st_size / (1024 * 1024)
        print(f"{src} -> {dst}  fps={fps:.2f}  size={size_mb:.1f}MB")


if __name__ == "__main__":
    main()
