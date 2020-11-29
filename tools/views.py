import logging

from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from .utils.email_utils import send_html_email


LOGGER = logging.getLogger(__name__)


def hello_view(request):
    LOGGER.info('Landing in hello view')
    return render(request, 'tools/hello.html')


class TestEmailView(View):

    def get(self, request, email_id):
        result = send_html_email(
            to=email_id,
            subject="Testing the html email integration",
            ctx={'name': 'Denise W. Medrano'},
            template='tools/test_html_email.html'
        )
        return JsonResponse({"result": result})
