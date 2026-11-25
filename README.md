# The Tired Dark Lord

[![The Tired Dark Lord](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Nadanese93/tired-dark-lord/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Nadanese93/tired-dark-lord/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

A 100-word villain monologue for [The Tired Dark Lord: A 100-Word Villain Monologue](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) on make.fun.

The Dark Lord conquered the Ashen Reaches before breakfast — and now he must sit across a table from Grubnuk the shop steward and discuss dental. For goblins. The dead can wait till Monday; the throne has waited three hundred years.

## How it works

`main.py` writes the monologue to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), validating the gate first: UTF-8 text, 1–600 characters, not whitespace-only, 80–120 words. The write is atomic (temp file + `os.replace`) and verified by re-reading the file after the write.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
