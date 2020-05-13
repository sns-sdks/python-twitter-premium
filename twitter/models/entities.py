from dataclasses import dataclass, field

from typing import Optional, List

from .base import BaseModel


@dataclass
class Hashtag(BaseModel):
    """
    A class representing hashtag object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#hashtags
    """
    text: str
    indices: List[int] = field(repr=False)


@dataclass
class Size(BaseModel):
    """
    A class representing size object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#size
    """
    w: int
    h: int
    resize: str


@dataclass
class Sizes(BaseModel):
    """
    A class representing sizes object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media-size
    """

    thumb: Size
    small: Size = field(repr=False)
    medium: Size = field(repr=False)
    large: Size = field(repr=False)


@dataclass
class Media(BaseModel):
    """
    A class representing media object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media
    """
    display_url: str = field(repr=False)
    expanded_url: str = field(repr=False)
    id: int = field(repr=False)
    id_str: str
    indices: List[int] = field(repr=False)
    media_url: str = field(repr=False)
    media_url_https: str = field(repr=False)
    type: str
    url: str = field(repr=False)
    sizes: Sizes = field(repr=False)
    source_status_id: Optional[int] = field(default=None, repr=False)
    source_status_id_str: Optional[str] = field(default=None, repr=False)


@dataclass
class Url(BaseModel):
    """
    A class representing media object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#urls
    """
    display_url: str = field(repr=False)
    expanded_url: str = field(repr=False)
    url: str
    indices: List[int] = field(repr=False)
    # Extends fields
    status: Optional[int] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)


@dataclass
class UserMention(BaseModel):
    """
    A class representing user mention object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#mentions
    """
    id: int = field(repr=False)
    id_str: str
    indices: List[int] = field(repr=False)
    name: str
    screen_name: str


@dataclass
class Symbol(BaseModel):
    """
    A class representing symbol object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#symbols
    """
    indices: List[int] = field(repr=False)
    text: str


@dataclass
class PollOption(BaseModel):
    position: int
    text: str


@dataclass
class Poll(BaseModel):
    """
    A class representing poll object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#polls
    """

    options: List[PollOption] = field(repr=False)
    end_datetime: str
    duration_minutes: int


@dataclass
class Entities(BaseModel):
    """
    A class representing entities object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object
    """
    hashtags: List[Hashtag]
    media: List[Media] = field(repr=False)
    urls: List[Url] = field(repr=False)
    user_mentions: List[UserMention] = field(repr=False)
    symbols: List[Symbol] = field(repr=False)
    polls: List[Poll] = field(repr=False)


@dataclass
class ExtendedEntities(Entities):
    """

    extended entities has same struct as entities.
    """
    ...
