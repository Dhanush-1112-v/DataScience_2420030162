
# Probability Distributions using Python
# 1. Bernoulli Distribution
# 2. Binomial Distribution
# Application: Student Exam Pass/Fail Analysis

import numpy as np
from scipy.stats import bernoulli, binom

# Bernoulli Distribution
print("----- Bernoulli Distribution -----")

# Probability of passing an exam
p = 0.7

# Generate random outcomes for 10 students
# 1 represents Pass and 0 represents Fail
bernoulli_samples = bernoulli.rvs(p, size=10)

print("Probability of Passing:", p)
print("Student Outcomes (1=Pass, 0=Fail):")
print(bernoulli_samples)

# Calculate probability of passing
print("\nProbability of Pass:")
print(bernoulli.pmf(1, p))

# Calculate probability of failing
print("Probability of Fail:")
print(bernoulli.pmf(0, p))

# Binomial Distribution
print("\n----- Binomial Distribution -----")

# Total number of students
n = 10

# Probability of passing each exam
p = 0.7

# Number of students expected to pass
k = 8

# Calculate probability that exactly 8 students pass
binomial_probability = binom.pmf(k, n, p)

print("Number of Students:", n)
print("Probability of Passing:", p)
print(f"\nProbability that exactly {k} students pass:")
print(binomial_probability)

# Generate random binomial outcomes for 5 experiments
random_binomial = binom.rvs(n, p, size=5)

print("\nRandom Binomial Outcomes:")
print(random_binomial)
