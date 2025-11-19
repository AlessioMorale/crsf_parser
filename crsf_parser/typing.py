from re import Pattern
from io import BytesIO
from enum import IntEnum
from construct import Construct
from construct.lib.containers import Container
from typing import (
    Callable,
    Union,
    List,
    Tuple,
    Literal,
    Optional,
    Self,
    Any
)


class ContainerType(Construct, Container):
    _io: BytesIO
    _search: Callable[[Pattern, bool], List[Any]]
    parse: Callable[[bytes], Self]


class CrsfHeaderType(ContainerType):
    sync_byte: Literal[b"\xc8"]
    frame_length: int
    data_offset: int
    type: int
    destination_address: Optional[int]
    origin_address: Optional[int]


class PayloadHeartbeatType(ContainerType):
    origin_device_address: int


class PayloadBatterySensorType(ContainerType):
    voltage: int
    current: int
    capacity: int
    remaining: int


class TxPower(IntEnum):
    TX_POWER_0_MW = 0
    TX_POWER_10_MW = 1
    TX_POWER_25_MW = 2
    TX_POWER_100_MW = 3
    TX_POWER_500_MW = 4
    TX_POWER_1000_MW = 5
    TX_POWER_2000_MW = 6


class DiversityAntenna(IntEnum):
    ANTENNA_1 = 0
    ANTENNA_2 = 1


class RfMode(IntEnum):
    RF_4_FPS = 0
    RF_50_FPS = 1
    RF_150_FPS = 2


class PayloadLinkStatisticsType(ContainerType):
    uplink_rssi_ant_1: int
    uplink_rssi_ant_2: int
    uplink_link_quality: int
    uplink_snr: int
    diversity_active_antenna: DiversityAntenna
    rf_mode: RfMode
    uplink_tx_power: TxPower
    downlink_rssi: int
    downlink_link_quality: int
    downlink_snr: int


class PayloadRcChannelsPackedType(ContainerType):
    channels: Tuple[int, ...]


class CrsfFrameType(ContainerType):
    header: CrsfHeaderType
    payload: Union[
        PayloadHeartbeatType,
        PayloadBatterySensorType,
        PayloadLinkStatisticsType,
        PayloadRcChannelsPackedType,
        List[int]
    ]
    crc_offset: int
    CRC: int