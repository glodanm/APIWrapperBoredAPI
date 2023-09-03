from django.core.management.base import BaseCommand
from wrapper.wrapper import Wrapper
from wrapper.models import Activity


class Command(BaseCommand):

    help = 'Get and save a new random activity based on specified options'

    def add_arguments(self, parser):
        parser.add_argument('--type', help='Filter by activity type')
        parser.add_argument('--participants', type=int, help='Filter by number of participants')
        parser.add_argument('--price_min', type=float, help='Minimum price')
        parser.add_argument('--price_max', type=float, help='Maximum price')
        parser.add_argument('--accessibility_min', type=float, help='Minimum accessibility')
        parser.add_argument('--accessibility_max', type=float, help='Maximum accessibility')
    
    def handle(self, *args, **options):
        activity_type=options['type']
        participants=options['participants']
        minprice=options['price_min']
        maxprice=options['price_max']
        minaccessibility=options['accessibility_min']
        maxaccessibility=options['accessibility_max']

        wrapper = Wrapper()

        activity_data = wrapper.get_activity(
            activity_type=activity_type,
            participants=participants,
            minprice=minprice,
            maxprice=maxprice,
            minaccessibility=minaccessibility,
            maxaccessibility=maxaccessibility,
        )

        if activity_data:
            activity = Activity.objects.create(
                activity=activity_data['activity'],
                type=activity_data['type'],
                participants=activity_data['participants'],
                price=activity_data['price'],
                accessibility=activity_data['accessibility'],
                link=activity_data['link'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully saved activity: {activity.activity}'))
        else:
            self.stderr.write(self.style.ERROR('Failed to fetch activity data from the API.'))
