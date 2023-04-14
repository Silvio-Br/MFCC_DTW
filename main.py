## Author: BRANCATI Silvio, BRIOT Anthony
## Année Universitaire: 2022-2023

# import libraries
import sys

# Variables
win_length = 250000.0 # = 25 ms = length of a time frame
hop_length = 100000.0 # = 10 ms = frame periodicity
n_mfcc = 13 # Number of MFCC coeffs
ref_oui_file = ""
ref_non_file = ""
tests_file = ""

# main function
def main():
    if (len(sys.argv) != 4):
        print("Usage: python main.py <Ref_OUI.txt> <Ref_NON.txt> <Tests.txt>")
        sys.exit(1)

    # take in arguments the 3 txt files
    if (len(sys.argv) == 4):
        ref_oui_file = sys.argv[1]
        ref_non_file = sys.argv[2]
        tests_file = sys.argv[3]

    print("Hello World!")

# Call main function
if __name__ == "__main__":
    main()