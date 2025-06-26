---
title: "Numerical Derivative Summary"
date: 2025-04-27 12:27:00 +0000
categories: [study, posts]
tags: [Calculus]
---

1. What is a Numerical Derivative?
If the function f(x) is known explicitly, we can calculate derivatives analytically.
But if:
The function is not explicitly known, and only discrete data points are available,
Or the function is too complex to differentiate analytically,
then we use numerical methods to approximate the derivative.

2. Types of Numerical Derivative Approximations
a. Forward Difference Approximation
f'(x₀) ≈ (f(x₁) - f(x₀)) / h
       = (f₁ - f₀) / h

b. Backward Difference Approximation
f'(x₀) ≈ (f(x₀) - f(x₋₁)) / h
       = (f₀ - f₋₁) / h

Central Difference Approximation
f'(x₀) ≈ (f(x₁) - f(x₋₁)) / (2h)
       = (f₁ - f₋₁) / (2h)
Central difference has better accuracy (error term is O(h²)).

3. Second Derivative Approximations
a. Central Difference (Second Order)
f''(x₀) ≈ (f₋₁ - 2f₀ + f₁) / h²

4. Higher Accuracy Approximations
First Derivative (4-point central difference, O(h⁴)):
f'(x₀) ≈ (-f(x₂) + 8f(x₁) - 8f(x₋₁) + f(x₋₂)) / (12h)

Second Derivative (5-point central difference, O(h⁴)):
f''(x₀) ≈ (-f(x₂) + 16f(x₁) - 30f(x₀) + 16f(x₋₁) - f(x₋₂)) / (12h²)

5. Formula Derivations
Numerical derivative formulas can be derived using:

Taylor Series Expansion

Interpolation Polynomials (e.g. Newton-Gregory)

6. Practical Example
Given table data:
x      f(x)
1.3    3.669
1.5    4.482
1.7    5.474
1.9    6.686
2.1    8.166
2.3    9.974
2.5   12.182

To compute f′ (1.7) using central difference with h = 0.2:
f'(1.7) ≈ (f(1.9) - f(1.5)) / (2h)
       ≈ (6.686 - 4.482) / 0.4
       ≈ 5.510

7. Application in Image Processing
Edge detection in digital images uses numerical derivatives.

The first derivative is used to detect sharp changes in intensity (edges).

The Laplacian (second derivative) is used for precise edge location.

