import codecs

import orjson
from django.conf import settings
from rest_framework_orjson.renderers import ORJSONRenderer
from rest_framework.parsers import BaseParser


class ORJSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """
    media_type = 'application/json'
    renderer_class = ORJSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        decoded_stream = codecs.getreader(encoding)(stream)
        return orjson.loads(decoded_stream.read())
