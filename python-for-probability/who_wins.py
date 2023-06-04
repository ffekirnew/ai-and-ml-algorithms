import numpy as np


def simulate():
    total = 0
    while total <= 100:
        player_1 = np.random.randint(1, 101)
        total += player_1

    while total <= 200:
        player_2 = np.random.randint(1, 101)
        total += player_2

    # print("Winner: " + ("Player 1" if player_1 >= player_2 else "Player 2"))
    return 1 if player_1 >= player_2 else 0


def main():
    player_1_score = 0
    player_2_score = 0
    for i in range(100_000):
        if simulate():
            player_1_score += 1
        else:
            player_2_score += 1

    print("Player 1:", np.round(player_1_score / 100_000, 3))
    print("Player 2:", np.round(player_2_score / 100_000, 3))


if __name__ == "__main__":
    main()
