from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.views import View


class RobotsView(View):
    http_method_names = ['get']
    lines = [
        "User-Agent: *",
        "Allow: /",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Disallow: /__api__/",
        "Disallow: /admin/",
    ]   
    lines_together = "\n".join(lines)

    def get_lines(self):
        return self.lines_together

    def get(self, request, *args, **kwargs):
        current_site = Site.objects.get_current()
        scheme = request.scheme
        return HttpResponse(self.get_lines(), content_type="text/plain")