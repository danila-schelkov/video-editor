from moviepy.video.io.VideoFileClip import VideoFileClip

from video_editor.actions.action import Action


class OpenAction(Action):
    def __init__(self, **action_data):
        super().__init__(**action_data)

    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        super().handle(video_file_clip)

        return VideoFileClip(str(self._clip_data.filepath))
