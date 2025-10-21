# Emojit

This package aims to address a long-standing Python issue:
```python
int("1️⃣") != 1
```

## Usage

```python
from emojit import emj

emoji_str = emj("4️⃣0️⃣2️⃣")

assert isinstance(emoji_str, str) is True
assert int(emoji_str) == 402
```
<sub><sup>Please, don't actually use this.</sup></sub>

## Simplified usage

You can simplify the previous example as:
```python
# coding: emoji-digit

emoji_str = "4️⃣0️⃣2️⃣"

assert isinstance(emoji_str, str) is True
assert int(emoji_str) == 402
```

To achieve this, you first need to find your `site-packages` directory:
```shell
python -c "import site; print(site.getsitepackages())"
```

And then create a new file called `sitecustomize.py` in this directory with the following contents:
```python
import builtins
import codecs

import emojit
import emojit.emoji_digit_codec

builtins.emj = emojit.emj

codecs.register(emojit.emoji_digit_codec.search_function)
```

You can read more about codecs [here](https://docs.python.org/3/library/codecs.html).

## Advanced usage

### Underscores as visual separators

```python
from emojit import emj

assert int(emj("4️⃣0️⃣2️⃣_0️⃣0️⃣0️⃣")) == 402_000
```

### Shorthand emojis

```python
from emojit import emj

assert int(emj("🔟")) == int(emj("1️⃣0️⃣"))
assert int(emj("💯")) == int(emj("1️⃣0️⃣0️⃣"))
assert int(emj("🔢")) == int(emj("1️⃣2️⃣3️⃣4️⃣"))
```

## Support

This package is considered feature complete. It will be archived once the functionality is upstreamed into the Python standard library.
