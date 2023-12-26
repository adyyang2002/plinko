import random
from collections import Counter

def odds():
    my_list = []
    for i in range(100):
        counter = 0
        for i in range(8):
            counter += random.choice([-.5, .5])
        my_list.append(int(counter))

    number_counts = Counter(my_list)

    # Sort the counts in descending order
    sorted_counts = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted counts
    for number, count in sorted_counts:
        print(f"Number {number} appeared {count} times")

def bucket_generator(num_rows, risk):
        bucket_list = []
        buckets = num_rows + 1
        counter = buckets * (risk + risk) * buckets
        multiplier = (risk + 1) * .8
        for x in range(buckets):
            if x < buckets/2:
                counter = counter / multiplier
            elif x == buckets/2:
                continue
            else:
                counter = counter * multiplier
            bucket_list.append(round(counter, 1))
        print(bucket_list)
# bucket_generator(16, 1)
# bucket_generator(16, 2)
# bucket_generator(16, 3)

def help(num_rows):
    for i in range(3, num_rows+2):
        print(i)

bucket = [0, 1, 2, 3, 4, 5, 6]

#odds()

def create_symmetric_exponential_list(n, max_val, min_val):
    mid_index = (n - 1) // 2
    a = max_val - min_val  # scaling factor
    b = (min_val / max_val) ** (1 / mid_index)# base for exponential decrease

    first_half = [round(a * b ** i + min_val, 1) for i in range(mid_index + 1)]
    second_half = first_half[::-1] if n % 2 == 0 else first_half[-2::-1]

    return first_half + second_half

# Example usage
rows = 16  # Length of the list
risk = 1
max_val = rows * rows * risk * risk  # Maximum value #rows times risk times rows * risk
min_val = (risk + risk) * (risk + risk) / (rows * rows)  # Minimum value
values = create_symmetric_exponential_list(rows, max_val, min_val)
print(values)