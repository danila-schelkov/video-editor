import os.path

from moviepy.video.io.VideoFileClip import VideoFileClip

from video_editor.actions.action import Action


# Or check format?
class CheckExtensionAction(Action):
    def __init__(self, **action_data):
        super().__init__(**action_data)

        self._allowed_extensions: list[str] = []
        self._output_directory: str = ""

    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        super().handle(video_file_clip)

        path_splitext = os.path.splitext(self._clip_data.filename)
        extension = path_splitext[1][1:]
        self._should_break = extension not in self._allowed_extensions

        return video_file_clip
