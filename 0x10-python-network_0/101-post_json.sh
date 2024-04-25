#!/bin/bash
# sends a JSON POST request to a URL passed ,send post with file content,
#json file passed as arg. then display the body of the response.
curl -s X POST -H "Content-Type: application/json" -d  "$(cat "$2")" "$1"
