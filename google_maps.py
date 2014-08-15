import urllib


class GoogleMaps(object):
    def __init__(self):
        super(GoogleMaps, self).__init__()

    def get_query_params(self):
        return urllib.urlencode(
            {
                'center': 'Detroit,MI',
                'zoom': 14,
                'size': '400x400'
            }
        )