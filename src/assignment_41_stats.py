arr = [1, 17, 8, 25, 3]


def prob4(k_lim):
    return sum(pk(k) for k in range(1, k_lim))


def pk(k):
    return k**-5 if not 0 < k < 25 else 0


print("Problem 4 converging...")
print(prob4(10))
print(prob4(100))
print(prob4(1000))
print(prob4(10000))
print(prob4(100000))
print(prob4(1000000))
# The last 2 approximate to the same value
# This is what c is equal to
print("c =", 1/prob4(1000000))


def prob5():
    return sum(1443199.783*pk(k) for k in range(25, 31))


print("probability of k <= 30")
print(prob5())


def prob6():
    val = 0
    k = 25
    while val < .95:
        val += 1443199.783*pk(k)
        k += 1
    return k, val


print("0.95% sure k is...")
print(prob6())
