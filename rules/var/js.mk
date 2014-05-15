

################################################################################
# PATHS
################################################################################


# PROJECT PATHS ################################################################


JS_BUILD_PATH       ?= $(PROJECT_PATH)/bin
JS_EXTERNS_PATH     ?= $(PROJECT_PATH)/externs
JS_SOURCES_PATH     ?= $(PROJECT_PATH)/lib
ENV_EXTERNS_PATH    ?= $(TOOLS_PATH)/externs


# PREREQUISITES PATHS ##########################################################


vpath %.jst         $(TEMPLATES_PATH)/js
vpath %.jsd         $(SOURCES_LISTS_PATH)/js
vpath %.js          $(JS_BUILD_PATH)


################################################################################
# VARS
################################################################################


# TOOLS ########################################################################


JS_COMPILER         ?= java -jar $(TOOLS_PATH)/tools/closure-compiler.jar \
                    --warning_level     VERBOSE \
                    --language_in       ECMASCRIPT5_STRICT


JS_LINTER           ?= $(TOOLS_PATH)/tools/closure-linter/gjslint.py \
		                --strict \
		                --custom_jsdoc_tags "namespace, event"


JS_EXTERNS_XTRACTOR ?= $(TOOLS_PATH)/tools/externs-extractor/externsExtractor.py


# NAMES ########################################################################


JS_FILES            ?= $(foreach FILE, \
                       $(shell find $(JS_BUILD_PATH) \
                       -maxdepth 1 \
                       -iname '*.js'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_LINT            ?= $(foreach FILE, \
                       $(shell find $(SOURCES_LISTS_PATH)/js \
                       -maxdepth 1 \
                       -iname '*.jsd' ), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_TEMPLATES        ?= $(foreach FILE, \
                       $(shell find $(TEMPLATES_PATH)/js \
                       -maxdepth 1 \
                       -iname '*.jst'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_TESTS            ?= $(foreach FILE, \
                       $(shell find $(JS_BUILD_PATH) \
                       -maxdepth 1 \
                       -iname 'test-*.js'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))

