from video_editor.actions.cut_action import CutAction
from video_editor.actions.factories.action_factory import ActionFactory


class DefaultActionFactory(ActionFactory):
    def _register_actions(self):
        self._register_action("cut", CutAction)
