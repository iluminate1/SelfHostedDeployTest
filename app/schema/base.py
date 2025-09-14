import msgspec


class BaseStruct(msgspec.Struct):
    def as_dict(self):
        return msgspec.structs.asdict(self)

    def to_builtins(self):
        return msgspec.to_builtins(self)
