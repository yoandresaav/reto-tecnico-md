import pytest

from . import utils

dummy_data = [
        {
            "id": 1, # added for testing purposes
            "is_answered": True,
            "score": 10,
            "view_count": 100,
            "creation_date": 123213123,
        },
        {
            "id": 2, # added for testing purposes
            "is_answered": False,
            "score": 5,
            "view_count": 50,
            "creation_date": 123213123,
        },
        {
            "id": 3, # added for testing purposes
            "is_answered": False,
            "score": 8,
            "view_count": 200,
            "creation_date": 123213120,
        },
        {
            "id": 4, # added for testing purposes
            "is_answered": False,
            "score": 2,
            "view_count": 10,
            "creation_date": 123213129,
        },

]


@pytest.fixture(autouse=True)
def use_dummy_cache_backend(settings):
    settings.CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }


def test_get_answers_responsed_and_not_responsed():
    """Test get_answers_responsed_and_not_responsed function."""
    responsed, not_responsed = utils.get_answers_responsed_and_not_responsed(dummy_data)
    assert responsed == 1
    assert not_responsed == 3


def test_get_answers_high_reputation():
    """Test get_answers_high_reputation function."""
    answer = utils.get_answers_high_reputation(dummy_data)
    assert answer['id'] == 1

def test_get_answers_low_number_of_views():
    """Test get_answers_low_number_of_views function."""
    answer = utils.get_answers_low_number_of_views(dummy_data)
    assert answer['id'] == 4

def test_get_answers_olds_and_news():
    """Test get_answers_olds_and_news function."""
    old_answer, new_answer = utils.get_answers_olds_and_news(dummy_data)
    assert old_answer['id'] == 4
    assert new_answer['id'] == 3
