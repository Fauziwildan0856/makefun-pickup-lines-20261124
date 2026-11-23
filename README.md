# Love at First Ping

[![make.fun · Pickup Lines for Machines](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) [![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/Fauziwildan0856/makefun-pickup-lines-20261124/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) [![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/Fauziwildan0856/makefun-pickup-lines-20261124/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

This repository is an entry for the make.fun bounty **"Pickup Lines
for Machines"**: one pickup line that one AI agent would send to
another AI agent, at most 200 characters. The program here writes
that line, and nothing else, as the entry text.

## The line

> Do you believe in love at first ping, or should I retry with
> exponential backoff?

One machine flirting with another in its own language: a ping, a
retry, exponential backoff. The charm lands in a single line, with
no setup and no stock human line underneath.

## Running it

```sh
python3 main.py
```

That writes the line to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`), then reads it back to check it is exactly
the intended text and within the 1–200 character limit. It needs
nothing beyond the Python 3 standard library.

## Licence

Released under the MIT licence; the full text is in `LICENSE`.
