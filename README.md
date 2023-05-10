# Python argv parser


Yet another argv parser written by me. Just to make my own life easier.
Showcase:
``` console
$  python3 pyargv.py -f -s hello -m hello world -n include_me
```
## Features
1. Supports flags and function-flags (with input).
2. You can set some flags as nessasary, python will raise excpetion if none was included.
3. All checking is applied: no function-flags without input and so on.

## TODO
1. __Usage__ method, thats sets string as default output after "-h" tag and before raise of Exception.
2. __Unkown_Flag__ optional method to detect flags that raises Exception if some unknown flag was given.
