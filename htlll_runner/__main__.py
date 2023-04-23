import sys
from html.parser import HTMLParser

class HTLLLParser(HTMLParser):
    pass


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m htlll_runner <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if not filename.endswith(".htlll"):
        print("Error: File must end with .htlll")
        sys.exit(1)
    with open(filename, "r") as file:
        code = file.readlines()
        for i in range(len(code)):
            line = code[i]
            line = line.strip()
            if line.startswith("#"):
                continue
            code[i] = line
        code = "\n".join(code)
    
    parser = HTLLLParser()
    parser.feed(code)
    print(parser.commands)