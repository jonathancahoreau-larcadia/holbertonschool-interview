#!/usr/bin/python3
"""Log parser that reads stdin and prints aggregated metrics.

Reads log entries from standard input, parses the status code and file size
from each valid line, and prints cumulative statistics every 10 lines or when
interrupted by CTRL + C.

Expected input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>

Example:
    192.168.0.1 - [2024-02-12] "GET /projects/260 HTTP/1.1" 200 512

Output format:
    File size: <total size>
    <status code>: <count>

Only supported HTTP status codes are reported in ascending order.
"""

import sys


def print_stats():
    """Print the current aggregate statistics."""
    print(f"File size: {total_size}")
    for code in status_code:
        if code in ref:
            print(f"{code}: {ref[code]}")


line_count = 0  # number of valid lines processed
total_size = 0  # cumulative file size from parsed log entries
status_code = [200, 301, 400, 401, 403, 404, 405, 500]  # supported HTTP codes
ref = {}  # counts of seen status codes

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            cut = line.split()

            try:
                file_size = int(cut[-1])
                code = int(cut[-2])
            except (ValueError, IndexError):
                # Ignore malformed lines that do not contain
                # a valid code and size
                continue

            if code in status_code:
                ref[code] = ref.get(code, 0) + 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
