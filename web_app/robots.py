from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.views import View

ALLOWABLES = [
    "/"
]

DISALLOWABLES = [
    "/private/",
    "/junk/",
    "/__api__/",
    "/admin/",
]
    
class RobotsView(View):
    http_method_names = ['get']
    lines = [
        "User-Agent: *"
    ]   

    for item in ALLOWABLES:
        lines.append(f'Allow: {item}')

    for item in DISALLOWABLES:
        lines.append(f'Disallow: {item}')

    lines_together = "\n".join(lines)

    def get_lines(self):
        return self.lines_together

    def get(self, request, *args, **kwargs):
        current_site = Site.objects.get_current()
        scheme = request.scheme
        return HttpResponse(self.get_lines(), content_type="text/plain")