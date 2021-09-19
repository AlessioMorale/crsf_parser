#!/usr/bin/env python3
from crsf_parser.payloads import PacketsTypes
from crsf_parser import crsf_frame
from crsf_parser.handling import crsf_build_frame, crsf_frame_crc

frame = crsf_build_frame(
    PacketsTypes.RC_CHANNELS_PACKED,
    {"channels": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]},
)

data = crsf_frame.parse(frame)
print(crsf_frame.header.data_offset)
print(data, type(data))
print(frame, len(frame), type(frame))
crc_test_frame = b"\xc8\x18\x16\xde\x03\x9f.\xb4\xf7\x0b\xf0\x81\x0f|\xe0\x03\x1f\xf8(\x08\x00\x00D<\xe2\xff"
print(crc_test_frame)
