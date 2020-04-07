<!-- auto-generated using https://github.com/apocalypse-book/reverse-md.git -->
# reverse-md.py

This script reads from stdin and outputs to stdout.

Every line that starts with $1, where $1 is the first command lined parameter
is replaced by the line itself, everything else is surrounded by a ``` block
this process produces a markdown annotated source file.

If there is a second parameter, that parameter will be used as the language
of the code blocks
needed for sys.argv and sys.stdin
```python
import sys

def main():
```
the comment symbol that we use
```python
    comment = sys.argv[1]
```
the (optional) language, or nothing
```python
    lang = sys.argv[2] if len(sys.argv) > 2 else ""
```
the (optional) ignore symbol, or nothing
```python
    ignore = sys.argv[3] if len(sys.argv) > 3 else None
    block = None
```
shameless plug
```python
    print("<!-- auto-generated using https://github.com/apocalypse-book/reverse-md.git -->")
    for line in sys.stdin.readlines():
```
ignore all lines that start with the `ignore` symbol
```python
        if ignore is not None and line.lstrip().startswith(ignore):
            pass
```
we wanna skip leading spaces, like on this line <<<
```python
        elif line.lstrip().startswith(comment):
```
if we have a non-empty block saved, print it and set it to None
again
```python
            if block is not None and len(block) > 0 and not block.isspace():
                print(f"```{lang}")
                print(block.rstrip())
                print("```")
                block = None
```
strip leading spaces from md-comments
```python
            line = line.lstrip()[len(comment):-1].lstrip()
```
aaand finally print
```python
            print(line)
        else:
```
if we don't have a block yet, set it to an empty string
```python
            if block is None:
                block = ""
```
strip trailing spaces
```python
            line = line.rstrip()
```
if block is empty, and the line is either empty or contains only
spaces, skip it
```python
            if len(block) == 0 and (len(line) == 0 or line.isspace()):
                continue
```
else we add the line to the code block and append a newline
