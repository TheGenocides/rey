from typing import List, Dict, Union, Self

class QuickReply:
    def __init__(self, **kwargs):
        self.__options = kwargs.get("options", [])

    @classmethod
    def from_dict(cls, options: List[Dict[str, Union[str, dict]]]):
        return cls(options=options)
    
    def add_option(self, label: str, *, type: str, **fields) -> Self:
        self.__options.append(
            {
                "type": "action",
                "action": {
                    "type": type,
                    "label": label,
                    **fields
                }
            }
        )

        return self