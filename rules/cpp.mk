

BUILD_PATH ?= ./bin
DEPS_PATH ?= ./node_modules

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

NODE_GYP = $(TOOLS_HOME)/tools/node-gyp/bin/node-gyp.js

%.node :
	$(NODE_GYP) configure build
	mkdir -p ./bin
	cp ./build/Release/$*.node ./bin
	rm -rf ./build


%.cpp-clean:
	if [ -e $(BUILD_PATH)/$*.node ]; then \
	rm -rf $(BUILD_PATH)/$*.node; \
	fi;
