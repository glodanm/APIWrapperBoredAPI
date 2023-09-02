from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .wrapper import Wrapper
from .models import Activity
from .serializers import ActivitySerializer


class GetActivityAPI(APIView):

    def get(self, request):
        data = request.data
        wrapper = Wrapper()
        activity_data = wrapper.get_activity(
            activity_type=data.get('type'),
            participants=data.get('participants'),
            minprice=data.get('minprice'),
            maxprice=data.get('maxprice'),
            minaccessibility=data.get('minaccessibility'),
            maxaccessibility=data.get('maxaccessibility'),
        )
        serializer = ActivitySerializer(data=activity_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class ActivityList(APIView):

    def get(self, request):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)
    