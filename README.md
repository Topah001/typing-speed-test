# Typing Speed Test

A dependency-free Python 3.13 terminal app. It displays a passage, accepts your typed version, and reports words per minute (five characters per word) and character accuracy. The scoring function is reusable and safely handles zero/negative elapsed times and empty input.

## Run

```powershell
py -3.13 typing_test.py
py -3.13 typing_test.py --prompt "Your own passage goes here."
```

## Test

```powershell
py -3.13 -m unittest discover -s tests -v
```