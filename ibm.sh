#!/usr/bin/env bash

curl -X POST \
-H "Content-Type: application/json" \
-u "apikey:fRu2v8uevQ9rgpssSnnz0OcjrJJRW5_fj6lfs8bDdkkT" \
-d @parameters.json \
"https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2019-07-12"
