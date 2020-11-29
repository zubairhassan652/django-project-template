from django.template.loader import get_template
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def send_email(to, subject, msg, from_email=settings.DEFAULT_FROM_EMAIL):
    to = to if type(to) == list else [to]
    return send_mail(subject, msg, from_email, to)


def send_html_email(to, subject, ctx, template, from_email=settings.DEFAULT_FROM_EMAIL, attachments=None):
    to = to if type(to) == list else [to]
    ctx['site_url'] = settings.SITE_URL
    ctx['year'] = timezone.now().year
    message = get_template(template).render(ctx)
    email = EmailMessage(subject, message, to=to, from_email=from_email)
    email.content_subtype = 'html'
    if attachments:
        for file in attachments:
            email.attach_file(file)
    return email.send()