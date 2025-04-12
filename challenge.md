# Superquantum's Challenge Description

One of the center pieces of the proof-of-work concept used in cryptocurrencies is an existence of a certain hash function, which is resilient to preimage attacks. This provides a way for the blockchain participants to know for certain that a meaningful amount of computational work has been performed to find an input that results in a specific output of that function. Our challenge is centered around a goal of developing a high-quality hash function based on the simulation of quantum circuits to be used in quantum-powered blockchain systems.

As for the more specific challenge requirements, the students will be required to develop a hash function in Python using their quantum simulator of choice. The input to this function will be an array of <em>2<sup>N</sup></em> bytes, where <em>N</em> can be any natural number greater than or equal to 5, and the function must produce the byte output of the same size. The function can only utilize the resulting expectation values for each qubit after conducting quantum simulations.

The grading will be based on the following criteria:

1. Output determinism - the function must always produce the same output for a given input.
2. Preservation of entropy - provided that the function receives random samples from the uniform distribution over its domain, its outputs should, on average, be distributed as uniformly as possible over its range.
3. Computational difficulty - the function should not be computable in sub-exponential time complexity in the number of input bits.
4. Preimage resistance - the inverse of the function should not be trivially computable.
5. Collision resistance - there should be no trivial way to find two distinct input values for which the hash function produces the same output.
6. Computational feasibility - the function should not utilize the simulation of circuits with the number of qubits exceeding 20 for any number of input bits not exceeding 256.
7. Computation time - the average time taken to calculate a single hash value should be as low as possible.
8. Purely quantum hashing - the function must not use any classical hash function on the inputs to and the outputs from the quantum circuit.

Some of these criteria will be judged quantitatively using a set of predetermined metrics for the hash function’s performance (strict avalanche criterion, bit independence, etc.), while others, such as the computational difficulty, will be evaluated by manually inspecting the structure of the hash function.

For each of the listed criteria, the contestants are encouraged to prove their function’s compliance or quantify its performance, to gain additional points. Another way to improve the team’s standing is to do the same analysis for the quantum portion of the Qubitcoin’s qhash algorithm for the criteria 1-5.

Lastly, as a bonus problem, contestants can try to develop a hash function that can accept variable-length input and produce fixed-length 256 bit output. It is advised to take on this challenge only after designing and analysing a solution to the main problem.

The contestants are required to include the following materials in their final submission:

- <em>main.py</em>, along with other necessary Python files, implementing the proposed hash function. The function should take <em>bytes</em> as input, return <em>bytes</em>, and be clearly marked in the code with appropriate comments.
- <em>requirements.txt</em>, listing the necessary Python packages for executing main.py
- <em>writeup.pdf</em>, detailing the work performed by the team and covering all obtained results
- any additional Python scripts/notebooks containing the analysis code used in the write-up
- <em>presentation.pptx</em>, containing the team's solution presentation
