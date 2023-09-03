from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .wrapper import Wrapper
from .models import Activity
from .serializers import ActivitySerializer


class GetActivityAPI(APIView):

    def get(self, request):
        data = request.data
        type = request.GET.get('type')
        participants = request.GET.get('participants')
        minprice = request.GET.get('minprice')
        maxprice = request.GET.get('maxprice')
        minaccessibility = request.GET.get('minaccessibility')
        maxaccessibility = request.GET.get('maxaccessibility')

        wrapper = Wrapper()

        activity_data = wrapper.get_activity(
            activity_type=type,
            participants=participants,
            minprice=minprice,
            maxprice=maxprice,
            minaccessibility=minaccessibility,
            maxaccessibility=maxaccessibility,
        )

        activity = Activity(
            activity=activity_data['activity'],
            type=activity_data['type'],
            participants=activity_data['participants'],
            price=activity_data['price'],
            accessibility=activity_data['accessibility'],
            link=activity_data.get('link', 'No URL'),
        )
        activity.save()
        serializer = ActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class ActivityList(APIView):

    def get(self, request):
        activity = Activity.objects.all()
        
        activity_type = self.request.query_params.get('type', None)
        participants = self.request.query_params.get('participants', None)
        minprice = self.request.query_params.get('minprice', None)
        maxprice = self.request.query_params.get('maxprice', None)
        minaccessibility = self.request.query_params.get('minaccessibility', None)
        maxaccessibility = self.request.query_params.get('maxaccessibility', None)

        if activity_type:
            activity = activity.filter(type__iexact=activity_type)

        if participants is not None:
            activity = activity.filter(participants__iexact=participants)

        if minprice is not None:
            activity = activity.filter(price__gte=minprice)

        if maxprice is not None:
            activity = activity.filter(price__lte=maxprice)

        if minaccessibility is not None:
            activity = activity.filter(accessibility__gte=minaccessibility)

        if maxaccessibility is not None:
            activity = activity.filter(accessibility__lte=maxaccessibility)

        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    