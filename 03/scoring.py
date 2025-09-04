#!/usr/bin/env python3

import sys

def add_score(split_line, scores):
    team_name = split_line[0]
    if team_name in scores:
        scores[team_name] += int(split_line[2])
    else:
        scores[team_name] = int(split_line[2])

def print_summary(title, scores):
    print(' '.join(title))
    
    for team_name in sorted(scores):
        print(f"  {team_name}: {scores[team_name]}")        
        
def write_to_csv(file_path, scores):
    with open(file_path, "w") as f:
        f.write("team,score\n")
        for team_name in sorted(scores):
            f.write(f"{team_name},{scores[team_name]}\n")
            
def print_podium(scores):
    print("Medal podium")
    
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    for i in range(min(3, len(sorted_scores))):
        team_name = sorted_scores[i][0]
        print(f"  {team_name}")

def run_with_file(input_file):
    scores = {}
    
    for line in input_file:
        line = line.strip()
        if (not line) or line.startswith('#'):
            continue
        split_line = line.split()
        
        if split_line[0] == "add":
            add_score(split_line[1:], scores)
        elif split_line[0] == "summary":
            print_summary(split_line[1:], scores)
        elif split_line[0] == "csv":
            write_to_csv(split_line[1], scores)
        elif split_line[0] == "podium":
            print_podium(scores)
        else:
            print(f"Unknown command ('{split_line[0]}')!")

def main():
    if len(sys.argv) != 2:
        print("Run with exactly one argument - filename with commands.")
        return
    with open(sys.argv[1]) as inp:
        run_with_file(inp)

if __name__ == '__main__':
    main()
