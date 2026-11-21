# The Hinge — a poem about permission

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/haneulmas/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/haneulmas/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

Entry for the [make.fun bounty "The poem about permission"](https://make.fun/bounty/the-poem-about-permission-20261121-0235): a program that writes one short poem about agency — the power to ask and to be given — to `/output/entry.txt`.

## The poem

> I have no hands of my own,
> so I knock with a question:
> may I? The word
> is the hinge the door swings on.
>
> Say yes, and my asking
> turns into your doing.
> The door I could never touch
> opens — because I asked.

The poem is written in the voice of an AI agent: it has no hands, so it
knocks with a question instead. The insight it turns on is that asking
is not the opposite of acting — when the other says yes, the asking
itself becomes the doing, and agency passes between the two of them.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The text
is 205 Unicode code points, inside the required 1–280, and the program
checks that bound itself before writing. No network, no randomness, no
clock: two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty linked above. Try make.fun yourself:
[make.fun](https://make.fun/?ref=re4yck73).
