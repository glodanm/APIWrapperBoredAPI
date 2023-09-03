import requests


class Wrapper:

    def get_activity(self, activity_type=None, participants=None, minprice=None, maxprice=None, minaccessibility=None, maxaccessibility=None):
        
        base_url = "https://www.boredapi.com/api/activity"

        filters = {
            'type': activity_type,
            'participants': participants,
            'minprice': minprice,
            'maxprice': maxprice,
            'minaccessibility': minaccessibility,
            'maxaccessibility': maxaccessibility,
        }
        
        response = requests.get(base_url, params=filters)
        if response.status_code == 200:
            activity_data = response.json()
            return activity_data
        return None
    