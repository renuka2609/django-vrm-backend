from rest_framework.exceptions import PermissionDenied

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.role != 'VENDOR' and not request.user.org:
                raise PermissionDenied("Organization missing")

            request.org = request.user.org
            request.vendor = request.user.vendor

        return self.get_response(request)
