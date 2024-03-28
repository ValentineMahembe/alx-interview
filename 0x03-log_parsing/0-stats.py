#!/usr/bin/python3
import sys
import signal

# Initialize variables
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0

def print_stats():
    print("File size: {:d}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {:d}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    try:
        data = line.split()
        status_code = data[-2]
        file_size += int(data[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except:
        pass

    if len(data) % 10 == 0:
        print_stats()

print_stats()
