import pytest
from nasa_weather_data.services.data_retrieval import (
    retrieve_data,
)


@pytest.mark.parametrize(
    ["input_data", "expected_response_len", "expected_bbox"],
    [
        pytest.param(
            [
                {
                    "boundary": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [7.144038703, 56.44444527],
                                [9.34452531, 56.444443921],
                                [9.344685887, 56.444263788],
                                [9.34501029, 56.444262887],
                                [9.345008662, 56.444083204],
                                [9.344521246, 56.443994714],
                                [9.344517995, 56.443635349],
                                [9.34403221, 56.44372654],
                                [9.343865954, 56.443277783],
                                [11.544038703, 59.44444527],
                            ]
                        ],
                    },
                }
            ],
            1,
            (7.144038703, 56.443277783, 11.544038703, 59.44444527),
            id="Successfully processed new area",
        ),
    ],
)
@pytest.mark.vcr
def test_each_step(input_data, expected_response_len, expected_bbox):
    api_results = retrieve_data(input_data=input_data)
    assert api_results

    assert expected_response_len == len(api_results)
    assert expected_bbox == (api_results[0]["bbox"])
