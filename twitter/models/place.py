from dataclasses import dataclass, field
from typing import Optional, List, Dict

from .base import BaseModel


@dataclass
class Coordinates(BaseModel):
    """
    A class representing coordinates object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#coordinates
    """
    coordinates: List[float] = field(repr=False)
    type: str


@dataclass
class BoundingBox(BaseModel):
    """
    A class representing bounding box object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#obj-boundingbox
    """
    coordinates: List[List[List[float]]] = field(repr=False)
    type: str


@dataclass
class Place(BaseModel):
    """
    A class representing place object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#place
    """
    id: str
    url: str = field(repr=False)
    place_type: str
    name: str = field(repr=False)
    full_name: str = field(repr=False)
    country_code: str = field(repr=False)
    country: str = field(repr=False)
    bounding_box: Optional[BoundingBox] = field(repr=False)
    attributes: Optional[Dict] = field(default=None, repr=False)
