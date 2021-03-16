from matemaatika import matemaatika
import re

while True:
    numbers = input("Enter add equation (like '3 + 5') or 'END' to stop the calculator: ")
    if str(numbers) == "END":
        exit(1)
    print(matemaatika.liida(*[int(n) for n in re.sub(r"\s", "", numbers).split("+")]))
