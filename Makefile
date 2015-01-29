

publish:
	@npm version patch
	@npm ls 1> /dev/null
	@npm publish
	@git push
	@echo $@: DONE

