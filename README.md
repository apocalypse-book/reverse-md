<!-- auto-generated using https://github.com/apocalypse-book/reverse-md.git -->
# reverse-md

reverse-md is a tool to easily convert code into markdown.
Comments like this: `///`, which can be easily configured to be a different
symbol, are converted into markdown, while everything else is transformed
into a markdown code block.

See the source of this README.md file at [README.c](/README.c)

## Instructions

Simply run `./reverse-md.py /// c <README.c >README.md` to generate this
README.md file.  You can replace the `///` with a different comment symbol,
or you can replace the (optional) `c` with a different language. For
example, to create an annotated python file with md behind a ## comment, run
`./reverse-md.py ## python <reverse-md.py >reverse-md.md`

## reverse-md demo

This is an annotated example of reverse-md

declare a main function
```c
int main() {
```
this is how you declare a variable
```c
    int x = 0;
```
this is a pointer to x
```c
    int xptr = &x;
    // since we use /// to annotate md-blocks, we can use regular comments, too

    printf("%d %p", x, (void *) xptr);
```
this was a bigger block containing 3 lines
```c
}
```
## The end

This example worked properly
