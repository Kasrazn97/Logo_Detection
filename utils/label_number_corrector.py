import in_place
import os
import argparse


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inpDir', help='path to the labels')

    opt = parser.parse_args()
    return opt

def main(opt):
    for label in os.listdir(opt.inpDir):
        with in_place.InPlace(os.path.join(opt.inpDir, label)) as file:
            for line in file:
                if int(line.split(' ', 1)[0]) == 1:
                    line = '6' +' '+ line.split(' ', 1)[1]
                file.write(line)

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)