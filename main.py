"""Write the Tired Dark Lord monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate: UTF-8 text, 1-600 characters, not whitespace-only, about 100 words.
"""
import os
import sys
import tempfile

ENTRY = (
    "The goblins have formed a union. They want weekends. Weekends. "
    "I conquered the Ashen Reaches before breakfast\u2014before breakfast\u2014and "
    "now I must sit across a table from Grubnuk the shop steward and "
    "discuss dental. Dental! For goblins. My scheme was simple: raise "
    "the dead, march on Valdris, take the throne. Instead I am here, "
    "signing a grievance form, while the skeleton crew\u2014literal "
    "skeletons\u2014picket the gate with signs they spelled wrong. Fine. "
    "Take your weekends. But the dead stay dead on company time, and "
    "the throne... the throne can wait till Monday. It has waited three "
    "hundred years."
)


def main() -> int:
    text = ENTRY
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= 600):
        raise ValueError(f"entry length {len(text)} outside 1-600 chars")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    words = text.split()
    if not (80 <= len(words) <= 120):
        raise ValueError(f"word count {len(words)} outside 80-120")
    data = text.encode("utf-8")
    # Round-trip check: valid UTF-8.
    data.decode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry.", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, target)
        # Read-back verification: the file on disk must be byte-identical
        # to what we intended to write.
        with open(target, "rb") as f:
            if f.read() != data:
                raise IOError("read-back verification failed: entry.txt differs from intended bytes")
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
