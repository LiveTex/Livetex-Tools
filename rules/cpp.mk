

include $(TOOLS_PATH)/rules/var/cpp.mk
include $(TOOLS_PATH)/rules/aux/cpp.mk


cpp-clean:
	@$(foreach TARGET_NAME, $(CPP_NODES), \
	rm -f $(TARGET_NAME).node;)
	@echo $@: DONE


cpp-build:
	@mkdir -p $(CPP_BUILD_PATH)
	@$(foreach TARGET_NAME, $(CPP_NODES), \
	$(MAKE) -s $(TARGET_NAME).node;)
	@rm -rf $(GIP_BUILD_PATH)
	@echo $@: DONE


cpp: | cpp-clean cpp-build
	@echo $@: DONE

