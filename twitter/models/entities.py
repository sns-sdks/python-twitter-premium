from dataclasses import dataclass, field

from typing import Optional, List

from .base import BaseModel


@dataclass
class Hashtag(BaseModel):
    """
    A class representing hashtag object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#hashtags
    """

    text: Optional[str] = field(default=None)
    indices: Optional[List[int]] = field(default=None, repr=False)


@dataclass
class Size(BaseModel):
    """
    A class representing size object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#size
    """

    w: Optional[int] = field(default=None)
    h: Optional[int] = field(default=None)
    resize: Optional[str] = field(default=None)


@dataclass
class Sizes(BaseModel):
    """
    A class representing sizes object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media-size
    """

    thumb: Optional[Size] = field(default=None)
    small: Optional[Size] = field(default=None, repr=False)
    medium: Optional[Size] = field(default=None, repr=False)
    large: Optional[Size] = field(default=None, repr=False)


@dataclass
class Variant(BaseModel):
    bitrate: Optional[int] = field(default=None, repr=False)
    content_type: Optional[str] = field(default=None, repr=False)
    url: Optional[str] = field(default=None, repr=False)


@dataclass
class VideoInfo(BaseModel):
    """
    A class representing video object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object
    """

    aspect_ratio: Optional[List[int]] = field(default=None, repr=False)
    duration_millis: Optional[int] = field(default=None, repr=False)
    variants: Optional[List[Variant]] = field(default=None, repr=False)


@dataclass
class AdditionalMediaInfo(BaseModel):
    """
    A class representing additional media object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object
    """

    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    embeddable: Optional[bool] = field(default=None, repr=False)
    monetizable: Optional[bool] = field(default=None, repr=False)


@dataclass
class Media(BaseModel):
    """
    A class representing media object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media
    """

    display_url: Optional[str] = field(default=None, repr=False)
    expanded_url: Optional[str] = field(default=None, repr=False)
    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None)
    indices: Optional[List[int]] = field(default=None, repr=False)
    media_url: Optional[str] = field(default=None, repr=False)
    media_url_https: Optional[str] = field(default=None, repr=False)
    type: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None, repr=False)
    sizes: Optional[Sizes] = field(default=None, repr=False)
    source_status_id: Optional[int] = field(default=None, repr=False)
    source_status_id_str: Optional[str] = field(default=None, repr=False)
    video_info: Optional[VideoInfo] = field(default=None, repr=False)
    additional_media_info: Optional[AdditionalMediaInfo] = field(default=None, repr=False)


@dataclass
class Url(BaseModel):
    """
    A class representing media object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#urls
    """

    display_url: Optional[str] = field(default=None, repr=False)
    expanded_url: Optional[str] = field(default=None, repr=False)
    url: Optional[str] = field(default=None)
    indices: Optional[List[int]] = field(default=None, repr=False)
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

    id: Optional[int] = field(default=None, repr=False)
    id_str: Optional[str] = field(default=None)
    indices: Optional[List[int]] = field(default=None, repr=False)
    name: Optional[str] = field(default=None)
    screen_name: Optional[str] = field(default=None)


@dataclass
class Symbol(BaseModel):
    """
    A class representing symbol object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#symbols
    """

    indices: Optional[List[int]] = field(default=None, repr=False)
    text: Optional[str] = field(default=None)


@dataclass
class PollOption(BaseModel):
    position: Optional[int] = field(default=None)
    text: Optional[str] = field(default=None)


@dataclass
class Poll(BaseModel):
    """
    A class representing poll object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#polls
    """

    options: Optional[List[PollOption]] = field(default=None, repr=False)
    end_datetime: Optional[str] = field(default=None)
    duration_minutes: Optional[int] = field(default=None)


@dataclass
class Entities(BaseModel):
    """
    A class representing entities object.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object
    """

    hashtags: Optional[List[Hashtag]] = field(default=None, repr=False)
    media: Optional[List[Media]] = field(default=None, repr=False)
    urls: Optional[List[Url]] = field(default=None, repr=False)
    user_mentions: Optional[List[UserMention]] = field(default=None, repr=False)
    symbols: Optional[List[Symbol]] = field(default=None, repr=False)
    polls: Optional[List[Poll]] = field(default=None, repr=False)


@dataclass
class ExtendedEntities(Entities):
    """
    extended entities has same struct as entities.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object
    """

    ...


@dataclass
class UserEntitiesUrl(BaseModel):
    urls: Optional[List[Url]] = field(default=None, repr=False)


@dataclass
class UserEntitiesDescription(BaseModel):
    description: Optional[List[Url]] = field(default=None, repr=False)


@dataclass
class UserEntities(BaseModel):
    """
    A class representing user entities object. It has a bit different for tweet entities.

    Refer: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#entities-user
    """

    url: Optional[UserEntitiesUrl] = field(default=None, repr=False)
    description: Optional[UserEntitiesDescription] = field(default=None, repr=False)
