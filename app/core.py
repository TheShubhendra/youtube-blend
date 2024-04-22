import json

import aiohttp


class YouTubeChannel:
    def __init__(self, channel_id, title):
        self.channel_id = channel_id
        self.title = title

    def __hash__(self):
        return hash(self.channel_id)

    def __eq__(self, other):
        return self.channel_id == other.channel_id

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"YoutubeChannel({self.channel_id}, {self.title})"

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, YouTubeChannel):
            return data
        if isinstance(data, str):
            return cls.from_dict(json.loads(data))
        if isinstance(data, dict) and "snippet" in data:
            return cls(
                data["snippet"]["resourceId"]["channelId"], data["snippet"]["title"]
            )
        if isinstance(data, dict) and "items" in data:
            return set([cls.from_dict(i) for i in data["items"]])
        raise ValueError(f"Invalid data type: {type(data)}")


async def get_channels(api_key: str) -> set[YouTubeChannel]:
    """Get all channels that the user is subscribed to."""
    url = "https://content-youtube.googleapis.com/youtube/v3/subscriptions"
    params = {
        "part": "snippet",
        "mine": True,
        "key": api_key,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            data = await response.json()
            return YouTubeChannel.from_dict(data)


def get_similarity_score(a: set[YouTubeChannel], b: set[YouTubeChannel]) -> float:
    """Calculate the similarity score between two sets of YouTube channels."""
    return len(a.intersection(b)) / len(a.union(b))
