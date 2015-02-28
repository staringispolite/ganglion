# ganglion /ˈɡaNGɡlēən/ (noun)

![Ganglion image](http://upload.wikimedia.org/wikipedia/commons/9/9f/Gray933.png)

The [cochlear ganglion](http://en.wikipedia.org/wiki/Spiral_ganglion) is the group of nerve cells that serve the sense of hearing by sending a representation of sound from the cochlea to the brain.

Ganglion is a Python script that processes audio time signatures output by [Cochlea](https://github.com/staringispolite/cochlea) (comma separated millisecond values), and parses that along with video input, to output a video with cuts that fit the beat time signature.

eg, the following command processes /path/to/video.mp4 according to a random sampling of 25% the beats in /home/beat_sig.csv:
>  /home> python ganglion -i cesare_vs_disorder_beat_sig.csv -v /path/to/woodkid_video.mp4 -s 25

Resulted in:
https://www.youtube.com/watch?v=PKi-RV_VsUY
