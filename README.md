# Pascal Triangle

This project implements a function that generates Pascal’s Triangle up to a given number of rows.

## 📌 Description

The function `pascal_triangle(n)` returns a list of lists of integers representing Pascal’s Triangle.

Each row is built from the previous one using the rule:

- The first and last elements of each row are always `1`
- Any inner element is the sum of the two elements directly above it

---

## 📥 Prototype

```python
def pascal_triangle(n):
