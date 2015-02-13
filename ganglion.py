import argparse

parser = argparse.ArgumentParser(description="processes audio time signatures to output a video with cuts that correspond to the times provided")
parser.add_argument('-i', metavar='path_beat',
                     help='relative or abs path to beat signature CSV')
parser.add_argument('-v', metavar='path_video',
                     help='relative or abs path to video file')
parser.add_argument('-s', metavar='sampling_rate',
                     help='Percent (out of 100) of beats from which to randomly sample')

args = parser.parse_args()

print args
