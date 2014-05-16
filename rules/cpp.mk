

include $(TOOLS_PATH)/rules/var/cpp.mk
include $(TOOLS_PATH)/rules/aux/cpp.mk


cpp-clean:
	@$(foreach NODE_NAME, $(BUILT_NODES), \
	rm -f $(CPP_BUILD_PATH)/$(NODE_NAME).node)
	@echo $@: DONE


cpp-build:
	@mkdir -p $(CPP_BUILD_PATH)
	@$(foreach TARGET_NAME, $(GYP_NODES), \
	$(MAKE) -s $(TARGET_NAME).node;)
	@rm -rf $(GIP_BUILD_PATH)
	@echo $@: DONE


cpp: | cpp-clean cpp-build
	@echo $@: DONE

