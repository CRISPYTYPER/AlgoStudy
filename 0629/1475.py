import math

def get_result(n):
    number_list = [0] * 10

    for num in number:
        number_list[ord(num)-48] += 1

    num_six = number_list[6]
    num_nine = number_list[9]

    avg_six_nine = math.ceil((num_six + num_nine)/2)

    number_list[6] = avg_six_nine
    number_list[9] = avg_six_nine
    return max(number_list)


number = input()
print(get_result(number))