import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    
    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            count_lines = 0
            for line in lines:
                if not check_lines(line):
                    count_lines += 1
            print(count_lines)         
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
