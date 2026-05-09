import base64
import argparse

# Usage:
# python encoding_tool.py b64-enc Hello
# python encoding_tool.py b64-enc --encoding utf-16 "Hello World"

# b64encode returns bytes and not a string
# the .decode() converts the bytes to python string
def b64_encode(text, encoding="utf-8"):
    print(f"Encoding '{text}' using {encoding} encoding and Base64...")
    raw_bytes = text.encode(encoding)
    encoded_bytes = base64.b64encode(raw_bytes)
    # Base64 output is ASCII-safe, so decode it as ASCII instead of the input text encoding.
    encoded_str = encoded_bytes.decode("ascii")
    return encoded_str
    # return base64.b64encode(text.encode(encoding)).decode()


def b64_decode(text, encoding="utf-8"):        
    decoded_bytes = base64.b64decode(text)
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str
    # return base64.b64decode(text).decode(encoding)


def hex_encode(text, encoding="utf-8"):
    return text.encode(encoding).hex()


def hex_decode(text, encoding="utf-8"):
    return bytes.fromhex(text).decode(encoding)


def ascii_to_bin(text, encoding=None):
    return " ".join(format(ord(char), "08b") for char in text)


def bin_to_ascii(binary, encoding=None):
    chars = binary.split()
    return "".join(chr(int(b, 2)) for b in chars)


def main():
    parser = argparse.ArgumentParser(
        description="Encoding and Decoding Utility"
    )

    parser.add_argument(
        "operation",
        choices=[
            "b64-enc",
            "b64-dec",
            "hex-enc",
            "hex-dec",
            "ascii-to-bin",
            "bin-to-ascii",
        ],
        help="Operation to perform"
    )
 
    parser.add_argument(
        "--encoding",
        default="utf-8",
        choices=["utf-8", "utf-16", "latin-1", "cp1252", "ascii"],
        help="Text encoding (utf-8, utf-16, latin-1, cp1252, ascii, etc.)"
    )

    parser.add_argument(
        "input",
        help="Input string"
    )

    args = parser.parse_args()

    operations = {
        "b64-enc": b64_encode,
        "b64-dec": b64_decode,
        "hex-enc": hex_encode,
        "hex-dec": hex_decode,
        "ascii-to-bin": ascii_to_bin,
        "bin-to-ascii": bin_to_ascii,
    }

    result = operations[args.operation](args.input, args.encoding)

    print(result)


if __name__ == "__main__":
    main()