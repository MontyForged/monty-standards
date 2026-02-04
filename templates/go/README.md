# Go Template

Copy these files to your Go project:

```
.
├── go.mod
├── main.go
└── main_test.go
```

## Usage

```bash
# Run tests
go test -v

# Run linter
golangci-lint run

# Format code
gofmt -w .

# Build
go build -o my-project
```

## go.mod Template

```go
module github.com/username/my-project

go 1.21
```
