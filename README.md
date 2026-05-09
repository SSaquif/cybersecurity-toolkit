# Security Toolkit

Collection of small cybersecurity and CTF helper tools.

## Current Tools

### Encoding Tool

Supports:

- Base64 encode/decode
- Hex encode/decode
- ASCII ↔ Binary conversion

## Usage

```bash
python encoding_tool.py b64-encode "hello"
```

## Running Tests

Run from the root of the project:

```bash
python -m unittest discover -s tests -v

# Or to run a specific test file:
python3 -m unittest tests.test_encoding_tool -v
```
