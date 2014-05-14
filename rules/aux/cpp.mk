

%.node:
	@mkdir -p $(CPP_BUILD_PATH)
	@cp $(CPP_NODES_PATH)/$@ $(CPP_BUILD_PATH)/$@