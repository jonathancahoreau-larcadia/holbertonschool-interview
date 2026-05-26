# Minimum Operations

In a text file, there is a single character `H`.

Your text editor can execute only two operations:

- **Copy All**
- **Paste**

Given a number `n`, write a method that calculates the **fewest number of operations** needed to result in **exactly `n` `H` characters** in the file.

Be smart about how you utilize the memory!

---

## Problem description

- Initial content of the file: `H`
- Allowed operations:
  - **Copy All** → copies the entire current content of the file into a buffer
  - **Paste** → pastes the buffer content at the end of the file
- Goal: reach **exactly `n` `H` characters**
- Output: **minimum number of operations** (Copy + Paste) required

If it is **impossible** to reach exactly `n` `H` characters, return `0`.

---

## Example

- `n = 1`
  Already have `H` → **0 operations**

- `n = 3`
  - Copy All (`H`) → 1
  - Paste (`HH`) → 2
  - Paste (`HHH`) → 3
  **Result: 3 operations**

- `n = 4`
  - Copy All (`H`) → 1
  - Paste (`HH`) → 2
  - Copy All (`HH`) → 3
  - Paste (`HHHH`) → 4
  **Result: 4 operations**

---

## Intuition

The optimal strategy is based on **factors** of `n`:

- When you can build `n` by multiplying smaller numbers,
  you can think in terms of:
  - **Copy** when you decide to reuse a block
  - **Paste** several times to reach a multiple

In practice, the minimal number of operations is obtained by **decomposing `n` into its prime factors** and summing them.

---

## Function prototype

Example in Python:

```python
def minOperations(n: int) -> int:
    """
    Returns the fewest number of operations needed
    to result in exactly n H characters.
    """
