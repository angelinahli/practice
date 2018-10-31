
def run(filename):
    with open(filename, "r") as fl:
        txt = fl.read()
    lines = txt.split("\n")[:-1]
    header = lines[0]
    num_ast = int(lines[1])
    coords = [ [int(n) for n in v.strip().split(" ")] for v in lines[2:] ]

if __name__ == "__main__":
    tc1 = "sample1.txt"
    tc2 = "sample2.txt"
    run(tc1)
