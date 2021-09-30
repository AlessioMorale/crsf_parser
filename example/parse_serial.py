#!/usr/bin/env python3
from operator import contains
from typing import Container
from crsf_parser import CRSFParser
from serial import Serial

from crsf_parser.payloads import PacketsTypes
from crsf_parser import crsf_frame
from crsf_parser.handling import crsf_build_frame


def print_frame(frame: Container) -> None:
    print(frame)


crsf_parser = CRSFParser(print_frame)
n = 10
v = 1
with Serial("/dev/ttyUSB0", 425000, timeout=2) as ser:
    input = bytearray()
    while True:
        if n == 0:
            n = 10
            frame = crsf_build_frame(
                PacketsTypes.BATTERY_SENSOR,
                {"voltage": v, "current": 1, "capacity": 100, "remaining": 100},
            )
            v += 1
            ser.write(frame)
        n = n - 1
        values = ser.read(100)
        input.extend(values)
        crsf_parser.parse_stream(input)
