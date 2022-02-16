import json
import json
from rest_framework import renderers


class UserRenderer(renderers.JSONOpenAPIRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        response = ''

        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})

        return response
