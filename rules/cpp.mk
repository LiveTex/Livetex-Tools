

SOURCE_PATH ?= ./src
BUILD_PATH ?= ./bin
HEADERS_BUILD_PATH ?= ./externs
DEPS_PATH ?= ./node_modules

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

NODE_GYP = $(TOOLS_HOME)/tools/node-gyp/bin/node-gyp.js

%.node :
	$(NODE_GYP) configure build
	cp ./build/Release/$*.node ./bin
	rm -rf ./build


%.cpp-clean:
	if [ -e $(BUILD_PATH)/$*.node ]; then \
	rm -rf $(BUILD_PATH)/$*.node; \
	fi;
