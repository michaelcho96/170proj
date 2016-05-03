from utils import *

def find_small_graphs():
    solved = do_not_test_set("COMBINED SOLUTIONS")
    short = []
    for i in range(1,493):
        if i not in solved:
            with open("instances/{0}.in".format(str(i)), "r") as inst:
                if int(inst.readline()) < 15:
                    short.append(i)
    return short

print(find_small_graphs())