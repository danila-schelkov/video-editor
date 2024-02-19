from video_editor.actions.check_extension_action import CheckExtensionAction
from video_editor.actions.cut_action import CutAction
from video_editor.actions.factories.action_factory import ActionFactory
from video_editor.actions.open_action import OpenAction
from video_editor.actions.save_action import SaveAction


class DefaultActionFactory(ActionFactory):
    def _register_actions(self):
        self._register_action("check_extension", CheckExtensionAction)
        self._register_action("open", OpenAction)
        self._register_action("save", SaveAction)
        self._register_action("cut", CutAction)
