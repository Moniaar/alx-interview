# UTF-8 Validation project
In order to effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

---

## Plan
### Identify Valid Byte Patterns:

UTF-8 encoding follows specific patterns for 1 to 4 byte sequences:
1-byte: 0xxxxxxx
2-byte: 110xxxxx 10xxxxxx
3-byte: 1110xxxx 10xxxxxx 10xxxxxx
4-byte: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
### Validation Rules:

For each byte, check the most significant bits (MSBs) to determine the expected length of the sequence.
For each sequence, subsequent bytes should match the 10xxxxxx pattern.
Ensure that the number of continuation bytes matches the expectation set by the leading byte.
### Algorithm Steps:

1. Traverse each byte in the data.
2. Identify the sequence type based on the leading byte.
3. Check the subsequent bytes to validate the pattern.
4. Return True if all sequences are valid, otherwise return False.

### Pseudocode
- Initialize a counter for the number of bytes in the current UTF-8 character.
- Loop through each byte in the data list:
- If the byte starts a new sequence (based on MSBs), set the expected number of bytes.
- For continuation bytes, check they match the 10xxxxxx pattern.
- Ensure all sequences are validated by the end of the loop.
