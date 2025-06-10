# Python argv parser


Yet another args parser.
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
2. __Unkown_Flag__ optional method that raises Exception if some unknown flag was given.
