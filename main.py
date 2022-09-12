import argparse
from io import TextIOWrapper
import sys


KB = 1024
MB = KB * 1024
GB = MB * 1024


def write_in_file(file: TextIOWrapper, value: int, filename: str):
    if value > 200 * MB:
        end = value / (MB * 100)
        written = 0
        progress = 0
        for i in range(int(end)):
            file.write("." * (MB * 100))
            written += MB * 100
            progress = int((written / value) * 100)
            sys.stdout.write("\rProgress: %i%%" % (progress))
            sys.stdout.flush()
        left_to_write = value - written
        file.write("." * left_to_write)
        sys.stdout.write("\rProgress: 100%%\nDone. Your file is here: %s\n" % filename)
        sys.stdout.flush()
    else:
        file.write("." * value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-kb", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-mb", type=int, help="Size in Kilobyte of the content", default=0)
    parser.add_argument("-gb", type=int, help="Size in Gigabyte of the content", default=0)
    parser.add_argument("-o", help="Output filepath", default="output.txt")

    args = parser.parse_args()
    f = open(args.o, "a")
    to_write = args.b + args.kb * KB + args.mb * MB + args.gb * GB
    write_in_file(f, to_write, args.o)
    f.close()
