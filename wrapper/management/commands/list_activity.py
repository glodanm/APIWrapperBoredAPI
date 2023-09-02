from django.core.management.base import BaseCommand
from ...models import Activity


class Command(BaseCommand):
    help = 'List the last 5 activities saved in the database'

    def handle(self, *args, **kwargs):
        activities = Activity.objects.order_by('-id')[:5]

        if not activities:
            self.stdout.write(self.style.WARNING('No activities found in the database.'))
            return

        self.stdout.write(self.style.SUCCESS('Last 5 activities saved in the database:'))
        for index, activity in enumerate(activities, start=1):
            self.stdout.write(f"{index}. {activity.activity} (Type: {activity.type})")
