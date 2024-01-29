from distutils.core import setup

import py2exe
import glob

setup(
    console=["python_project.py"],
    data_files=[
        ("sprites", glob.glob("sprites\\*.json")),
        ("sound_effects", glob.glob("sound_effects\\*.ogg") + glob.glob("sound_effects\\*.wav")),
        ("levels", glob.glob("levels\\*.json")),
        ("images", glob.glob("images\\*.gif") + glob.glob("images\\*.png")),
        ("", ["settings.json"]),
    ],
)
