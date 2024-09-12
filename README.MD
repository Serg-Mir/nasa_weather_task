# Nasa Weather Data Retrieval Task

A test task to retrieve a **Monthly** data for a specific coordinates for temperature, evaporation and Temperature at 2 meters above ground level

## Usage

Input should be a list of dicts with boundary
```text
--coordinates (A JSON array of coordinates with `boundary` inside)
or
--points (A JSON array of points as an alternative, not yet implemented)

```


Execution example:
```text
$ python nasa_weather_data/main.py --coordinates '[{"boundary": {
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
                            [11.544038703, 59.44444527]
                        ]
                    ]
                }},{"boundary": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [7.044038703, 56.41444527],
                            [9.31452531, 56.144443921],
                            [9.144685887, 56.144263788],
                            [9.14501029, 56.144262887],
                            [9.145008662, 56.144083204],
                            [9.314521246, 56.433994714],
                            [9.314517995, 56.433635349],
                            [9.31403221, 56.43372654],
                            [9.313865954, 56.423277783],
                            [11.344038703, 59.44444527]
                        ]
                    ]
                }}]'


INFO: [nasa_weather_data.data_retrieval:retrieve_data:169] Successful weather data retrieval for {coordinates}. Time spent: 0:00:18.881976
```

## Development

### Initial configuration

If you need to specify local development project settings, create a .env file in the root of the project and specify them as environment variables.

### Docker setup (recommended)

Make sure you have [Docker](https://docs.docker.com) installed in your local machine.

Create a Docker image from the nasa-weather-data project:

```bash
DOCKER_BUILDKIT=1 docker build --ssh default -t nasa-weather-data .
```

**Note:** If you are using macOS, you may need to run ssh-add to add private key identities to the authentication agent first.

Run the Docker container once the image is built:

```bash
docker run --env-file .env nasa-weather-data <ARGUMENTS>
```

### Native setup

To develop and run the project in native setup it is extremely recommended to use a
[Python virtual environment](https://docs.python.org/3/tutorial/venv.html). There is a range of
options to create a virtual environment, but here we will describe the easiest one which is using
the `venv` builtin module.

1. Type on the terminal:
   ```bash
   python -m venv ~/.virtualenvs/nasa-weather-data
   ```
2. Activate the virtual environment:
   ```bash
   source ~/.virtualenvs/nasa-weather-data/bin/activate
   ```
3. Install project requirements and development requirements:
   ```bash
   pip install -r requirements/requirements.txt
   ```

You can now test the basic project setup by running this command in terminal:

```bash
python nasa_weather_data/main.py
```

:warning: **Note:** you might need to add the generated project root directory to the
[`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) in some cases:

```bash
export PYTHONPATH="{$PYTHONPATH}:/absolute/path/to/nasa-weather-data"
```


## Contributing

Before contributing to the nasa-weather-data, install pre-commit to ensure your changes are checked for style and standards:

    $ pre-commit install

[pre-commit](https://pre-commit.com) is installed automatically in development environment by pip.
If you are running the Docker setup, please install it with `pip` in your host machine:

    $ pip install pre-commit
