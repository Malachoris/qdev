# qdev

The task is to implement the Linux command line utility "[grep](https://man7.org/linux/man-pages/man1/grep.1.html)”. 
The subset of all features that you should focus on:
- Parsing of CLI flags & arguments
- Simple patterns searching
- Parallel searching*

Support for:
### part 1
- -E, --extended-regexp  (same as python’s `re` module)
- -i, --ignore-case
- -c, --count
- -n, --line-number
- -A NUM, --after-context=NUM
- -B NUM, --before-context=NUM
- -C NUM, -NUM, --context=NUM
- -exclude=GLOB
- --include=GLOB
- -r, --recursive

### part 2
- -f FILE, --file=FILE
- -L, --files-without-match
- -l, --files-with-matches
- --group-separator=SEP
- --exclude-from=FILE
- --exclude-dir=GLOB
- -H, --with-filename