
BUILD_PATH ?= ./bin
DEPS_PATH ?= ./node_modules
TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

CSS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/closure-stylesheets.jar

CSS_SOURCES = $(addprefix ./, $(shell cat ./css-src.d))
CSS_MOBILE_SOURCES = $(addprefix ./, $(shell cat ./css-mobile-src.d))


%.css-compile :
	mkdir -p $(BUILD_PATH)
	$(CSS_COMPILER) $(CSS_SOURCES) > $(BUILD_PATH)/main.css;

%.css-mobile-compile :
	mkdir -p $(BUILD_PATH)
	$(CSS_COMPILER) $(CSS_MOBILE_SOURCES) > $(BUILD_PATH)/mobile.css;
