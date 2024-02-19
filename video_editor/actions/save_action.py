from pathlib import Path

from moviepy.video.io.VideoFileClip import VideoFileClip

from video_editor.actions.action import Action


class SaveAction(Action):
    def __init__(self, **action_data):
        super().__init__(**action_data)

        self._output_directory: str = ""

    def handle(self, video_file_clip: VideoFileClip) -> VideoFileClip:
        super().handle(video_file_clip)

        edited_file_path = Path(
            self._clip_data.directory, self._output_directory, self._clip_data.filename
        )
        edited_file_path.parent.mkdir(exist_ok=True)

        # TODO: extend this info with clip info, add support for more formats
        video_file_clip.write_videofile(
            str(edited_file_path),
            codec="libx264",
            verbose=False,
            logger=None,
        )

        return video_file_clip
