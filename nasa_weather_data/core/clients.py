import logging
from requests import Session

from nasa_weather_data.core.config.settings import get_settings

logger = logging.getLogger(__name__)  # type: ignore


class WeatherClient:
    def __init__(self, point=False, headers: dict | None = None):
        #  default_api_url:  "https://power.larc.nasa.gov/api/temporal/monthly/regional"

        self.config_data_url = (
            get_settings().regional_api_url if not point else get_settings().point_api_url
        )
        self.config_params_url = "https://power.larc.nasa.gov/api/system/manager/metrics/parameters"
        self.headers = headers
        self.session = Session()

    def request_params(self, params: dict | None = None, data: dict | None = None):
        with self.session:
            response = self.session.request("get", self.config_params_url, params=params, data=data)
            return response

    def request_monthly_regional_data(self, params: dict):
        """Successful request example:
        https://power.larc.nasa.gov/api/temporal/monthly/regional?start=2010&end=2013&
        latitude-min=80&latitude-max=90&longitude-min=80&longitude-max=90&community=sb&
        parameters=TS&format=json&header=true

        Get params: https://power.larc.nasa.gov/api/pages/?urls.primaryName=Manager"""

        with self.session:
            url = self.config_data_url
            response = self.session.request("get", url, params=params)
            return response
