import pytest


from .models import AirportsModel, FlightsModel, MovementsModel, AirlinesModel


@pytest.mark.django_db
def test_airport_more_movement():
    max_origin = FlightsModel.objects.get_airport_more_movement()
    assert max_origin['total'] == 4
    assert max_origin['origin'] == 3


@pytest.mark.django_db
def test_airlines_more_flights():
    max_airline = FlightsModel.objects.get_airlines_more_flights()
    assert max_airline['total'] == 3
    assert max_airline['airline'] == 2


@pytest.mark.django_db
def test_day_with_more_flights():
    max_day = FlightsModel.objects.get_day_with_more_flights()
    assert max_day['total'] == 6
    max_day_str = str(max_day['day'])
    assert max_day_str == '2021-05-02'


@pytest.mark.django_db
def test_get_airlines_with_more_than_two_fligths_by_day():
    airlines = FlightsModel.objects.get_airlines_with_more_than_two_fligths_by_day()
    assert len(airlines) == 0


@pytest.mark.django_db
def test_get_airlines_with_more_than_two_fligths_by_day_with_other_data():
    airline = AirlinesModel.objects.get(id=1)
    origin = AirportsModel.objects.get(id=1)
    movement = MovementsModel.objects.get(id=1)
    day = '2021-05-12'

    TOTAL_CREATE_SAME_DAY = 3

    all_flights = [
        FlightsModel(
                **{
                    'airline': airline,
                    'origin': origin,
                    'movement': movement,
                    'day': day,
                    },
        )
        for i in range(TOTAL_CREATE_SAME_DAY)
    ]

    FlightsModel.objects.bulk_create(all_flights)

    # test
    airlines = FlightsModel.objects.get_airlines_with_more_than_two_fligths_by_day()

    assert airlines[0]['total'] == TOTAL_CREATE_SAME_DAY
    assert airlines[0]['airline'] == airline.id

