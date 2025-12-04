import re

HEX_FILTER = ''.join([chr(i) if len(repr(chr(i))) == 3 else '.' for i in range(256)])

def hexdump(src, length=16, show=True, to_file=False, filename="hexdump.txt"):
    if isinstance(src, bytes):
        src = src.decode(errors='ignore')

    results = []
    
    for i in range(0, len(src), length):
        word = str(src[i:i + length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hex_width = length * 3

        results.append(f'{i:04x}  {hexa:<{hex_width}}  {printable}')

    output = "\n".join(results)
    
    if show:
        print(output)
    
    if to_file:
        with open(filename, 'w') as file:
            file.write(output)
        print(f"Hexdump saved to {filename}")

    return results

if __name__ == "__main__":
    data = b"Here's a test with some non-ASCII characters: \x01\x02\x03"
    hexdump(data, length=16, show=True, to_file=True, filename="hexdump_output.txt")
