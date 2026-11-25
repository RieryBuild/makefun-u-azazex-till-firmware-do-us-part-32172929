"""Write the robot wedding vow to entry.txt.

The joke: the wedding ring is treated as a piece of hardware — the one
peripheral this machine will never unplug and never trade for
a newer model. A robot's fidelity is refusing an upgrade, which is both the
laugh (a ring as a USB device) and the tenderness (no newer model, ever).
"""

import os

VOW = "I take this ring as the one peripheral I will never unplug and never trade for a newer model."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(VOW)
