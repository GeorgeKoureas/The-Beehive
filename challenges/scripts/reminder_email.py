import os
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from challenges.models import Challenge
from users.models import Notifications


def run():
    for challenge in Challenge.objects.filter(apply_until_date=date.today() + relativedelta(days=5)):
        for applicant in challenge.applicants.all():
            notification = Notifications.objects.create(recipient=applicant, message=f'Applications for "{challenge.name}" close in 5 days!')
            notification.save()
            send_mail(
                'Applications are closing',
                'You are 5 days away from the 2nd phase of a challenge! Make sure you visit our site for updates!',
                'george.s.koureas@gmail.com',
                [applicant.email],
                fail_silently=False,
                )
    
    for challenge in Challenge.objects.filter(due_date=date.today() + relativedelta(days=5)):
        for applicant in challenge.applicants.all():
            notification = Notifications.objects.create(recipient=applicant, message=f'"{challenge.name}" is due in 5 days! Make sure to submit your final solution')
            notification.save()
            send_mail(
                'A challenge is wrapping up',
                'You are 5 days away from the end of a challenge! Make sure you co-operate with your team and submit your final solution!',
                'george.s.koureas@gmail.com',
                [applicant.email],
                fail_silently=False,
                )
