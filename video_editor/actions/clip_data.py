import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClipData:
    directory: os.PathLike | str
    filename: os.PathLike | str

    @property
    def filepath(self) -> str:
        return Path(self.directory, self.filename)
