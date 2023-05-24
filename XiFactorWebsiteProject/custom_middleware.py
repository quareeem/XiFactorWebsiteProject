from django.conf import settings
from django.utils.module_loading import import_string
from django_ratelimit.exceptions import Ratelimited
from django_ratelimit.decorators import ratelimit


class RatelimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        @ratelimit(key='user_or_ip', rate='40/m')
        def rate_limited_view(request):
            return self.get_response(request)
        return rate_limited_view(request)

    def process_exception(self, request, exception):
        if not isinstance(exception, Ratelimited):
            return None
        view = import_string(settings.RATELIMIT_VIEW)
        return view(request, exception)