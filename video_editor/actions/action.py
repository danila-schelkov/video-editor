from abc import ABC, abstractmethod

from moviepy.video.io.VideoFileClip import VideoFileClip


class Action(ABC):
    def __init__(self, **action_data):
        self._action_data = action_data
        self._is_action_data_set: bool = False

    @abstractmethod
    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        self._load_action_data()
        return video_file_clip

    def _load_action_data(self):
        if self._is_action_data_set:
            return

        self.__dict__ = {f"_{key}": value for key, value in self._action_data.items()}
        self._is_action_data_set = True
