# Rotate 2D Matrix

## Description
This project features a Python algorithm designed to rotate an $n \times n$ 2D matrix by 90 degrees clockwise.

The core constraint of this task is that the rotation must be performed **in-place**. The function edits the original matrix directly in memory and does not return a new matrix.

## Requirements
* **Prototype:** `def rotate_2d_matrix(matrix):`
* **Return Value:** None (Do not return anything).
* **Assumptions:** You can assume the given matrix will always have 2 dimensions and will not be empty.

## Files
* `0-rotate_2d_matrix.py`: The Python script containing the `rotate_2d_matrix` function.
* `main_0.py`: The test file used to execute and verify the function.

## Usage & Example

Here is how to use the function and what the expected output looks like.

**1. Create the test file (`main_0.py`):**
```python
#!/usr/bin/python3
"""
Test - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
