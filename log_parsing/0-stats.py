#!/usr/bin/python3
"""Log parser that reads stdin and prints aggregated metrics."""

import re
import sys


def print_stats(total_size, status_code, ref):
    """Print the current aggregate statistics."""
    print(f"File size: {total_size}")

    for code in status_code:
        if code in ref:
            print(f"{code}: {ref[code]}")


def main():
    """Read stdin and compute metrics."""
    line_count = 0
    total_size = 0
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    ref = {}

    pattern = re.compile(
        r'^\S+ - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:

            line = line.strip()
            match = pattern.match(line)

            if not match:
                continue

            line_count += 1

            code = int(match.group(1))
            file_size = int(match.group(2))

            if code in status_code:
                ref[code] = ref.get(code, 0) + 1

            total_size += file_size

            if line_count % 10 == 0:
                print_stats(total_size, status_code, ref)

    except KeyboardInterrupt:
        print_stats(total_size, status_code, ref)

    finally:
        print_stats(total_size, status_code, ref)


if __name__ == "__main__":
    main()
