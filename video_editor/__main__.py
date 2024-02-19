import json
import os
from pathlib import Path

from progress.bar import IncrementalBar

from video_editor.actions import create_actions_from_settings
from video_editor.actions.clip_data import ClipData
from video_editor.actions.factories.default_action_factory import DefaultActionFactory
from video_editor.console import move_cursor_down, move_cursor_up

ACTIONS_FILENAME = "actions.json"

VIDEOS_PATH = Path("videos")
VIDEOS_PATH.mkdir(exist_ok=True)


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
                clip_data = ClipData(dirpath, filename)

                move_cursor_down()
                with IncrementalBar(
                    "Handling actions", max=len(actions)
                ) as actions_bar:
                    clip = None
                    for action in actions:
                        action.set_clip_data(clip_data)
                        clip = action.handle(clip)

                        if action.should_break():
                            break

                        actions_bar.next()

                move_cursor_up(2)

                bar.next()


if __name__ == "__main__":
    main()
