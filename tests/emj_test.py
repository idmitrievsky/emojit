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


def test_base_2():
    assert int(emj("0️⃣🅱️1️⃣1️⃣")) == 3


def test_base_8():
    assert int(emj("0️⃣🅾️🔟")) == 8


def test_base_16():
    assert int(emj("0️⃣❌DEADBEEF")) == 3735928559
