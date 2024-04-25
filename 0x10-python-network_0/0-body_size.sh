#!/bin/bash
# script to dispaly size of response body using curl
curl -s "$1" | wc -c
