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


# Function to generate the MFCCs of the ref_oui_file and ref_non_file
def generate_mfcc(array_ref_oui, array_ref_non, array_tests):
    # create the MFCCs of the ref_oui_file and ref_non_file
    # calculate the 13 first vectors, delta and delta-delta
    array = array_ref_oui + array_ref_non + array_tests
    for i in range(len(array)):
        # get audio file
        y, sr = librosa.load(array[i])
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
        if not os.path.exists("test_mfcc_files"):
            os.makedirs("test_mfcc_files")
        mfcc_file = open(array[i].replace(".wav", ".mfcc").replace("audio", "mfcc"), "w")
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

    # check if the files exist
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
    generate_mfcc(array_ref_oui, array_ref_non, array_tests)

    # replace the .wav files by the .mfcc files
    for i in range(len(array_ref_oui)):
        array_ref_oui[i] = array_ref_oui[i].replace(".wav", ".mfcc").replace("audio", "mfcc")
    for i in range(len(array_ref_non)):
        array_ref_non[i] = array_ref_non[i].replace(".wav", ".mfcc").replace("audio", "mfcc")
    for i in range(len(array_tests)):
        array_tests[i] = array_tests[i].replace(".wav", ".mfcc").replace("audio", "mfcc")

    NB = 36

    # for each test file
    for j in range(len(array_tests)):
        # get the mfcc file
        mfcc_test_file = open(array_tests[j], "r")

        # get number of vectors of the mfcc file
        n = int(mfcc_test_file.readline().replace("Nombre de vecteurs : ", ""))

        X = [[0 for j in range(NB + 1)] for i in range(n + 1)]
        # for each vector of the mfcc file (except the first line) put the vector in X
        for i in range(1, n + 1):
            line = mfcc_test_file.readline().replace("Vecteur " + str(i) + " : ", "").split(" ")
            # remove last element of the list (empty string)
            line.pop()

            for j in range(0, NB):
                X[i][j] = line[j]
        X.pop(0)

        # for each oui file
        for k in range(len(array_ref_oui)):
            # get oui file mfcc
            mfcc_file_ref_oui = open(array_ref_oui[k], "r")

            # get number of vectors of the oui
            m = int(mfcc_file_ref_oui.readline().replace("Nombre de vecteurs : ", ""))

            # score of alignment
            M = [[0 for j in range(m + 1)] for i in range(n + 1)]

            # for each 'trame' of the audio file
            #for i in range(1, n + 1):
                # for each 'trame' of the oui file
                #for j in range(1, m + 1):
                    # M[i][j] = min(M[i - 1][j - 1], M[i][j - 1], M[i - 1][j]) + distance(mfcc_test_file[i - 1], mfcc_file_ref_oui[j - 1])

            # score of the alignment mean of the matrix
            #print(np.mean(M))


# Call main function
if __name__ == "__main__":
    main()