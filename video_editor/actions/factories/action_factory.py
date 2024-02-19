from abc import abstractmethod, ABC

from video_editor.actions.action import Action
from video_editor.exceptions import ActionAlreadyBound, ActionNotFound


class ActionFactory(ABC):
    def __init__(self):
        self._actions: dict[str, type[Action]] = {}
        self._register_actions()

    @abstractmethod
    def _register_actions(self):
        ...

    def _register_action(self, action_type: str, action_class: type[Action]):
        if action_type in self._actions:
            raise ActionAlreadyBound(f"Action {action_type} already bound")
        self._actions[action_type] = action_class

    def create_action_by_type(self, action_type: str, action_data: dict) -> Action:
        if action_type in self._actions:
            return self._actions[action_type](**action_data)

        raise ActionNotFound(f"Action {action_type!r} not found.")
