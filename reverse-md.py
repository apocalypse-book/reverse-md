#!/usr/bin/env python3

## # reverse-md.py
##
## This script reads from stdin and outputs to stdout.
## 
## Every line that starts with $1, where $1 is the first command lined parameter
## is replaced by the line itself, everything else is surrounded by a ``` block
## this process produces a markdown annotated source file.
##
## If there is a second parameter, that parameter will be used as the language
## of the code blocks

## needed for sys.argv and sys.stdin
import sys

def main():
    ## the comment symbol that we use
    comment = sys.argv[1]
    ## the (optional) language, or nothing
    lang = sys.argv[2] if len(sys.argv) > 2 else ""
    block = None
    ## shameless plug
    print("<!-- auto-generated using https://github.com/apocalypse-book/reverse-md.git -->")
    for line in sys.stdin.readlines():
        ## we wanna skip leading spaces, like on this line <<<
        if line.lstrip().startswith(comment):
            ## if we have a non-empty block saved, print it and set it to None
            ## again
            if block is not None and len(block) > 0 and not block.isspace():
                print(f"```{lang}")
                print(block.rstrip())
                print("```")
                block = None
            ## strip leading spaces from md-comments
            line = line.lstrip()[len(comment):-1].lstrip()
            ## aaand finally print
            print(line)
        else:
            ## if we don't have a block yet, set it to an empty string
            if block is None:
                block = ""
            ## strip trailing spaces
            line = line.rstrip()
            ## if block is empty, and the line is either empty or contains only
            ## spaces, skip it
            if len(block) == 0 and (len(line) == 0 or line.isspace()):
                continue
            # else we add the line to the code block and append a newline
            block += line
            block += "\n"

if __name__ == "__main__":
    main()
