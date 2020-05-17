"""
    User object
"""
from dataclasses import dataclass, field
from typing import List, Optional

from .base import BaseModel
from .geo import Location
from .entities import Entities


@dataclass
class Derived(BaseModel):
    """
    A class representing User extend deride objects
    """
    locations: Optional[List[Location]] = field(default=None)


@dataclass
class User(BaseModel):
    """
    A class representing the user object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
    """
    id: int = field(repr=False)
    id_str: str
    name: str
    screen_name: str
    protected: bool = field(repr=False, compare=False)
    verified: bool = field(repr=False, compare=False)
    followers_count: int = field(repr=False, compare=False)
    friends_count: int = field(repr=False, compare=False)
    listed_count: int = field(repr=False, compare=False)
    favourites_count: int = field(repr=False, compare=False)
    statuses_count: int = field(repr=False, compare=False)
    created_at: str = field(repr=False, compare=False)
    profile_banner_url: Optional[str] = field(repr=False, compare=False)
    profile_image_url_https: Optional[str] = field(repr=False, compare=False)
    default_profile: bool = field(repr=False, compare=False)
    default_profile_image: bool = field(repr=False, compare=False)
    location: Optional[str] = field(default=None, repr=False, compare=False)
    derived: Optional[Derived] = field(default=None, repr=False, compare=False)
    url: Optional[str] = field(default=None, repr=False, compare=False)
    description: Optional[str] = field(default=None, repr=False, compare=False)
    withheld_in_countries: Optional[List[str]] = field(default=None, repr=False, compare=False)
    withheld_scope: Optional[str] = field(default=None, repr=False, compare=False)
    entities: Optional[Entities] = field(default=None, repr=False, compare=False)
