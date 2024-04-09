import argparse, pickle

def openResults(file):
    with open(file, 'rb') as handle:
        resDict = pickle.load(handle)
        handle.close()
        return(resDict)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-alpha', '--alphaGenes', action='store', nargs='?', help='imgt alpha genes', type=str)
    parser.add_argument('-beta', '--betaGenes', action='store', nargs='?', help='imgt beta genes', type=str)
    return parser.parse_args()

# Call this function to retrieve AA sequence dictionaries
if __name__ == '__main__':
    args = parse_args()
    if args.alphaGenes is not None:
        alp = openResults(args.alphaGenes)
        print(alp)
    if args.betaGenes is not None:
        bet = openResults(args.betaGenes)
        print(bet)