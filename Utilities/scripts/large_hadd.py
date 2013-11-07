#!/usr/bin/env python

import sys
import os
import argparse

def hadd(outfile, infiles):
    cmd = "hadd " + outfile + " " + " ".join(infiles)
    os.system(cmd)


def batch_hadd(outfile, infiles, n_files=200):
    split_infiles = [infiles[x:x+n_files]
                     for x in xrange(0, len(infiles), n_files)]

    intermediate_files = []

    user_name = os.environ['USER']

    for i in xrange(len(split_infiles)):
        intm_file = ("/tmp/tmp_" + user_name + "_" + str(i) + "_" +
                     os.path.basename(outfile))
        print intm_file
        intermediate_files.append(intm_file)
        hadd(intm_file, split_infiles[i])

    hadd(outfile, intermediate_files)

    #os.system("rm " + " ".join(intermediate_files))


def parse_command_line(argv):
    parser = argparse.ArgumentParser(description='Run hadd on a large number '
                                                 'of ROOT files')
    parser.add_argument('outfile', type=str,
                        help='The name of the output ROOT file.')
    parser.add_argument('infiles', nargs='+',
                        help='A list of input ROOT files to merge.')
    parser.add_argument('--max-jobs', type=int, default=1,
                        help='How many instances of hadd should run at once?')
    args = parser.parse_args(argv)

    return args

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = parse_command_line(argv)

    batch_hadd(args.outfile, args.infiles)
    
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)
