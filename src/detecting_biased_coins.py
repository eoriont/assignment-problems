from coin_flipping import dict_to_list
import matplotlib.pyplot as plt
plt.style.use("bmh")

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH', 'TTH', 'TTH', 'TTH', 'THT', 'TTH', 'HTH', 'HTH',
          'TTT', 'HTH', 'HTH', 'TTH', 'HTH', 'TTT', 'TTT', 'TTT', 'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH', 'THH', 'HHH', 'HHH', 'HTT', 'TTH', 'TTH', 'HHT',
          'TTH', 'HTH', 'HHT', 'THT', 'THH', 'THT', 'TTH', 'TTT', 'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH', 'HHT', 'HHT', 'HHH', 'TTT', 'THH', 'HHH', 'HHH',
          'TTH', 'THH', 'THH', 'TTH', 'HTT', 'TTH', 'HTT', 'HHT', 'TTH', 'HTH', 'THT', 'THT', 'HTH']


def plot_probabilities(probabilities):
    # Graph them
    x_vals = [0, 1, 2, 3]
    for i, probs in enumerate(probabilities):
        line_width = 2.5 if i == 0 else 0.75
        plt.plot(x_vals, probs, linewidth=line_width)

    plt.legend(["Coin 1", "Coin 2", "Coin 3"])
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability")
    plt.title("Coin Flipping Bias")
    plt.show()


probs = []
for coin in [coin_1, coin_2, coin_3]:
    coin_probs = {}
    for trial in coin:
        trial = trial.count('H')
        if trial in coin_probs:
            coin_probs[trial] += 1
        else:
            coin_probs[trial] = 1
    probs.append(dict_to_list(coin_probs, 3))
print(probs)
plot_probabilities(probs)

# Coin 1 is definitly biased towards tails, coin 2 is the normal coin, and coin 3 is biased towards heads.
