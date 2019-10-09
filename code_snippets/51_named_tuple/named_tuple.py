from typing import *

class Blob(NamedTuple):
    x: Optional[float]
    numbers: List[int]
    object: Dict[str, int]

    @classmethod
    def from_json(cls, blob: Dict[str, Any]) -> "Blob":
        return cls(blob["x"], blob["numbers"], blob["object"])
