from video_editor.actions.action import Action
from video_editor.actions.factories import ActionFactory


def create_actions_from_settings(
    action_factory: ActionFactory, action_settings
) -> list[Action]:
    actions: list[Action] = []
    for action_setting in action_settings:
        action_type = action_setting["action"]

        action_instance = action_factory.create_action_by_type(
            action_type, action_setting
        )
        actions.append(action_instance)

    return actions
