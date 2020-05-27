import os
from datetime import date
from datutil.relativedelta import relativedelta
from django.mail import send_mail
from .models import Challenge


def run():
    for challenge in Challenge.objects.filter(apply_until_date=date.today() + relativedelta(days=5)):
        for applicant in challenge.applicants.all():
            print(applicant.email)
            send_mail(
                'Subject here',
                'Applications are closing',
                'george.s.koureas@gmail.com',
                [applicant.email],
                fail_silently=False,
                )
            os.sytem("pause")