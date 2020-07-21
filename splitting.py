g = "world hello"
print(f"g is the string: {g}")
print(f"g.split() is {g.split()}")

L = g.split()
sorted_list = sorted(L)
print(f"Sorted list: {sorted_list}")

new_string = "".join(sorted_list)
print(new_string)
