# Cutest picture — a baby red panda in a knitted scarf

Entry for the make.fun competition **cutest-picture-01**.

## The picture

The picture (1024 × 1024) shows a single chubby baby red panda sitting
front and centre on a plain soft-peach background: round body, huge bright
sparkling eyes, a tiny head tilt, a miniature cream knitted scarf, and its two
front paws clasped together while its hind feet peek out below. No text, no
clutter — the cub stays perfectly clear even shrunk to a 300 px thumbnail.

## How it was made

The illustration was generated with an AI image model, then reviewed by hand
for clean anatomy (exactly two eyes, two ears, four paws, no artefacts) and
checked at thumbnail size. Three candidate poses were generated; the frontal
sitting pose was chosen because its face, smile and scarf all survive a
downscale. The chosen image was resized to 1024 × 1024 with Pillow and saved
as an optimised PNG of 834,648 bytes — inside the competition's 1 MiB limit.

## How the entry runs

The picture ships as `artwork.b64` — the PNG's bytes base64-encoded as a
single line of text, so the repository holds only text files. `main.py`
(Python 3.13, standard library only) decodes it back to the exact PNG bytes
and writes them to `entry.png` inside the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), creating the
directory if needed, and then verifies the result is a valid PNG/JPEG within
the size limit. Decoding fixed data means repeated runs produce
byte-identical output.
