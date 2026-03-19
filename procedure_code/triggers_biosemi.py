from typing import List


class TriggerTypes:
    """
    Base class for trigger types. Inherit from this to define your experiment triggers.
    Example:
        class MyTriggers(TriggerTypes):
            TRIAL_START = "trial_start"
            STIMULUS = "stimulus"
            RESPONSE = "response"
    """

    @classmethod
    def vals(cls) -> List[str]:
        return [value for name, value in vars(cls).items() if name.isupper()]