import os
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from challenges.models import Challenge


def run():
    print('yey')
    for challenge in Challenge.objects.filter(apply_until_date=date.today() + relativedelta(days=5)):
        print('AWESOME')
        for applicant in challenge.applicants.all():
            print(applicant.email)
            send_mail(
                'Subject here',
                'Applications are closing',
                'george.s.koureas@gmail.com',
                [applicant.email],
                fail_silently=False,
                )