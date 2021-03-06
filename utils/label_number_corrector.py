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
                    line = '2' +' '+ line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 2:
                    line = '3' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 3:
                    line = '4' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 4:
                    line = '6' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 5:
                    line = '7' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 6:
                    line = '8' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 7:
                    line = '10' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 8:
                    line = '11' + ' ' + line.split(' ', 1)[1]
                elif int(line.split(' ', 1)[0]) == 9:
                    line = '12' + ' ' + line.split(' ', 1)[1]
                file.write(line)

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)