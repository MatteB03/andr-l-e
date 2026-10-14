import random
import csv
from pathlib import Path

folder = Path("files")
tries = 5
errors = 0

def read(name):
    with open(folder / name, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

x = [read("x_train.txt"), read("x_test.txt")]
y = [read("y_train.txt"), read("y_test.txt")] # THEY HAVE THE SAME LENGTH, 50-50 split
n = len(x[0])

def generate_random_guess():
    i = random.randint(0, 1)
    j = random.randrange(n)
    return x[i][j], y[i][j]

language_to_label = {}
with open(folder / "labels.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        language_to_label[row["English"]] = row["Label"]
label_to_language = {v: k for k, v in language_to_label.items()}

phrase, label = generate_random_guess()
correct_language = label_to_language[label]

print(f"the phrase is: {phrase}")
while errors < tries:
    name = input("What language is this? ").strip()

    if language_to_label.get(name) == label:
        print("Ma quanto sei forte?")
        break

    errors += 1
    if errors < tries:
        print(f"Azz hai sbagliato! Ti rimangono {tries-errors+1} tentativi")
else:
    print(f"Ci dispiace, hai perso! La label corretta era {correct_language}")