f = open("3-input.txt", "r")
input = f.read().splitlines()

total = len(input)
digits = len(str(input[0]))

str_input = [str(x) for x in input]

def get_rating(l, mode="oxygen"):
    for idx in range(digits):
        count = 0
        for option in l:
            if int(option[idx]):
                count += 1
            filt = "1" if count >= len(l)/2 else "0"
            if mode == "C02":
                filt = "1" if filt == "0" else "0"

        l = list(filter(lambda x: x[idx] == filt, l))
        if len(l) == 1:
            break
    
    return int(l[0], 2)

oxygen_generator_rating = get_rating(str_input)
C02_generator_rating = get_rating(str_input, "C02")

print(oxygen_generator_rating * C02_generator_rating)