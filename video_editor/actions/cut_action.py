from moviepy.video.io.VideoFileClip import VideoFileClip

from video_editor.actions.action import Action


class CutAction(Action):
    def __init__(self, **action_data):
        super().__init__(**action_data)

        self._start: int = 0
        self._end: int | None = None

    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        video_file_clip = super().handle(video_file_clip)

        return video_file_clip.subclip(self._start, self._end)
