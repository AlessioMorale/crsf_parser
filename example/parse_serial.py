#!/usr/bin/env python3
from operator import contains
from typing import Container
from crsf_parser import CRSFParser
from serial import Serial
# test = bytearray(
#     b"\xc8\x18\x16\xfe\xa2\xe6\x02\xbb\x0b\xf0\x81\x0f|\xe0\x03\x8f\x88\x08\x00D\x12\x1c\xc8d\xe47\xf4\xe6\x82\xf7\x0b\xf0\xc1\x88\x81\x03\x84(\x08\x00\x00D<\xe2\xfc\xc8\x98\x917\xfa.\xa0\xf7\x0b\xf0\x81\x0f|\xf0\xa0\x84(\x08\x00D<\xe2\xef\xc8\x18\x16\xde#\x9f.\xa0\xf7!\x81\x0f|\xe0\x03\x1f\xf8(\x88\x00\x14\x12\xef\xc8\x18\x16\xde"
# )

def print_frame(frame: Container)-> None:
    print(frame)

crsf_parser = CRSFParser(print_frame)

with Serial("/dev/ttyUSB0", 425000, timeout=2) as ser:
    input = bytearray()
    while True:
        values = ser.read(100)
        input.extend(values)
        crsf_parser.parse_stream(input)
