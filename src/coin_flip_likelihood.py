import matplotlib.pyplot as plt


def compute_likelihood(p, sequence):
    return p**sequence.count("H") * (1-p)**sequence.count("T")


# Problem A
# L(p = 0.5 | HHTTH) = P(H) * P(H) * P(T) * P(T) * P(H)
#                    = .5 * .5 * .5 * .5 * .5 = (.5)^5 = .03125
print("Problem A: ", compute_likelihood(.5, "HHTTH"))


# Problem B
# L(p = 0.55 | HHTTH) = P(H) * P(H) * P(T) * P(T) * P(H)
#                    = .55 * .55 * .45 * .45 * .55 = (.55)^3 * (.45)^2 = .03369
print("Problem B: ", round(compute_likelihood(.55, "HHTTH"), 5))

# Problem C
# L(p | HHTTH) = P(H) * P(H) * P(T) * P(T) * P(H)
#              = p * p * (1-p) * (1-p) * p = (p)^3 * (1-p)^2 = .03369

# Problem D
# Get x value as p, and y value as the likelihood
x_vals, y_vals = zip(*((i/100, compute_likelihood(i/100, "HHTTH"))
                       for i in range(100)))
plt.plot(x_vals, y_vals)
plt.savefig("coin_flip_likelihood.png")
