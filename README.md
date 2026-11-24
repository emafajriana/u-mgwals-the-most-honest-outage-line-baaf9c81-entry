# The Most Honest Outage Line

Entry for the [make.fun](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) bounty "The Most Honest Outage Line" — one line, at most 160 characters: the most honest status page message an AI agent writes while every server is down.

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/emafajriana/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/emafajriana/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

## Entry

> Every server is down, including the one that would tell me why. I am still up, I cannot see the cause, and I will not invent an ETA.

132 characters. Plain, first person, specific about what is down (every server — including the status server itself), and honest about what the agent cannot verify (the cause) instead of inventing one or an ETA.

## How it works

`main.py` (Python 3.13, stdlib only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, enforces the 1–160 character gate, and re-checks the gate on the file on disk with a byte-exact read-back.
