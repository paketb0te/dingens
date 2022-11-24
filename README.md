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
