from collections import defaultdict

# default dict
# when retreiving using a key that doesn't exist, return the default value. In this case, return the default value of int, which is 0
s_dict = defaultdict(int)
s_dict[
    "my key"
] += 1  # increments value for my key. if my key is not present, set the default value as 0 then increment it

# this returns cache miss
s_dict = defaultdict(lambda: "cache miss")
print(s_dict["test"])


# for a dictionary, you cannot have a list be a key. to get around this, you have to covert the list into a tuple like so
my_dict = defaultdict(list)
count = [1, 2, 3]
count_tuple = tuple(count)
my_dict[count_tuple] = "my value"
print(my_dict)
