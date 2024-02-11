from rest_framework.views import APIView
from rest_framework.response import Response

from . import utils


class AnswersResponsedAndNotResponsedView(APIView):
    """Step: 1. View to get the number of answers responsed and not responsed."""
    methods = ['GET']

    def get(self, request):
        """Return the number of answers responsed and not responsed."""
        data = utils.get_data_from_api()
        answers_responsed, answers_not_responsed = (utils
            .get_answers_responsed_and_not_responsed(data)
        )

        return Response({
            "answers_responsed": answers_responsed,
            "answers_not_responsed": answers_not_responsed,
        })


class AnswersHighReputationView(APIView):
    """Step: 2. View to get the number of answers with high reputation."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the number of answers with high reputation."""
        data = utils.get_data_from_api()
        answer = utils.get_answers_high_reputation(data)

        return Response({
            "answers_high_reputation": answer,
        })


class AnswersLowNumberOfViewsView(APIView):
    """Step: 3. View to get the number of answers with low number if views."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the number of answers with low reputation."""
        data = utils.get_data_from_api()
        answer = utils.get_answers_low_number_of_views(data)

        return Response({
            "answers_low_number_of_views": answer,
        })


class AnswersOldsAndNewsView(APIView):
    """Step: 4.View to get the number of answers olds and news."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the number of answers olds and news."""""
        data = utils.get_data_from_api()
        old_answer, new_answer = utils.get_answers_olds_and_news(data)

        return Response({
            "answers_old": old_answer,
            "answers_new": new_answer,
        })


class PrintsView(APIView):
    """Step: 5. View to get the number of prints."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the number of prints."""
        data = utils.get_data_from_api()

        step_2 = utils.get_answers_high_reputation(data)
        step_3 = utils.get_answers_low_number_of_views(data)
        step_4A, step_4B = utils.get_answers_olds_and_news(data)

        return Response({
            "answers_high_reputation": step_2,
            "answers_low_number_of_views": step_3,
            "answers_old": step_4A,
            "answers_new": step_4B,
        })

