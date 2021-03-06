

################################################################################
# PATHS
################################################################################


# PROJECT PATHS ################################################################


JS_BUILD_PATH       ?= $(PROJECT_PATH)/bin
JS_EXTERNS_PATH     ?= $(PROJECT_PATH)/externs
JS_SOURCES_PATH     ?= $(PROJECT_PATH)/lib
JS_PACKAGES_PATH    ?= $(PROJECT_PATH)/packages

NODE_EXTERNS_PATH   ?= $(TOOLS_PATH)/externs


# PREREQUISITES PATHS ##########################################################


vpath %.jst         $(CONFIG_PATH)
vpath %.jsd         $(CONFIG_PATH)
vpath %.js          $(JS_BUILD_PATH)


################################################################################
# VARS
################################################################################


# TOOLS ########################################################################


JS_COMPILER         ?= java -jar $(TOOLS_PATH)/tools/closure-compiler.jar \
                    --warning_level     VERBOSE \
                    --language_in       ECMASCRIPT5_STRICT \
                    --jscomp_error      checkTypes \
                    --jscomp_error      suspiciousCode \


JS_LINTER           ?= $(TOOLS_PATH)/tools/closure-linter/gjslint.py \
		                --strict \
		                --custom_jsdoc_tags "namespace, event"


JS_EXTERNS_XTRACTOR ?= $(TOOLS_PATH)/tools/externs-extractor/externsExtractor.py


# NAMES ########################################################################


JS_EXTERNS          ?= $(foreach FILE, \
                       $(shell find $(JS_BUILD_PATH) \
                       -maxdepth 1 \
                       -iname '*.js'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_LINT             ?= $(foreach FILE, \
                       $(shell find $(CONFIG_PATH) \
                       -maxdepth 1 \
                       -iname '*.jsd' ), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_CHECK            ?= $(foreach FILE, \
                       $(shell find $(CONFIG_PATH) \
                       -maxdepth 1 \
                       -iname '*.jst'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_TEMPLATES        ?= $(foreach FILE, \
                       $(shell find $(CONFIG_PATH) \
                       -maxdepth 1 \
                       -iname '*.jst'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


JS_TESTS            ?= $(foreach FILE, \
                       $(shell find $(JS_BUILD_PATH) \
                       -maxdepth 1 \
                       -iname 'test-*.js'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))

