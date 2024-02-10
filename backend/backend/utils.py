import requests


API_URL = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

def get_data_from_api():
    """Get data from the API."""
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception('Error getting data from API')
    return response.json()['items']


def get_answers_responsed_and_not_responsed(data):
    """Get the number of answers responsed and not responsed."""
    answers_responsed = 0
    answers_not_responsed = 0
    for item in data:
        if item['is_answered']:
            answers_responsed += 1
        else:
            answers_not_responsed += 1
    return answers_responsed, answers_not_responsed

def get_answers_high_reputation(data):
    """Get the number of answers with high reputation."""
    answers_high_reputation = -1
    answer = {}
    for item in data:
        if item['score'] > answers_high_reputation:
            answers_high_reputation = item['score']
            answer = item
    return answer

def get_answers_low_number_of_views(data):
    """Get the number of answers with low number of views."""
    if not data:
        return {}

    low_number_of_views = data[0]['view_count']
    answer = data[0]

    data.pop(0)

    for item in data:
        if item['view_count'] < low_number_of_views:
            low_number_of_views = item['view_count']
            answer = item

    return answer


def get_answers_olds_and_news(data):
    """Get the answers most olds and news."""
    if not data:
        return {}, {}

    old_answers_date = data[0]['creation_date']
    old_answer = data[0]

    new_answers_date = data[0]['creation_date']
    new_answer = data[0]

    data.pop(0)

    for item in data:
        if item['creation_date'] > old_answers_date:
            old_answers_date = item['creation_date']
            old_answer = item

        elif item['creation_date'] < new_answers_date:
            new_answers_date = item['creation_date']
            new_answer = item

    return old_answer, new_answer

