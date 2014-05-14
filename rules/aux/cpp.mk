

%.node:
	@mkdir -p $(CPP_BUILD_PATH)
	@cp $(GIP_BUILD_PATH)/Release/$@ $(CPP_BUILD_PATH)/$@

