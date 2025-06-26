---
title: "Derivative Summary"
date: 2025-03-27 12:27:00 +0000
categories: [study, posts]
tags: [Calculus]
---

1. What is a Derivative?
A derivative represents the rate of change or slope of a function at a particular point. It is defined as the limit of the average rate of change as the interval approaches zero.

2. The Tangent Line Problem
A tangent line to a curve touches it at exactly one point and has the same slope as the curve at that point.

To approximate the slope of the tangent, we use the slope of a secant line, which is:
(f(x) - f(a)) / (x - a)
As x approaches a, this expression becomes the derivative:
f'(a) = lim(x→a) [(f(x) - f(a)) / (x - a)]
This gives the instantaneous rate of change at x = a.

3. The Velocity Problem
In motion problems, velocity is the derivative of position with respect to time.

The average velocity over a time interval is:
[s(t + h) - s(t)] / h

The instantaneous velocity at time t is the limit of this expression as h → 0:
v(t) = lim(h→0) [(s(t + h) - s(t)) / h]
This is exactly the definition of the derivative of s(t).

4. Key Concepts
The derivative measures how fast a quantity changes.

It is geometrically interpreted as the slope of the tangent line.

It is physically interpreted as instantaneous speed or rate.

5. Derivative Notation
Different notations for derivatives include:

f '(x)

dy/dx

d/dx [f(x)]

The chain rule is a method for finding the derivative of composite functions.
If a function is defined as: y = f(g(x)). Then the derivative is dy/dx = f'(g(x)) * g'(x) or more generally dy/dx = dy/du * du/dx.
u = g(x) is the inner function
y = f(u) is the outer function

How to Apply the Chain Rule
1) Identify the inner and outer functions.

2) Differentiate the outer function, leaving the inner function as it is.

3) Multiply by the derivative of the inner function.

Examples
1) y = (3x + x²)²
Inner: u = 3x + x²
Outer: f(u) = u²
dy/dx = 2(3x + x²) * (3 + 2x)

2) y = √(3x + x²)
= (3x + x²)^(1/2)
dy/dx = (1/2)(3x + x²)^(-1/2) * (3 + 2x)

3) y = (−2t⁴ + 7t)⁵
Inner: u = −2t⁴ + 7t
Outer: f(u) = u⁵
dy/dt = 5(−2t⁴ + 7t)⁴ * (−8t³ + 7)

4) y = (3x³ + 2x² − 4x)⁻⁴
dy/dx = −4(3x³ + 2x² − 4x)⁻⁵ * (9x² + 4x − 4)


Chain Rule with Other Rules
A. Product Rule + Chain Rule:
y = (4x³ + 5)(3x³ − x²)²
Use product rule: u·v' + v·u'
Where v' uses chain rule.

B. Quotient Rule + Chain Rule:
y = x / (x³ + 7x + 4)^(1/3)
Apply quotient rule and use chain rule on denominator.

Applications
Tangent Line at a Point:
Use the chain rule to find dy/dx, then plug in x to find the slope and use:
y - y₁ = m(x - x₁)
Compound Interest:
If A = P(1 + r/m)^(mt), then dA/dr involves applying the chain rule with:

Inner: u = 1 + r/m

Outer: A = P·u^(mt)

Exponential & Logarithmic Functions
Exponential Example:
y = 5e^(2x)
dy/dx = 5 * e^(2x) * 2 = 10e^(2x)
Logarithmic Example:
y = ln(2x)
dy/dx = (1 / 2x) * 2 = 1/x
