#!/usr/bin/env python3
from crsf_parser.payloads import PacketsTypes
from crsf_parser import crsf_frame
from crsf_parser.handling import crsf_build_frame

frame = crsf_build_frame(
    PacketsTypes.RC_CHANNELS_PACKED,
    {"channels": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]},
)

data = crsf_frame.parse(frame)
print(crsf_frame.header.data_offset)
print(data, type(data))
print(frame, len(frame), type(frame))
