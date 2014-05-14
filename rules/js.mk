

include $(TOOLS_PATH)/rules/all.mk
include $(TOOLS_PATH)/rules/var/js.mk
include $(TOOLS_PATH)/rules/aux/js.mk
include $(TOOLS_PATH)/rules/tts/js.mk


js-clean:
	@rm -rf $(wildcard $(JS_BUILD_PATH)/*.js) $(JS_EXTERNS_PATH)
	@echo $@: DONE


js-tests:
	@$(foreach TARGET_NAME, $(JS_TESTS_NAMES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-test);)
	@echo $@: DONE


js-lint:
	@$(foreach TARGET_NAME, $(JS_LISTS_NAMES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-lint);)
	@echo $@: DONE


js-check: js-lint
	@$(foreach TARGET_NAME, $(JS_TEMPLATES_NAMES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-check);)
	@echo $@: DONE


js-build: js-clean
	@mkdir -p $(JS_BUILD_PATH)
	@$(foreach TARGET_NAME, $(JS_TEMPLATES_NAMES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-assemble);)
	@echo $@: DONE


js-externs:
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(foreach TARGET_NAME, $(JS_FILES_NAMES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).js-extract-externs);)
	@echo $@: DONE


js: | js-build js-externs
	@echo $@: DONE

