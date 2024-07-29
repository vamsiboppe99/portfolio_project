from django.core.management.base import BaseCommand
import csv
from resume.models import ContactSubmission

class Command(BaseCommand):
    help = 'Export contact submissions to CSV'

    def handle(self, *args, **options):
        with open('submissions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Message', 'Created At'])
            
            for submission in ContactSubmission.objects.all():
                writer.writerow([submission.name, submission.email, submission.message, submission.created_at])
        
        self.stdout.write(self.style.SUCCESS('Successfully exported submissions'))