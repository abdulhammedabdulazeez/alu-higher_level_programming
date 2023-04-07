#!/bin/bash
#5-post_params.sh
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"; 
