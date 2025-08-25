from typing import Any
from gradio import EventData
from gradio.blocks import Block

class LikeData(EventData):
    def __init__(self, target: Block | None, data: Any):
        super().__init__(target, data)
        self.index: int | tuple[int, int] = data["index"]
        """The index of the liked/disliked item.
        Is a tuple if the component is two dimensional.
        """
        self.value: Any = data["value"]
        """The value of the liked/disliked item."""
        self.liked: bool = data.get("liked", True)
        """True if the item was liked, False if disliked."""


class KeyUpData(EventData):
    def __init__(self, target: Block | None, data: Any):
        super().__init__(target, data)
        self.key: str = data["key"]
        """
        The key that was pressed.
        """
        self.input_value: str = data["input_value"]
        """ The displayed value in the input textbox after the key was pressed.
        This may be different than the `value` attribute of the component
        itself, as the `value` attribute of some components (e.g. Dropdown)
        are not updated until the user presses Enter.
        """


class SelectData(EventData):
    def __init__(self, target: Block | None, data: Any):
        super().__init__(target, data)
        self.index: Any = data["index"]
        """
        The index of the selected item. Is a tuple if the component is two dimensional or selection is a range.
        """
        self.value: Any = data["value"]
        """
        The value of the selected item.
        """
        self.row_value: Any = data.get("row_value")
        """
        The value of the entire row that the selected item belongs to, as a 1-D list. Only implemented for the `Dataframe` component, returns None for other components.
        """
        self.col_value: Any = data.get("col_value")
        """
        The value of the entire row that the selected item belongs to, as a 1-D list. Only implemented for the `Dataframe` component, returns None for other components.
        """
        self.selected: bool = data.get("selected", True)
        """
        True if the item was selected, False if deselected.
        """