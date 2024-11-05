_NUMBER_STR_FROM_EMOJI_STR = {
    "0️⃣": "0",
    "1️⃣": "1",
    "2️⃣": "2",
    "3️⃣": "3",
    "4️⃣": "4",
    "5️⃣": "5",
    "6️⃣": "6",
    "7️⃣": "7",
    "8️⃣": "8",
    "9️⃣": "9",
    "🔟": "10",
    "💯": "100",
    "🅱️": "b",
    "🅾️": "o",
    "❌": "x",
}


class emj(str):
    def __int__(self) -> int:
        value = self
        base = self._detect_base(value)

        for emoji_str, number_str in _NUMBER_STR_FROM_EMOJI_STR.items():
            value = value.replace(emoji_str, number_str)
        return int(value, base=base)

    @staticmethod
    def _detect_base(value):
        base = 10
        if value.startswith("0️⃣🅱️"):
            base = 2
        elif value.startswith("0️⃣🅾️"):
            base = 8
        elif value.startswith("0️⃣❌"):
            base = 16
        return base
