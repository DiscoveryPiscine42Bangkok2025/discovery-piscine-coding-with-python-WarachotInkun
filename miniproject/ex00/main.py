#!/usr/bin/env python3
from checkmate import checkmate
def main():
    board = """\
.....
.....
..B.B
.....
KP..R\
""" 
    checkmate(board)
if __name__ == "__main__":
    main()