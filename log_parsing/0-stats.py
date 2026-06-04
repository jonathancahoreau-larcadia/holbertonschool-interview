#!/usr/bin/python3
"""Log parser that reads stdin and prints aggregated metrics."""

import sys


def print_stats(total_size, status_codes, ref):
    """Print the current aggregate statistics."""
    print(f"File size: {total_size}")

    for code in status_codes:
        if code in ref:
            print(f"{code}: {ref[code]}")


def main():
    """Read stdin and compute metrics."""
    line_count = 0
    total_size = 0
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    ref = {}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (ValueError, IndexError):
                pass

            try:
                code = int(parts[-2])
                if code in status_codes:
                    ref[code] = ref.get(code, 0) + 1
            except (ValueError, IndexError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes, ref)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes, ref)
        return

    if line_count % 10 != 0:
        print_stats(total_size, status_codes, ref)


if __name__ == "__main__":
    main()
