# Makefile

## Configuration

BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))


## Install dependencies
.PHONY: install
install:
	pip install -r requirements.txt
