from dataclasses import dataclass
from typing import (
    Dict,
    Type,
    TypeVar,
)

from dataclasses_json import (
    dataclass_json,
    DataClassJsonMixin,
)

A = TypeVar("A", bound=DataClassJsonMixin)


@dataclass_json
@dataclass
class BaseModel:
    @classmethod
    def new_from_json_dict(cls: Type[A], data: Dict, *, infer_missing=False) -> A:
        """
        Convert json dict to data class
        :param data: A json dict which will convert model class.
        :param infer_missing: if set True, will let missing field (not have default vale) to None
        :return: The data class
        """
        c = cls.from_dict(data, infer_missing=infer_missing)
        # save origin data
        cls._json = data
        return c
