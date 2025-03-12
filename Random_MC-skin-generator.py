import random
import struct
import zlib
import os

def png_chunk(chunk_type, data):
    """Creates a PNG chunk with the given type and data."""
    chunk = chunk_type.encode() + data
    return struct.pack(">I", len(data)) + chunk + struct.pack(">I", zlib.crc32(chunk))

def generate_random_skin():
    width, height = 64, 64
    filename = os.path.join(os.path.expanduser("~"), "Desktop", "random_skin.png")


    # Generate raw pixel data (RGBA: 4 bytes per pixel)
    raw_data = b""
    for y in range(height):
        raw_data += b"\x00"  # Filter type 0 (None)
        for _ in range(width):
            raw_data += bytes([random.randint(0, 255) for _ in range(4)])  # RGBA

    # PNG file signature
    png_signature = b"\x89PNG\r\n\x1a\n"

    # IHDR chunk (Image header)
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)  # 8-bit, RGBA
    ihdr_chunk = png_chunk("IHDR", ihdr_data)

    # IDAT chunk (Image data, compressed)
    compressed_data = zlib.compress(raw_data)
    idat_chunk = png_chunk("IDAT", compressed_data)

    # IEND chunk (End of PNG)
    iend_chunk = png_chunk("IEND", b"")

    # Write the PNG file
    with open(filename, "wb") as f:
        f.write(png_signature + ihdr_chunk + idat_chunk + iend_chunk)

    print(f"Random Minecraft skin saved as: {filename}")
    print(f"Skin saved at: {os.path.abspath(filename)}")


generate_random_skin()



