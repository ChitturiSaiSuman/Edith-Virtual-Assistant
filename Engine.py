# Utility Program to call Actual Assistant

import os

def main():
    os.chdir("Assistant")
    os.system("python3 Assistant.py")

if __name__ == '__main__':
    main()