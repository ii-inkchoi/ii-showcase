# Acceptance test for a hero candidate.
#
#   python check-hero.py path/to/candidate.jpg [more.jpg ...]
#
# Orientation is not a criterion: a tall frame is cropped, and where the crop is taken decides
# everything, so this scans horizontal bands down the frame and reports the best one it finds,
# with the offset needed to reproduce it. Resolution is the real constraint, because a 1.6 crop
# has to come out at 2400px wide or more without upscaling.
#
# Every threshold came out of measuring the frames tried in this project, not from taste.
#
# What it cannot judge, and a human still must:
#   - a legible third-party logo. A Canadian financial institution's mark in an issuer's hero
#     lets a reader infer a relationship, and that is what disqualified the one Toronto frame
#     that passed everything measurable.
#   - aerial views, neon spectacle, anything else on the banned list.
#   - whether the frame is AI-generated. Never for the page.
import sys, os
from PIL import Image, ImageOps, ImageFilter

W, H = 2560, 1600
LO, HI = 4, 124
ASPECT = W / H

REGIONS = {
    "hmark 11px": ((0.17, 0.07, 0.42, 0.13), 4.5),
    "h1    54px": ((0.17, 0.52, 0.78, 0.78), 3.0),
    "hfoot 13px": ((0.17, 0.79, 0.58, 0.87), 4.5),
}


def contrast_white(l):
    def lin(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 1.05 / (lin(l) + 0.05)


def assess(band):
    """band is already the hero frame at W x H, before the window."""
    s = band.resize((160, 160))
    px = list(s.getdata())
    raw_rb = sum(v[0] for v in px) / len(px) - sum(v[2] for v in px) / len(px)
    lut = [max(0, min(255, int(LO + (v / 255.0) * (HI - LO)))) for v in range(256)]
    w = band.point(lut * 3).filter(ImageFilter.GaussianBlur(0.9))
    s2 = w.resize((160, 160))
    p2 = list(s2.getdata())
    rb = sum(v[0] for v in p2) / len(p2) - sum(v[2] for v in p2) / len(p2)
    sat = sum(max(v) - min(v) for v in p2) / len(p2)
    g = ImageOps.grayscale(w)
    gd = list(g.getdata())
    mean = sum(gd) / len(gd)
    px2 = g.load()
    tiers = {}
    worst_margin = 99.0
    for label, ((x0, y0, x1, y1), floor) in REGIONS.items():
        brightest = 0
        for y in range(int(y0 * H), int(y1 * H), 3):
            for x in range(int(x0 * W), int(x1 * W), 3):
                v = px2[x, y]
                if v > brightest:
                    brightest = v
        r = contrast_white(brightest)
        tiers[label] = (r, floor, brightest)
        worst_margin = min(worst_margin, r - floor)
    return dict(raw_rb=raw_rb, rb=rb, sat=sat, mean=mean, tiers=tiers,
                worst_margin=worst_margin)


def crop_band(im, offset):
    """a 1.6 band taken at a vertical offset, 0 = top, 1 = bottom."""
    if im.width / im.height >= ASPECT:
        nw = int(im.height * ASPECT)
        l = int((im.width - nw) * 0.5)
        return im.crop((l, 0, l + nw, im.height))
    nh = int(im.width / ASPECT)
    t = int((im.height - nh) * offset)
    return im.crop((0, t, im.width, t + nh))


def main(paths):
    worst = 0
    for path in paths:
        if not os.path.exists(path):
            print("no such file:", path); worst = 2; continue
        im = Image.open(path).convert("RGB")
        print("=" * 66)
        print("%s" % os.path.basename(path))
        print("  %dx%d  aspect %.2f" % (im.width, im.height, im.width / im.height))

        # resolution, the one thing a crop cannot fix
        crop_w = im.width if im.width / im.height < ASPECT else int(im.height * ASPECT)
        ok_res = crop_w >= 2400
        print("  %-4s a 1.6 crop is %d wide, needs 2400" % ("PASS" if ok_res else "FAIL", crop_w))
        if not ok_res:
            print("       FAIL on: resolution. A crop cannot add pixels.")
            worst = max(worst, 1)
            continue

        offsets = [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 1.0] if im.width / im.height < ASPECT else [0.5]
        results = []
        for off in offsets:
            band = crop_band(im, off).resize((W, H), Image.LANCZOS)
            a = assess(band)
            a["offset"] = off
            results.append(a)
        best = max(results, key=lambda a: a["worst_margin"])

        print("  band scan (offset: luminance / R-B / worst margin over floor)")
        for a in results:
            flag = " <= best" if a is best else ""
            print("       %.2f: %5.1f  %+6.1f  %+5.2f%s" % (
                a["offset"], a["mean"], a["rb"], a["worst_margin"], flag))

        a = best
        print("\n  best band at offset %.2f" % a["offset"])
        print("       luminance mean %.1f   saturation %.1f   R-B %+.1f  (raw R-B %+.1f)" % (
            a["mean"], a["sat"], a["rb"], a["raw_rb"]))
        fails = []
        if a["rb"] > 4:
            fails.append("golden tint")
        print("       %-4s R-B <= +4 after the window   (%+.1f)" % (
            "PASS" if a["rb"] <= 4 else "FAIL", a["rb"]))
        if a["mean"] > 55:
            fails.append("too bright")
        print("       %-4s luminance mean <= 55         (%.1f)" % (
            "PASS" if a["mean"] <= 55 else "FAIL", a["mean"]))
        for label, (r, floor, b) in a["tiers"].items():
            good = r >= floor
            if not good:
                fails.append(label.split()[0])
            print("       %-4s %-11s %5.2f  needs %.1f   brightest %d" % (
                "PASS" if good else "FAIL", label, r, floor, b))
        if fails:
            print("\n       FAIL on: " + ", ".join(fails))
            worst = max(worst, 1)
        else:
            print("\n       PASS. Now check by eye: third-party logos, aerial view, neon, AI.")
    return worst


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python check-hero.py <candidate> [more...]")
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
