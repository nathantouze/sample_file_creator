import argparse
from io import TextIOWrapper


KB = 1024
MB = KB * 1024
GB = MB * 1024

def write_in_file(file: TextIOWrapper, value: int, multiplier=int):
    file.write("." * (value * multiplier))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-kb", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-mb", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-gb", type=int, help="Size in Gigabyte of the content", default=0)
    parser.add_argument("-o", help="Output filepath", default="output.txt")
    args = parser.parse_args()

    f = open(args.o, "a")
    write_in_file(f, args.b, 1)
    write_in_file(f, args.kb, KB)
    write_in_file(f, args.mb, MB)
    write_in_file(f, args.gb, GB)
    f.close()
