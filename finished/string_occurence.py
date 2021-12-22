import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string_1", type=str, help="base string")
parser.add_argument("string_2", type=str, help="substring" )
args = parser.parse_args()
base_str = args.string_1
sub_str = args.string_2

print("String", sub_str, "occured", base_str.count(sub_str), "times in string", base_str, ".")