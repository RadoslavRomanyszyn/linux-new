#!/bin/bash

set -ueo pipefail

for png_img in *.png; do
	target_img="$( basename "$png_img" .png ).jpg"
	convert "$png_img" "$target_img"
done
