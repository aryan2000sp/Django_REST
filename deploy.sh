#!/bin/bash
message=""
for i in "$@"
do
	message="${i} ${message}"
done

git add .

git commit -m "$message"

git push origin main

