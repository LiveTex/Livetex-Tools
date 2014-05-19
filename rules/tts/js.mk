

%.js-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.jsd %.jsh-node
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


# WEB ##########################################################################


%.js-web-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-web-compile-compressed: %.jsd %.jsh-web
	@$(JS_COMPILER) \
  --js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)

