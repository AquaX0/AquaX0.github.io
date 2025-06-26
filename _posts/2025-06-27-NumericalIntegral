---
title: "Numerical Integral Summary"
date: 2025-06-27 12:27:00 +0000
categories: [study, posts]
tags: [Calculus]
---

1. What is Numerical Integration?
Numerical integration is a method to approximate the definite integral of a function when:

The function is too complex to integrate analytically.

The function is only known at discrete points (tabular data).

It estimates the area under a curve using rectangles, trapezoids, or parabolas.

2. Common Methods
A. Rectangle Rule (Kaidah Segi empat)
Approximate each strip as a rectangle.

Left endpoint:
∫ f(x) dx ≈ h * f(x₀)

Right Endpoint:
∫ f(x) dx ≈ h * f(x₁)

Composite Version:
∫ from a to b f(x) dx ≈ h * [f₀ + f₁ + ... + fₙ₋₁]

B. Trapezoidal Rule (Kaidah Trapesium)
Approximate each strip as a trapezoid.

Single interval:
∫ from a to b f(x) dx ≈ (h / 2) * [f(a) + f(b)]

Composite rule (with n intervals):
∫ f(x) dx ≈ (h / 2) * [f₀ + 2f₁ + 2f₂ + ... + 2fₙ₋₁ + fₙ]

C. Midpoint Rule (Kaidah Titik Tengah)
Uses the midpoint of each interval.

For n intervals:
∫ f(x) dx ≈ h * [f(x₁/₂) + f(x₃/₂) + ... + f(xₙ₋₁/₂)]

3. Error Estimation
Trapezoidal Rule Error:
E ≈ -[(b - a) * h² / 12] * f ''(t), for some t in [a, b]
⇒ Order of Error: O(h²)

Midpoint Rule Error:
E ≈ [(b - a) * h² / 24] * f ''(t)
⇒ Also O(h²), but typically more accurate than trapezoidal

4. Simpson’s 1/3 Rule
Uses a parabolic approximation through 3 points.

For even n:
∫ from a to b f(x) dx ≈ (h / 3) * [f₀ + 4f₁ + 2f₂ + 4f₃ + ... + 4fₙ₋₁ + fₙ]
More accurate, but requires even number of subintervals.

Error:
E ≈ -[(b - a) * h⁴ / 180] * f ⁽⁴⁾(t)
⇒ Order of Error: O(h⁴)
5. Practical Use
Used in:
- Engineering (e.g., RMS current, heat flux)

- Physics (e.g., area under experimental data curves)

- Computer simulations and graphics