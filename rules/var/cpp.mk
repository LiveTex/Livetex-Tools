

################################################################################
# PATHS
################################################################################


# PROJECT PATHS ################################################################


CPP_BUILD_PATH      ?= $(PROJECT_PATH)/bin
GIP_BUILD_PATH      ?= $(PROJECT_PATH)/build
CPP_NODES_PATH      ?= $(GIP_BUILD_PATH)/Release


################################################################################
# VARS
################################################################################


BUILT_NODES         ?= $(foreach FILE, \
                       $(shell find $(CPP_BUILD_PATH) \
                       -maxdepth 1 \
                       -iname '*.node'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


GYP_NODES           ?= $(foreach FILE, \
                       $(shell find $(CPP_NODES_PATH) \
                       -maxdepth 1 \
                       -iname '*.node'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))

