from construct import Byte, If, Struct, Const, Int8ub, Switch, Tell, this, Array
from .payloads import (
    PacketsTypes,
    payload_battery_sensor,
    payload_heartbeat,
    payload_link_statistics,
    payload_rc_channels_packed,
)

SYNC_BYTE_BIN_STRING = b"\xc8"
SYNC_BYTE = int.from_bytes(SYNC_BYTE_BIN_STRING, byteorder="big")

crsf_header = Struct(
    "sync_byte" / Const(SYNC_BYTE_BIN_STRING),
    "frame_length" / Int8ub,
    "data_offset" / Tell,
    "type" / Int8ub,
    "destination_address" / If(this.type > 0x27, Int8ub),
    "origin_address" / If(this.type > 0x27, Int8ub),
)

crsf_frame = Struct(
    "header" / crsf_header,
    "payload"
    / Switch(
        this.header.type,
        {
            PacketsTypes.HEARTBEAT: payload_heartbeat,
            PacketsTypes.BATTERY_SENSOR: payload_battery_sensor,
            PacketsTypes.LINK_STATISTICS: payload_link_statistics,
            PacketsTypes.RC_CHANNELS_PACKED: payload_rc_channels_packed,
        },
        default=Array(this.frame_length - 2, Byte),
    ),
    "crc_offset" / Tell,
    "CRC" / Int8ub,
)
