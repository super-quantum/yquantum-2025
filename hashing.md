Sure! Here's a clear and concise summary of the lecture:

---

**CMSC 420 - Lecture 10 Summary: Hashing – Basic Concepts and Hash Functions**

**Overview:**
Hashing is an efficient technique used to implement dictionary operations (`insert()`, `delete()`, `find()`) in expected **O(1) time**, unlike comparison-based structures like AVL trees or skip lists which operate in **O(log n)** time.

**Key Concepts:**

- **Hashing Basics:**
  - Hashing avoids comparisons by mapping keys to indices in a fixed-size table using a **hash function**.
  - Collisions (two keys mapping to the same index) are possible and must be handled.
  - Best used for exact-key lookups, not for ordered operations like range or nearest-neighbor queries.

- **Hash Functions:**
  - Should be **efficient** (constant time), depend on **all bits of the key**, and **scatter keys well**.
  - Common examples:
    - **Division Hashing:** `h(x) = x % m` (simple, but poor clustering).
    - **Multiplicative Hashing:** `h(x) = (a * x) % m`.
    - **Linear Hashing:** `h(x) = (a * x + b) % m`.
    - **Polynomial Hashing:** Used for strings or sequences. Efficiently implemented using **Horner’s Rule**.

- **Example (Java implementation of Polynomial Hashing using Horner’s Rule):**
  ```java
  public int hash(String c, int m) {
      final int P = 37;
      int hashValue = 0;
      for (int i = c.length() - 1; i >= 0; i--) {
          hashValue = P * hashValue + Character.getNumericValue(c.charAt(i));
      }
      return hashValue % m;
  }
  ```

- **Universal Hashing:**
  - Uses **randomization** to select a hash function from a family to avoid worst-case scenarios.
  - A hashing system is **universal** if the chance of a collision between two distinct keys is at most `1/m`.
  - Example function:
    - `h_ab(x) = ((a * x + b) mod p) mod m`
    - `p` is a large prime > all keys, and `a` and `b` are random.

**Conclusion:**
Hashing is a powerful tool for fast data retrieval when ordering isn’t required. The choice of a good hash function and collision resolution strategy (covered in the next lecture) is crucial for maintaining performance.

---

Let me know if you'd like a visual diagram or slide-style breakdown!