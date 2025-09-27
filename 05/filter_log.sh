#!/bin/bash

set -ueo pipefail

grep "$( grep -v -e 'GET' -e 'POST' requests.txt )" apache.log
