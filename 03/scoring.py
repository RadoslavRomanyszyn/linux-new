#!/usr/bin/env python3

import sys

def run_with_file(input_file):
    scores = {}
    for line in input_file:
        line = line.strip()
        if (not line) or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0] == "summary":
            print(' '.join(parts[1:]))
            for name in sorted(scores):
                print("  {}: {}".format(name, scores[name]))
        elif parts[0] == "add":
            name = parts[1]
            if name in scores:
                scores[name] += int(parts[3])
            else:
                scores[name] = int(parts[3])
        elif parts[0] == "csv":
            with open(parts[1], "w") as f:
                f.write("team,score\n")
                for name in sorted(scores):
                    f.write("{},{}\n".format(name, scores[name]))
        else:
            print("Unknown command ('{}')!".format(parts[0]))

def main():
    if len(sys.argv) != 2:
        print("Run with exactly one argument - filename with commands.")
        return
    with open(sys.argv[1]) as inp:
        run_with_file(inp)

if __name__ == '__main__':
    main()
