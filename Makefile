BUF ?= npx --yes @bufbuild/buf

.PHONY: gen lint breaking build clean check

## Regenerate Go, TypeScript and Python bindings from proto/.
gen:
	$(BUF) generate

lint:
	$(BUF) lint

## Fail if this branch breaks wire compatibility with main. This is the check
## that makes the polyrepo safe: what a monorepo catches at build time.
breaking:
	$(BUF) breaking --against '.git#branch=main'

build:
	go build ./...

clean:
	rm -rf gen/go/tank gen/ts/src/tank gen/python/tank

## Everything CI runs.
check: lint gen build
	@git diff --exit-code --stat gen/ \
		|| (echo ""; echo "ERROR: generated code is stale. Run 'make gen' and commit."; exit 1)
	@echo "contracts OK"
