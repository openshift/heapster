package oscmd

import (
	"heapster/tools/junitreport/pkg/builder"
	"heapster/tools/junitreport/pkg/parser"
	"heapster/tools/junitreport/pkg/parser/stack"
)

// NewParser returns a new parser that's capable of parsing `os::cmd` test output
func NewParser(builder builder.TestSuitesBuilder, stream bool) parser.TestOutputParser {
	return stack.NewParser(builder, newTestDataParser(), newTestSuiteDataParser(), stream)
}
