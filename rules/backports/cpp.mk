

BUILD_PATH ?= ./bin
DEPS_PATH ?= ./node_modules

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

%.node :
	mkdir -p ./bin
	cp ./build/Release/$*.node ./bin
	rm -rf ./build


%.node-clean:
	if [ -e $(BUILD_PATH)/$*.node ]; then \
	rm -rf $(BUILD_PATH)/$*.node; \
	fi;