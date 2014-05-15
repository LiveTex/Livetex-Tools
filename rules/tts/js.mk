

%.js-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.jsd
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-externs-compile-compressed: %.jsd %.jsh-node
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


%.js-compile-advanced: %.jsd %.jsh-node
	$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--jscomp_error      checkTypes \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


# WEB ##########################################################################


%.js-web-compile-compressed: %.jsd
	@$(JS_COMPILER) \
  --jscomp_warning    undefinedVars \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-web-externs-compile-compressed: %.jsd %.js-web-headers
	@$(JS_COMPILER) \
	--jscomp_warning    undefinedVars \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


%.js-web-compile-advanced: %.jsd %.js-web-headers
	@$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--jscomp_error      checkTypes \
	--jscomp_warning    undefinedVars \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)

