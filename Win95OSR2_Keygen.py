import random
import argparse

def generate_oem_key():
    day_of_year = random.randint(100, 365)
    year = random.randint(95, 99)

    while True:
        number = f"{random.randint(0, 999999):06}"
        digit_sum = sum(int(d) for d in number)
        if digit_sum % 7 == 0 and number[-1] not in ['0', '8', '9']:
            middle_block = "0" + number
            break

    last_block = ''.join(str(random.randint(0,9)) for _ in range(5))

    # Sestavení klíče
    return f"{day_of_year}{year}-OEM-{middle_block}-{last_block}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, default=1, help="Počet generovaných klíčů")
    args = parser.parse_args()

    keys = [generate_oem_key() for _ in range(args.count)]

    for key in keys:
        print(key)

    save = input("Uložit do souboru? (A/N): ").strip().lower()

    if save == "a":
        with open("oem_keys.txt", "w") as file:
            for key in keys:
                file.write(key + "\n")
        print("Klíče byly uloženy do oem_keys.txt")