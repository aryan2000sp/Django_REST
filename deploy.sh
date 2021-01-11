#!/bin/bash
message=""
for i in "$@"
do
	message="${message} ${i}"
done

git add .

git commit -m "$message"

git push origin main

