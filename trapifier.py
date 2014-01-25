#!/usr/bin/env python
import pydub
import random
import argparse
import os

# Take command-line arguments for input and output files
# (And maybe directory to sample from)
parser = argparse.ArgumentParser(description="Turn boring sound files into \
                                 Real Trap Shit.")
parser.add_argument("inputfile", metavar='inputfile',
                    help="The input file, a mp3, wav, ogg, or flv")
parser.add_argument("outputfile", metavar='outputfile',
                    help="The output filename")
parser.add_argument("--samples", nargs='?',
                    help="The directory to look in \
                    for samples.  Defaults to \"samples\"")


# Get a file extension for a given file
def extension(file):
    ext = os.path.splitext(file)[-1].lower()
    return ext


# Turn arguments into variables
def parse():
    # Interpret the input file based on its codec
    if extension(inputfile) == ".wav":
        base_track = pydub.AudioSegment.from_wav(inputfile)
    elif extension(inputfile) == ".mp3":
        base_track = pydub.AudioSegment.from_mp3(inputfile)
    elif extension(inputfile) == ".ogg":
        base_track = pydub.AudioSegment.from_ogg(inputfile)
    elif extension(inputfile) == ".flv":
        base_track = pydub.AudioSegment.from_flv(inputfile)
    else:
        raise NameError("Please use a .wav, .mp3, .ogg, or .flv file as input")

    # Check if we're using custom samples
    if args.samples:
        sample_dir = args.samples
    else:
        sample_dir = "samples"

    return_value = [base_track, sample_dir]
    return return_value


# Actually put the samples over the base track
def overlay(parsed_values):

    base_track = parsed_values[0]
    sample_dir = parsed_values[1]
    output = base_track
    break_length = 0
    not_done = False

    while not_done is False:
        # Pick out a random sample to overlay
        overlay_sound_file = random.choice(os.listdir(sample_dir))
        # Parse it based on its codec
        if extension(overlay_sound_file) == ".wav":
            overlay_sound = pydub.AudioSegment.from_wav(os.path.join(str(
                sample_dir), overlay_sound_file))
        else:
            overlay_sound = pydub.AudioSegment.from_mp3(os.path.join(str(
                sample_dir), overlay_sound_file))

        # Put it over the track
        output = output.overlay(overlay_sound, position=break_length)

        # Pick out a length from 1.5 - 6 seconds to wait
        break_length += random.randrange(1500, 6000)

        # If we'd be waiting until the track ended, stop the loop
        if break_length > len(base_track):
            not_done = True

    # Save the file as an MP3
    print "Success!"
    output.export(outputfile, format="mp3")

# Actually do things
if __name__ == "__main__":
    args = parser.parse_args()
    inputfile = args.inputfile
    outputfile = args.outputfile
    overlay(parse())
