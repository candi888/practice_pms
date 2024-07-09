import subprocess


cmds = [
    "cargo run ./src/main.rs",
    "python ./src/plot.py",
]

for cmd in cmds:
    subprocess.run(cmd.split())
