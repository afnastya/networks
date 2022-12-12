import subprocess
import sys
import platform

if len(sys.argv) < 2:
    print("No host")
    exit(1)
host = sys.argv[1]
print(f"Host: {host}")

FRAGMENT_ERROR_CODE = (1, 2)[platform.system().lower() == 'darwin']
NOT_FRAGMENT_OPTION = (["-M", "do"], ["-D"])[platform.system().lower() == 'darwin']

def ping(mtu):
    cmd = subprocess.run(
        ["ping", host, "-s", str(mtu), "-c", "1"] + NOT_FRAGMENT_OPTION,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print(f"ping {host}, mtu {mtu}, returncode {cmd.returncode}")
    return cmd

l, r = 0, 1
print("\nSearching for upper bound...")
cmd = ping(r)
while cmd.returncode == 0:
    r *= 2
    cmd = ping(r)
if cmd.returncode != FRAGMENT_ERROR_CODE:
    print("ERROR")
    print(cmd.stderr.decode().rstrip())
    exit(2)

print("\nBinsearch mtu...")
while l + 1 < r:
    mtu = (l + r) // 2

    cmd = ping(mtu)

    if cmd.returncode == 0:
        l = mtu
    elif cmd.returncode == FRAGMENT_ERROR_CODE:
        r = mtu
    else:
        print("ERROR")
        print(cmd.stderr.decode().rstrip())
        exit(2)

print(f"\nMTU is {l + 28}")

