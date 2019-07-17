import orjson
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class ORJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return bytes()
        return orjson.dumps(data, default=serialize_arbitrary_type)


def serialize_arbitrary_type(data):
    if isinstance(data, ReturnDict):
        return dict(data)

    if isinstance(data, ReturnList):
        items = []
        for item in data:
            items.append(dict(item))
        return list(items)
