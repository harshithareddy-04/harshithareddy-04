import subprocess, re
raw = subprocess.check_output(["git","show","HEAD:lanyard.svg"]).decode("utf-8","replace")
for line in raw.splitlines():
    if "HARSHITHA" in line or "rotate(90)" in line or "strap" in line.lower() or "M152" in line:
        print(line.strip()[:200])
# also check older commits for strap text
