CODE=nginx_configurator
.PHONY: lint
lint:
	ruff $(CODE)
	black --check $(CODE)
	mypy $(CODE)

.PHONY: format
format:
	ruff --fix $(CODE)
	black $(CODE)