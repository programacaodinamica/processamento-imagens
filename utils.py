import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)