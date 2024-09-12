import argparse
import logging.config

from nasa_weather_data.core.config.logging import logging_config
from nasa_weather_data.services.data_retrieval import retrieve_data

logger = logging.getLogger("weather_data_acquisition_task")  # type: ignore


def main():
    # Configure Python logging system before starting.
    logging.config.dictConfig(logging_config)

    # Parse user input arguments.
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--coordinates",
        help="A JSON array of geometry list as a `boundary`.",
        type=eval,
    )
    # ToDo: Point input implementation pending
    group.add_argument(
        "--points",
        help="A JSON array of lat,lon lists",
        type=eval,
    )
    args = parser.parse_args()

    # Obtain data from the given source.
    if args.points:
        # ToDo: add related condition
        coordinates = args.points

    else:
        coordinates = args.coordinates

    print(retrieve_data(coordinates))


if __name__ == "__main__":
    main()
