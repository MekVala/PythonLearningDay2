# Function Demo


def find_interest(p, n, r=3.5):
    intr = (p * r * n) / 100
    return intr


if __name__ == "__main__":
    print("Interest: ", find_interest(10000, 2))
