def parent(num):
    def first_child(x):
        return num+x

    def second_child(x):
        return num*x

    if num < 10:
        return first_child
    else:
        return second_child

