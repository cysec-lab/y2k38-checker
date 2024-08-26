#[derive(Debug, PartialEq)]
pub enum Y2k38Category {
    ReadFsTimestamp,
    WriteFsTimestamp,
    TimetToIntDowncast,
    TimetToLongDowncast,
}
