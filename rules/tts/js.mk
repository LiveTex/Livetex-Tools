

%.js-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-simple: %.jsd %.jsh-node
	$(JS_COMPILER) \
	--compilation_level WHITESPACE_ONLY \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.jsd %.jsh-node
	@$(JS_COMPILER) \
  	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


# WEB ##########################################################################


%.js-web-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-web-compile-simple: %.jsd %.jsh-web
	@$(JS_COMPILER) \
	--compilation_level WHITESPACE_ONLY \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-web-compile-compressed: %.jsd %.jsh-web
	@$(JS_COMPILER) \
  	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)
