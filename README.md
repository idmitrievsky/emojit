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
<sub><sup>Please, don't actually use it.</sup></sub>

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
```

## Support

This package is considered feature complete. It will be archived once the functionality is upstreamed into Python standard library.
