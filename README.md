# YQuantum 2025 - Super Hash Function Challenge

> _"Quantum computations are the next frontier in securing blockchain with advanced proof-of-work." – Anonymous, probably_

Welcome to Superquantum challenge at **YQuantum 2025**! This repository houses resources and examples for developing a quantum-based hash function, as described in our challenge prompt. Below you’ll find instructions on how to use and navigate the materials, as well as details on submission and evaluation.

## Contents

1. [Challenge Description](#challenge-description)
2. [Example Notebooks](#example-notebook)
3. [Recommended Environment & Dependencies](#recommended-environment--dependencies)
4. [Documentation & Write-up](#documentation--write-up)
5. [Submission Guidelines](#submission-guidelines)
6. [Evaluation Criteria](#evaluation-criteria)
7. [License & Attribution](#license--attribution)

---

## Challenge Description

The heart of this repository is the **[challenge.md](challenge.md)** file. It details the goal of the challenge and provides the necessary information for you to understand the problem.

---

## Example Notebook

This repository provides an example Jupyter notebook **[example.ipynb](example.ipynb)**. It provides an example quantum hash function and analyzes it based on our judging criteria.

---

## Qhash implementaion

We also provide a simplified implementation of the Qubitcoin's hash algorithm in the **[qhash.py](qhash.py)** (which we internally call qhash) for you to analyze. This implementation lacks the post-simulation classical hashing present in the blockchain to make it more in line with the challenge requirements. However, it only accepts 256-bit inputs, which would make it not eligible as a challenge solution.

---

## Recommended Environment & Dependencies

`example.ipynb` and `qhash.py` require the following dependencies to be run locally:

- [qiskit](https://pypi.org/project/qiskit/)
- [numpy](https://pypi.org/project/numpy/)

---

## Documentation & Write-up

A well-documented solution is key:

- **Code Documentation**: Add docstrings and inline comments explaining your logic, especially where the quantum portion is crucial (i.e., the “hashing” circuit).
- **Write-up**: Provide a `writeup.pdf` (or an equivalent Markdown/LaTeX file) detailing your approach:

  - Explanation of your circuit design.
  - Performance and quality analysis of your output.
  - Rationale for how your function meets the challenge requirements.

  **Optionally**:

  - Analysis of the Qubitcoin's hash algorithm.

---

## Submission Guidelines

To submit your final project:

1. **Include Source Code**:  
   Place your core hashing function in the `main.py` that takes `bytes` as input and returns `bytes` as output.

2. **Include Documentation**:
   Provide a `writeup.pdf` summarizing your design, plus a brief presentation (`presentation.pptx`).

3. **Include Examples**:  
   Demonstrate, in a separate notebook or Python script, how you tested your hashing function’s performance (time, uniformity, etc.).

---

## Evaluation Criteria

Submissions will be judged according to the criteria outlined in `challenge.md`:

1. **Output determinism**
2. **Entropy Preservation**
3. **Computational Difficulty**
4. **Preimage & Collision Resistance**
5. **Feasibility** – Not exceeding 20 qubits for up to 256-bit inputs.
6. **Speed** – Reasonable execution times.
7. **Purely Quantum Hashing** – No offloading to classical hash functions.

Additional points (a lot of them) may be awarded for thorough proofs or analyses of your function, and the corresponding analysis of the Qubitcoin's hash algorithm.

---

## License & Attribution

All files in this repository, including the notebooks and challenge materials, are distributed for educational purposes.
