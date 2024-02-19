import json
import os
from pathlib import Path

from moviepy.video.io.VideoFileClip import VideoFileClip
from progress.bar import IncrementalBar

from video_editor.actions import create_actions_from_settings
from video_editor.actions.factories.default_action_factory import DefaultActionFactory

ACTIONS_FILENAME = "actions.json"

VIDEOS_PATH = Path("videos")
VIDEOS_PATH.mkdir(exist_ok=True)

EDITED_VIDEOS_DIRECTORY_NAME = "edited"


def main():
    for dirpath, dirnames, filenames in os.walk(VIDEOS_PATH):
        actions_file_path = Path(dirpath, ACTIONS_FILENAME)
        if not actions_file_path.exists():
            continue

        with open(actions_file_path) as actions_file:
            action_settings = json.load(actions_file)

        action_factory = DefaultActionFactory()

        actions = create_actions_from_settings(action_factory, action_settings)

        with IncrementalBar(
            f"Editing videos in {dirpath!r}", max=len(filenames)
        ) as bar:
            for filename in filenames:
                with IncrementalBar(
                    "Handling actions", max=len(actions)
                ) as actions_bar:
                    video_file_path = Path(dirpath, filename)

                    # TODO: check is video (of format?) action
                    if video_file_path == actions_file_path:
                        continue

                    # TODO: open action
                    clip = VideoFileClip(str(video_file_path))

                    for action in actions:
                        clip = action.handle(clip)
                        actions_bar.next()

                    # TODO: save action
                    edited_file_path = Path(
                        dirpath, EDITED_VIDEOS_DIRECTORY_NAME, filename
                    )
                    edited_file_path.parent.mkdir(exist_ok=True)

                    clip.write_videofile(
                        str(edited_file_path),
                        verbose=False,
                        logger=None,
                        codec="libx264",
                    )

                bar.next()


if __name__ == "__main__":
    main()
