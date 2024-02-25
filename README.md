# dingens

## Overview

### Components

- Website
- API
- Generating Backend

### Flow

1. On the website, a user selects his desired options and sends them to the API.
1. The API then translates these options into a prompt / starting image / whatever that can be processed by the generating backend and sends it there.
2. The generating backend processes the received *stuff* and returns one or more assets to the API.
3. The API stores these assets somewhere where they can be retrieved by the client and returns an array of URLs (for the assets) to the users browser where they are loaded dynamically.

## Installation

This project uses [`poetry`](https://python-poetry.org/) for managing dependencies and virtualenvs.

If you don't have it installed, it is recommended to follow the [installation instructions](https://python-poetry.org/docs/#installation).

With poetry installed, clone this repository and install a python virtual environment with all dependencies:

```bash
git clone git@github.com:paketb0te/dingens.git
cd dingens
poetry install
```

Now you have a virtualenv which you can easily activate / deactivate with `poetry shell` / `exit`.

If you want ro run the app locally for testing, start uvicorn like so:

```bash
uvicorn main:app --reload
```

If you want to use the `DreamstudioBackend` (you can configure the used backend in [`config.py`](app/config.py)), you must provide an API key as environment variable before starting the app (go [HERE](https://beta.dreamstudio.ai/membership?tab=apiKeys) to see yours):

```bash
export STABILITY_KEY=api-key
```
