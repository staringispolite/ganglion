import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="processes audio time signatures to output a video with cuts that correspond to the times provided")
parser.add_argument('-i', metavar='path_beat',
    help='relative or abs path to beat signature CSV')
parser.add_argument('-v', metavar='path_video',
    help='relative or abs path to video file')
parser.add_argument('-s', metavar='sampling_rate',
    help='Percent (out of 100) of beats from which to randomly sample')

args = parser.parse_args()
print args

beat_sig = []
beat_durations = []
beat_sig_formatted = []
ffmpeg_commands = []

# Read the beat signature in
with open (args.i, "r") as myfile:
  beat_sig = myfile.read().replace('\n', '').split(',')
print "Read %d beat timecodes from %s" % (len(beat_sig), args.i)
print "timecodes:\n%r" % (beat_sig)

# Process into segment lengths between beats
last_beat = 0
for timecode in beat_sig:
  beat_durations.append(int(timecode) - last_beat)
  last_beat = int(timecode)
print "durations:\n%r" % (beat_durations)

# Translate beat durations from ms to hh:mm:ss.ms
for duration in beat_durations:
  dt = datetime.utcfromtimestamp(duration//1000)
  milliseconds = duration%1000
  dt_str = dt.strftime('%H:%M:%S')
  duration_formatted = "%s.%d" % (dt_str, milliseconds)
  beat_sig_formatted.append(duration_formatted)
print "durations formatted:\n%r" % (beat_sig_formatted)
