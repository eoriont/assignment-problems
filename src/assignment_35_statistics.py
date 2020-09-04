
def expected_val(x):
    return sum(i*prob for i, prob in enumerate(x))


def variance(x):
    expected = expected_val(x)
    return sum(y*(i - expected)**2 for i, y in enumerate(x))


def stdev(x):
    return variance(x)**.5


# Calculate the probability for all amounts of heads, where 0 < heads < num_flips
def prob_distribution(num_flips, bias=0.5):
    return [probability(i, num_flips, bias) for i in range(num_flips+1)]


# Calculate the probability for x heads in y number of flips
def probability(num_heads, num_flips, bias=0.5):
    outcomes_perm = factorial(
        num_flips) / (factorial(num_flips - num_heads) * factorial(num_heads))
    return outcomes_perm * bias**num_heads * (1-bias)**(num_flips-num_heads)


def factorial(num):
    return 1 if num == 0 else factorial(num-1) * num


# A:

# HHHH
# HHHT
# HHTH
# HHTT
# HTHH
# HTHT
# HTTH
# HTTT
# THHH
# THHT
# THTH
# THTT
# TTHH
# TTHT
# TTTH
# TTTT

# 1
dist = prob_distribution(4)
# [(.5)^4, 4*.5(.5)^3, 6*(.5)^2(.5)^2, 4(.5)^3*.5, (.5)^4]
print("Probability distribution for x:", dist)

# 2
# Intuitively, the expected value of x is 2 because the bias is .5, so half of the flips will be heads.

# 3
# Calculate the expected val
# 0*0.0625 + 1*0.25 + 2*.375 + 3*.25 + 4*0.0625
print("Expected value of x:", expected_val(dist))

# 4
# 0.0625 * (0 - 2)^2 + 0.25 * (1-2)^2 + 0.375 * (2-2)^2 + 0.25 * (3-2)^2 + 0.0625 * (4-2)^2 = 1
print("Variance of x:", variance(dist))

# 5
# Sqrt(var(x)) = 1
print("Standard deviation of x:", stdev(dist))

# Part B

# Prob distribution:
# [(1-λ)^4, 4λ(1-λ)^3, 6λ^2(1-λ)^2, 4λ^3(1-λ), λ^4]

# Intuitive expected value:
# 4λ

# Actual expected value:
# 4λ(1-λ)^3 +                 12λ^2(1-λ)^2 +          12λ^3(1-λ) + 4λ^4
# 4λ(1-3λ+3λ^2-λ^3) +         12λ^2(1-2λ+λ^2) +       12λ^3 - 12λ^4 + 4λ^4
# 4λ - 12λ^2 + 12λ^3 - 4λ^4 + 12λ^2 - 24λ^3 + 12λ^4 + 12λ^3 - 12λ^4 + 4λ^4
# 4λ

# Variance:
# (1-λ)^4 * (0-4λ)^2 + 4λ(1-λ)^3 * (1-4λ)^2 + 6λ^2(1-λ)^2 * (2-4λ)^2 + 4λ^3(1-λ) * (3 - 4λ)^2 + λ^4 * (4 - 4λ)^2
# According to symbolab
# = 4λ(1 - λ)


# Standard Deviation (square root of the variance):
# sqrt(4λ(1 - λ))
