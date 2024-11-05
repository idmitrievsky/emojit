from emojit import emj


def test_emj():
    s = emj("2️⃣0️⃣💯")
    assert isinstance(s, str)
    assert int(s) == 20100


def test_visual_separator():
    assert int(emj("4️⃣0️⃣2️⃣_0️⃣0️⃣0️⃣")) == 402_000


def test_shorthand():
    assert int(emj("🔟")) == int(emj("1️⃣0️⃣"))
    assert int(emj("💯")) == int(emj("1️⃣0️⃣0️⃣"))
