import subprocess
import sys

if sys.argc < 2:
    print("No host")
    exit(1)
host = sys.argv[1]
print(host)


l, r = 0, 5000
while l + 1 < r:
    mtu = (l + r) // 2
    cmd = subprocess.run(["ping", host, "-M", "do", "-s", str(mtu), "-c", "1"], capture_output=True)
    print(f"ping {host}, mtu {mtu}, returncode {cmd.returncode}, cmd output {cmd.stdout}")

    if cmd.returncode == 0:
        l = mtu
    elif cmd.returncode == 2:     # Fragment error
        r = mtu
    else:
        print("ERROR")
        print(cmd.stdout)
        exit(2)

print(f"Minimal mtu is {l + 28}")

