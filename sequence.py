def sequence():
    first, diff, terms = int(input("Please enter the first term of a sequence: ")), int(input("Please enter the common difference: ")), int(input("Please enter the amount of terms you would like to display: "))

    seq = 0
    for i in range(0, terms):
        seq += first
        first += diff
        print(f"Term {i + 1}: {seq}")

if __name__ == "__main__":
    sequence()
