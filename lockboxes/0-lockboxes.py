#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked.

    Each element in `boxes` is a list of keys (integers) for other
    boxes. You start with box 0 unlocked. A key with value `k` opens
    box `k` if `0 <= k < len(boxes)`.

    Args:
        boxes (list of list of int): The list of boxes with keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    opened = {0}
    to_check = [0]

    while to_check:
        box = to_check.pop()

        for k in boxes[box]:
            if 0 <= k < len(boxes) and k not in opened:
                opened.add(k)
                to_check.append(k)

    if len(boxes) - len(opened) == 0:
        return True
    else:
        return False
