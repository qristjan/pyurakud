from matemaatika import matemaatika
import re

while True:
    numbers = input("Enter add/multiplication equation (like '3 + 5'/'3 * 5') or 'END' to stop the calculator: ")
    if str(numbers) == "END":
        exit(1)
    if "+" in str(numbers):
        print(matemaatika.liida(*[int(n) for n in re.sub(r"\s", "", numbers).split("+")]))
    if "*" in str(numbers):
        print(matemaatika.korruta(*[int(n) for n in re.sub(r"\s", "", numbers).split("*")]))
