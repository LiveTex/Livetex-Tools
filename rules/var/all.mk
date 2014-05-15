

################################################################################
# PATHS
################################################################################


# PROJECT PATHS ################################################################


PROJECT_PATH        ?= $(shell pwd)
CONFIG_PATH         ?= $(PROJECT_PATH)/etc/build
MODULES_PATH        ?= $(PROJECT_PATH)/node_modules
TEMPLATES_PATH      ?= $(CONFIG_PATH)/templates
SOURCES_LISTS_PATH  ?= $(CONFIG_PATH)/sources-lists


################################################################################
# VARS
################################################################################


# TOOLS ########################################################################


REVERSIONER         ?= $(TOOLS_PATH)/tools/reversioner.py package.json


TEMPLATER           ?= $(TOOLS_PATH)/tools/templater.py


################################################################################


SUBMODULES = $(foreach SUBMODULE, \
             $(shell grep path .gitmodules | sed 's/.*= //'), \
             $(SUBMODULE))