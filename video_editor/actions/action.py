from abc import ABC, abstractmethod
from typing import ClassVar

from moviepy.video.io.VideoFileClip import VideoFileClip

from video_editor.actions.clip_data import ClipData


class Action(ABC):
    fields_to_save: ClassVar[list[str]] = ["_clip_data", "_is_action_data_set", "_should_break"]

    def __init__(self, **action_data):
        self._action_data = action_data

        self._is_action_data_set: bool = False
        self._should_break: bool = False
        self._clip_data: ClipData | None = None

    def set_clip_data(self, clip_data: ClipData):
        self._clip_data = clip_data

    @abstractmethod
    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        self._load_action_data()
        return video_file_clip

    def _load_action_data(self):
        if self._is_action_data_set:
            return

        data_to_save = {
            key: value for key, value in self.__dict__.items()
            if key in self.fields_to_save
        }
        self.__dict__ = {f"_{key}": value for key, value in self._action_data.items()}
        self.__dict__.update(data_to_save)
        self._is_action_data_set = True

    def should_break(self) -> bool:
        return self._should_break
