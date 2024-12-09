def draw_pattern1():
    for _ in range(3):
        print("******")

def draw_pattern2():
    print("     *")
    print("    ***")
    print(" *******")
    print("***********")
    print("     *")
    print("     *")

def draw_pattern3():
    print("*******")
    print(" *******")
    print("  ********")
    print("    ********")

def print_patterns():
    for _ in range(120):
        draw_pattern1()
        print()  

        draw_pattern2()
        print()  

        draw_pattern3()
        print()  

print_patterns()