import codecs
import re

pattern = re.compile(r"""((["'])((?:0️⃣|1️⃣|2️⃣|3️⃣|4️⃣|5️⃣|6️⃣|7️⃣|8️⃣|9️⃣|🔟|💯)+)\2)""")


class EmojiDigitIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input_bytes, final=False):
        text = input_bytes.decode("utf-8", self.errors)
        transformed = re.sub(pattern, r"emj(\1)", text)
        return transformed


class EmojiDigitIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input_string, final=False):
        return input_string.encode("utf-8", self.errors)


def emoji_digit_decode(input_bytes, errors="strict"):
    """Decode function that wraps emoji-digit string literals with an `emj` call."""
    text = bytes(input_bytes).decode("utf-8", errors)
    transformed = re.sub(pattern, r"emj(\1)", text)
    return transformed, len(input_bytes)


class EmojiDigitStreamReader(codecs.StreamReader):
    decode = emoji_digit_decode


def emoji_digit_encode(input_string, errors="strict"):
    """Encode function (just uses UTF-8)"""
    return input_string.encode("utf-8", errors), len(input_string)


class EmojiDigitStreamWriter(codecs.StreamWriter):
    encode = emoji_digit_encode


def search_function(encoding_name):
    if encoding_name == "emoji_digit":
        return codecs.CodecInfo(
            name="emoji-digit",
            encode=emoji_digit_encode,
            decode=emoji_digit_decode,
            incrementalencoder=EmojiDigitIncrementalEncoder,
            incrementaldecoder=EmojiDigitIncrementalDecoder,
            streamreader=EmojiDigitStreamReader,
            streamwriter=EmojiDigitStreamWriter,
        )
    return None
