## Author: BRANCATI Silvio, BRIOT Anthony
## Année Universitaire: 2022-2023

# Variables
win_length = 250000.0 # = 25 ms = length of a time frame
hop_length = 100000.0 # = 10 ms = frame periodicity
n_mfcc = 13 # Number of MFCC coeffs
audio_file = "audio_files/oui_01.wav" # Default audio file

# main function
def main():
    # get the path of the audio file in argument
    if (len(sys.argv) > 2):
        print("Usage: python main.py <audio_file_path>")
        exit(1)
    if (len(sys.argv) == 2):
        audio_file = sys.argv[1]

    print("Hello World!")

# Call main function
if __name__ == "__main__":
    main()