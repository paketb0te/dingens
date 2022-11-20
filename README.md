# dingens

## Overview

### Components

- Website
- API
- Generating Backend

### Flow

1. On the website, a user selects his desired options and sends them to the API.
1. The API then translates these options into a prompt / starting image / whatever that can be processed by the generating backend and sends it there.
1. The generating backend processes the received *stuff* and returns an asset to the API.
1. The API returns this asset to the users browser.

## TODO

- [ ] use dreamstudio API and understand the response format
- [ ] build stub for dreamstudio API
