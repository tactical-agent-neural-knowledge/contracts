BUF ?= npx --yes @bufbuild/buf

PROTOC_VERSION := 29.3
PROTOC_OS := $(shell uname -s | sed -e 's/Darwin/osx/' -e 's/Linux/linux/')
PROTOC_ARCH := $(shell uname -m | sed -e 's/arm64/aarch_64/' -e 's/aarch64/aarch_64/')

.PHONY: gen lint breaking build clean check tools

## The code generators, pinned (buf.gen.yaml runs every plugin locally, not on buf.build).
tools: .tools/protoc/bin/protoc .tools/bin/protoc-gen-go .tools/bin/protoc-gen-connect-go .tools/node_modules/.bin/protoc-gen-es
.tools/bin/protoc-gen-go:
	GOBIN=$(CURDIR)/.tools/bin go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.4
.tools/bin/protoc-gen-connect-go:
	GOBIN=$(CURDIR)/.tools/bin go install connectrpc.com/connect/cmd/protoc-gen-connect-go@v1.18.1
.tools/node_modules/.bin/protoc-gen-es:
	npm install --prefix .tools --no-audit --no-fund --no-save @bufbuild/protoc-gen-es@2.2.3 @bufbuild/protobuf@2.2.3
.tools/protoc/bin/protoc:
	mkdir -p .tools/protoc
	curl -fsSL -o .tools/protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v$(PROTOC_VERSION)/protoc-$(PROTOC_VERSION)-$(PROTOC_OS)-$(PROTOC_ARCH).zip
	unzip -oq .tools/protoc.zip -d .tools/protoc && rm .tools/protoc.zip

## Regenerate Go, TypeScript and Python bindings from proto/.
gen: tools
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
