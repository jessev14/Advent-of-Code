f = open("3-input.txt", "r")
input = f.read().splitlines()

total = len(input)
collection_list = []

for i in input:
    str_i = str(i)
    for idx, bit in enumerate(str_i):
        if len(collection_list) < idx + 1:
            collection_list.append(0)
        
        if int(bit):
            collection_list[idx] += 1


gamma_binary_str = ""
epsilon_binary_str = ""

for bit in collection_list:
    if bit > total/2:
        gamma_binary_str += "1"
        epsilon_binary_str += "0"
    else:
        gamma_binary_str += "0"
        epsilon_binary_str += "1"

gamma_decimal = int(gamma_binary_str, 2)
epsilon_decimal = int(epsilon_binary_str, 2)

print(gamma_decimal * epsilon_decimal)
