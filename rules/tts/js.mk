

%.js-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.jsd
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-externs-compile-compressed: %.jsd
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(JS_NODE_HEADERS)


%.js-compile-advanced: %.jsd
	@$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--jscomp_error      checkTypes \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(JS_NODE_HEADERS)


# WEB ##########################################################################


%.js-web-externs-compile-compressed: %.jsd
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(JS_WEB_HEADERS)


%.js-web-compile-advanced: %.jsd
	@$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--jscomp_error      checkTypes \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(JS_WEB_HEADERS)

