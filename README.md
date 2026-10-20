# Simple RSA Cryptosystem in Python

A lightweight, native Python implementation of the **RSA (Rivest–Shamir–Adleman)** public-key cryptosystem. This project is built entirely from scratch without using any external cryptographic libraries, demonstrating the fundamental math behind key generation, encryption, and decryption.

## 📌 Features
* **Custom Primality Test:** Implements a trial division check to discover prime numbers.
* **Extended Euclidean Algorithm:** Features a custom Modular Multiplicative Inverse function to generate the private exponent d.
* **Character-by-Character Encryption:** Encrypts and decrypts text strings by mapping characters to their Unicode (`ord()`) values.
* **Interactive CLI:** Prompts the user for input and displays the generated keys, encrypted tokens, and decrypted text instantly.

## 🛠 Project Structure & Functions

The script consists of the following core components:
* `check_on_common_numbers(q)`: Validates whether a generated number is prime using a square-root optimized trial division loop.
* `generator_e(N)`: Searches for a public exponent e that is prime and coprime to the Euler's totient function φ(N).
* `generator_d(e, N)`: Computes the private key exponent d using a custom Extended Euclidean Algorithm approach.
* `RSA_generator_keys()`: Generates random prime bounds (10,000 to 1,000,000) for p and q, computes n and φ(F), and returns the public parameters.
* `RSA_encode(text, e, n)`: Encrypts plain text into a list of integers using modular exponentiation (`pow(char, e, n)`).
* `RSA_decode(encode, d, n)`: Reverses the cipher integers back into the human-readable text string using `pow(cipher, d, n)`.

## 💻 Quick Start

### Prerequisites
* Python 3.x (No external dependencies required).

### Usage Example Output
```text
Input text: Hello RSA!
Public key n: 429107931443
Public key e: 60757
[30807038101, 19283741029, ... ]
Hello RSA!
```

## ⚠️ Important Disclaimer (Educational Only)
This repository is created exclusively for **educational and demonstration purposes**. 
* **Key Size:** The prime generation bounds (10,000 to 1,000,000) create keys that are far too small for real-world applications and can be easily brute-forced in milliseconds.
* **Lack of Padding:** It uses "textbook RSA" without secure padding schemes (like OAEP or PSS). This makes it highly vulnerable to frequency analysis and known-plaintext attacks.
* **Entropy:** It relies on Python's standard pseudo-random `random` module instead of a cryptographically secure source like `secrets`.

**Do not use this implementation to protect any sensitive or production data.**

