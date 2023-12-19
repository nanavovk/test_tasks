import argparse

parser = argparse.ArgumentParser(description='Circular array')
parser.add_argument('array_initiator', type=int, help='circular array')
parser.add_argument('array_length', type=int, help='length')
args = parser.parse_args()
current_array = [0] * args.array_length

if args.array_initiator == 0:
    print('Число, задающее массив, должно быть больше 0')
elif args.array_length == 0:
    print('Число, задающее путь, должно быть больше 0')

result_array = []
circle_array = [i for i in range(1, args.array_initiator + 1)]
saved_index = 0
end_digit = 0

while end_digit != 1:
    i = saved_index
    for j in range(0, args.array_length):
        current_array[j] = circle_array[i]
        if i == len(circle_array) - 1:
            saved_index = i
            i = 0
            continue
        saved_index = i
        i += 1

    print(current_array)
    result_array.append(current_array[0])
    end_digit = current_array[args.array_length - 1]
    current_array = [0] * args.array_length

print(*result_array, sep='')
