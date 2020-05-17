from dataclasses import dataclass, field
from typing import Optional, List, Dict

from .base import BaseModel


@dataclass
class Coordinates(BaseModel):
    """
    A class representing coordinates object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#coordinates
    """

    coordinates: Optional[List[float]] = field(default=None, repr=False)
    type: Optional[str] = field(default=None)


@dataclass
class BoundingBox(BaseModel):
    """
    A class representing bounding box object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#obj-boundingbox
    """

    coordinates: Optional[List[List[List[float]]]] = field(default=None, repr=False)
    type: Optional[str] = field(default=None)


@dataclass
class Place(BaseModel):
    """
    A class representing place object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/geo-objects#place
    """

    id: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None, repr=False)
    place_type: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None, repr=False)
    full_name: Optional[str] = field(default=None, repr=False)
    country_code: Optional[str] = field(default=None, repr=False)
    country: Optional[str] = field(default=None, repr=False)
    bounding_box: Optional[BoundingBox] = field(default=None, repr=False)
    attributes: Optional[Dict] = field(default=None, repr=False)
