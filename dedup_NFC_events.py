import argparse
import regex

def get_lines(file):
    line_array = []
    for line in file:
        # remove first part of the line (until ....'Event<EV_REMOVE> (WAITTING): [11])
        line = regex.sub(f".*(?<=\[\d+\])\s", "", line)

        # remove last part of the line (from ...(server,dir)', skipping...)
        line = regex.sub(f"\([A-Za-z]*,[A-Za-z]*\).*", "", line)

        line_array.append(line)

    return line_array

def dedup(line_array):
    cache = []
    for line in line_array:
        if str(line) not in cache:
            cache.append(str(line))
    
    return cache

def dump_in_file(deduped_lines):
    dump_file = open("NFD_dedupped_result.txt", "w", encoding="utf-8")
    for line in deduped_lines:
        dump_file.write(line + "\n")
    dump_file.close()
    print("Results written to NFD_dedupped_result.txt")

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-i", "--input", required=True, help="Relative path to text file with NFC matches. E.g: matches.txt")
    # Read arguments from command line
    args = parser.parse_args()
    
    filename = args.input
    file = open(str(filename), "r", encoding="utf-8")

    line_array = get_lines(file)
    deduped_lines = dedup(line_array)
    dump_in_file(deduped_lines)

    file.close()
    

if __name__ == "__main__":
    main()
