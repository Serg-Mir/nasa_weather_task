import logging

from shapely.geometry import shape
from nasa_weather_data.core.clients import WeatherClient


logger = logging.getLogger(__name__)  # type: ignore


def validate_coordinates(coordinate_type, min_value, max_value):
    """Due to API limitations, we need to ensure that input coordinates meet the size requirements."""
    if max_value - min_value < 2:
        extender = 2 - (max_value - min_value)
        logger.debug(
            "%s is too small to retrieve weather data, "
            "changing min from %s to %s, max from %s to %s",
            coordinate_type,
            min_value,
            min_value - (extender / 2),
            max_value,
            max_value + (extender / 2),
        )
        min_value -= extender / 2
        max_value += extender / 2
    elif max_value - min_value > 10:
        reducer = (max_value - min_value) - 10
        logger.debug(
            "%s is too big to retrieve weather data, "
            "changing min from %s to %s, max from %s to %s",
            coordinate_type,
            min_value,
            min_value - (reducer / 2),
            max_value,
            max_value + (reducer / 2),
        )
        min_value += reducer / 2
        max_value -= reducer / 2
    return min_value, max_value


def retrieve_data(
    input_data: list[dict], parameters="TS,T2M,EVPTRNS", start_period="2006", end_period="2007"
):
    client = WeatherClient()
    new_data = []
    for input_coordinates in input_data:
        coordinates = shape(input_coordinates["boundary"])

        bbox = coordinates.bounds
        logger.debug("Calculated bbox: %s for %s", bbox, input_coordinates)

        lat_min, lat_max = validate_coordinates("latitude", bbox[0], bbox[2])
        lon_min, lon_max = validate_coordinates("longitude", bbox[1], bbox[3])

        data = {
            "start": start_period,
            "end": end_period,
            "latitude-min": lat_min,
            "latitude-max": lat_max,
            "longitude-min": lon_min,
            "longitude-max": lon_max,
            "community": "ag",
            "parameters": parameters,
            "format": "json",
            "header": False,
        }
        # more parameters info: https://power.larc.nasa.gov/docs/services/api/temporal/monthly/#request-structure

        api_response = client.request_monthly_regional_data(params=data)
        if api_response.ok:
            logger.info("Successful weather data retrieval for %s", input_coordinates)
            new_data.append(
                {
                    "input_coordinates": input_coordinates,
                    "bbox": bbox,
                    "response": api_response.json()["features"],
                }
            )
        else:
            logger.info(
                "%s has been skipped to fetch weather data due to %s",
                input_coordinates,
                api_response.json(),
            )
    return new_data
