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
}


class emj(str):
    def __int__(self):
        value = self
        for emoji_str, number_str in _NUMBER_STR_FROM_EMOJI_STR.items():
            value = value.replace(emoji_str, number_str)
        return int(value)
