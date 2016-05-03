def find_our_instances():
    our_instances = []
    inst_numbers = []
    possible = []
    for i in range(1,493):
        with open("instances/{0}.in".format(str(i)), "r") as inst:
            if inst.readline().strip() == "500" and inst.readline().strip() == "":
                possible.append(i)
    print("{0} possible...".format(len(possible)))
    for i in possible:
        print("checking {0}".format(i))
        with open("instances/{0}.in".format(str(i)), "r") as inst:
            with open("part1/TMDW1.in".format(str(i)), "r") as src1:
                with open("part1/TMDW2.in".format(str(i)), "r") as src2:
                    with open("part1/TMDW3.in".format(str(i)), "r") as src3:
                        for _ in range(492):
                            keys = []
                            keys.append(src1.readline())
                            keys.append(src2.readline())
                            keys.append(src3.readline())
                            if inst.readline() not in keys:
                                break
                        inst_numbers.append(i)
    return inst_numbers

print(find_our_instances())