import sys
sys.set_int_max_str_digits(100_000)

depth = 100000
running_count = 2
for x in range(depth):
    running_count = running_count*2
    if str(running_count)[0:7] == "8675309":
        print("success")
        print(x)
        break
    else:
        print(x)

# checked up to 2^64735 and it hasn't found it yet, maybe brute force is not the best way to go