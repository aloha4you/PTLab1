# -*- coding: utf-8 -*-
import argparse
import sys

from CalcClassman import CalcClassman
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.endswith("txt"):
        reader = TextDataReader()
    else:
        reader = XmlDataReader()

    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    classmans = CalcClassman(students).calc()
    print("Classman (names, count of all classmans): ", classmans)


if __name__ == "__main__":
    main()
