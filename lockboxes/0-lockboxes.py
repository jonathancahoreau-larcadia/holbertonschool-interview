#!/usr/bin/env python3
def canUnlockAll(boxes):
    opened = {0}
    to_check = [0]

    while to_check:
        boxe = to_check.pop()

        for key in boxes[boxe]:
            if 0<= key < len(boxes) and key not in opened:
                opened.add(key)
                to_check.append(key)

    if len(boxes) - len(opened) == 0:
        return True
    else :
        return False
