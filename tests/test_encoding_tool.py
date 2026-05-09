import base64
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "crypto"))

import encoding_tool as et


class EncodingToolTests(unittest.TestCase):
    def test_b64_encode_uses_ascii_output(self):
        self.assertEqual(et.b64_encode("hello", "utf-8"), "aGVsbG8=")

    def test_b64_round_trip_with_utf16(self):
        original = "Hello World"
        encoded = et.b64_encode(original, "utf-16")

        self.assertEqual(
            encoded,
            base64.b64encode(original.encode("utf-16")).decode("ascii"),
        )
        self.assertEqual(et.b64_decode(encoded, "utf-16"), original)

    def test_hex_round_trip_with_non_default_encoding(self):
        original = "café"
        encoded = et.hex_encode(original, "latin-1")

        self.assertEqual(encoded, original.encode("latin-1").hex())
        self.assertEqual(et.hex_decode(encoded, "latin-1"), original)

    def test_ascii_binary_round_trip(self):
        original = "AB"
        encoded = et.ascii_to_bin(original)

        self.assertEqual(encoded, "01000001 01000010")
        self.assertEqual(et.bin_to_ascii(encoded), original)

    def test_main_dispatches_ascii_to_bin(self):
        argv = ["encoding_tool.py", "ascii-to-bin", "A"]
        stdout = io.StringIO()

        with redirect_stdout(stdout):
            old_argv = sys.argv
            try:
                sys.argv = argv
                et.main()
            finally:
                sys.argv = old_argv

        self.assertEqual(stdout.getvalue().splitlines()[-1], "01000001")


if __name__ == "__main__":
    unittest.main()