## Author: BRANCATI Silvio, BRIOT Anthony
## Année Universitaire: 2022-2023

# import libraries
import sys
import os
import librosa
import numpy as np

# Variables
n_mfcc = 13 # Number of MFCC coeffs
ref_oui_file = ""
ref_non_file = ""
tests_file = ""

# Function to preaccentuate the signal
def preaccentuation(signal):
    signaldec = np.roll(signal, 1)
    signaldec[0] = 0
    output = signal - 0.97 * signaldec
    return output

# Function to generate the MFCCs of the ref_oui_file and ref_non_file
def generate_mfcc(array_ref_oui, array_ref_non):
    # create the MFCCs of the ref_oui_file
    # calculate the 13 first vectors, delta and delta-delta
    array_refs = array_ref_oui + array_ref_non
    for i in range(len(array_refs)):
        # get audio file
        y, sr = librosa.load(array_refs[i])
        y = preaccentuation(y)
        win_length = 25 * sr // 1000
        hop_length = 10 * sr // 1000
        fen = np.hamming(win_length)

        # get MFCCs
        mfccs = librosa.feature.mfcc(y=y, sr=sr, win_length=win_length, hop_length=hop_length, n_mfcc=n_mfcc, window=fen)

        # get delta
        delta = librosa.feature.delta(mfccs)

        # get delta-delta
        delta_delta = librosa.feature.delta(mfccs, order=2)

        # generate the .mfcc file
        # Vecteur i : [12 coeffs MFCCs] [12 coeffs delta] [12 coeffs delta-delta]
        # create folder mfcc_files if it doesn't exist
        if not os.path.exists("mfcc_files"):
            os.makedirs("mfcc_files")
        mfcc_file = open(array_refs[i].replace(".wav", ".mfcc").replace("audio", "mfcc"), "w")
        mfcc_file.write("Nombre de vecteurs : " + str(len(mfccs[0])) + "\n")
        mfccs_transpose = mfccs.T
        delta_transpose = delta.T
        delta_delta_transpose = delta_delta.T
        for j in range(len(mfccs_transpose)):
            mfcc_file.write("Vecteur " + str(j+1) + " : ")
            for k in range(1, 13):
                mfcc_file.write(str(mfccs_transpose[j][k]) + " ")
            for k in range(1, 13):
                mfcc_file.write(str(delta_transpose[j][k]) + " ")
            for k in range(1, 13):
                mfcc_file.write(str(delta_delta_transpose[j][k]) + " ")
            mfcc_file.write("\n")
        mfcc_file.close()

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

    # read the tests_file

    for file in [ref_oui_file, ref_non_file, tests_file]:
        if not os.path.exists(file):
            print("Error: " + file + " does not exist")
            sys.exit(1)

        # check if the file is empty
        if os.stat(file).st_size == 0:
            print("Error: " + file + " is empty")
            sys.exit(1)

    # read the tests_file
    array_tests = []
    with open(tests_file, "r") as f:
        for line in f:
            if line != "\n":
                array_tests.append(line.replace("\n", ""))

    # read the ref_oui_file
    array_ref_oui = []
    with open(ref_oui_file, "r") as f:
        for line in f:
            if line != "\n":
                array_ref_oui.append(line.replace("\n", ""))

    # read the ref_non_file
    array_ref_non = []
    with open(ref_non_file, "r") as f:
        for line in f:
            if line != "\n":
                array_ref_non.append(line.replace("\n", ""))

    # create the MFCCs of the ref_oui_file and ref_non_file
    generate_mfcc(array_ref_oui, array_ref_non)

# Call main function
if __name__ == "__main__":
    main()