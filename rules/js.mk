

TOOLS_PATH ?= $(shell pwd)/node_modules/livetex-tools


include $(TOOLS_PATH)/rules/all.mk
include $(TOOLS_PATH)/rules/var/js.mk
include $(TOOLS_PATH)/rules/aux/js.mk
include $(TOOLS_PATH)/rules/tts/js.mk


js-clean:
	@rm -rf $(wildcard $(JS_BUILD_PATH)/*.js) $(JS_EXTERNS_PATH)
	@echo $@: DONE


js-tests:
	@$(foreach TARGET_NAME, $(JS_TESTS), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-test);)
	@echo $@: DONE


js-lint:
	@$(foreach TARGET_NAME, $(JS_LINT), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-lint);)
	@echo $@: DONE


js-check: js-lint
	@$(foreach TARGET_NAME, $(JS_CHECK), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-check);)
	@echo $@: DONE


js-build: js-clean
	@mkdir -p $(JS_BUILD_PATH)
	@$(foreach TARGET_NAME, $(JS_TEMPLATES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-assemble);)
	@echo $@: DONE


js-externs:
	@$(foreach TARGET_NAME, $(JS_EXTERNS), \
	$(MAKE) -s $(shell mkdir -p $(JS_EXTERNS_PATH) && \
	echo $(TARGET_NAME).js-extract-externs);)
	@echo $@: DONE


js: | js-build js-externs
	@echo $@: DONE
