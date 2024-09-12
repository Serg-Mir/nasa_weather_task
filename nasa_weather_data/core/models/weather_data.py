from typing import List, Dict, Union
from pydantic import BaseModel


class Parameter(BaseModel):
    TS: Dict[str, Union[float, int]]
    T2M: Dict[str, Union[float, int]]
    EVPTRNS: Dict[str, Union[float, int]]


class Properties(BaseModel):
    parameter: dict


class Geometry(BaseModel):
    type: str
    coordinates: List[float]


class Feature(BaseModel):
    type: str
    geometry: Geometry
    properties: Properties


class WeatherData(BaseModel):
    features: List[Feature]


class FinalWeatherData(BaseModel):
    input_coordinates: Geometry
    bbox: tuple
    response: WeatherData


class WeatherDataList(BaseModel):
    data: List[FinalWeatherData]
