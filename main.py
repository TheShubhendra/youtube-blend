import json


class YoutubeChannel:
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

    @staticmethod
    def from_dict(data):
        if isinstance(data, YoutubeChannel):
            return data
        if isinstance(data, str):
            return YoutubeChannel.from_dict(json.loads(data))
        if isinstance(data, dict) and "snippet" in data:
            return YoutubeChannel(
                data["snippet"]["resourceId"]["channelId"], data["snippet"]["title"]
            )
        if isinstance(data, dict) and "items" in data:
            return set([YoutubeChannel.from_dict(i) for i in data["items"]])
        raise ValueError(f"Invalid data type: {type(data)}")


with open("a.json") as f:
    a = YoutubeChannel.from_dict(json.load(f))
with open("b.json") as f:
    b = YoutubeChannel.from_dict(json.load(f))

print(f"Channels in A: {a}")
print(f"Channels in B: {b}")
print(f"Same channels: {a.intersection(b)}")
print(f"Similarity score: {len(a.intersection(b)) / len(a.union(b))}")
