# chatbot

#GCOV 6.2.0 

GCov is a source code coverage analysis tool which can report line, function and branch coverage.

The GCov utility creates a temporary copy of the input source code, and instruments it so that a coverage data base will be produced when you run the resulting code.

Step1: BUILDING THE EXEUTABLE 

Create a GCOV BUILD 

• Create an instrumented binary: use the gcc, g++ or gfortan compiler(s), with the “-fprofile-arcs -ftest-coverage” or “--coverage” flags.

• Run the instrumented binary; the coverage DB is written to a series of location where the object files reside.

• Run gcov to process the individual DB files and generate an overall line, function, and branch coverage report


# Running the executable

To avoid having to wait for locks to update a common database at the end of each run, you can create the coverage database on a per test case basis and merge the data in a separate step.

For each test, specify the location (with absolute path) where the gcov database will be created via the “GCOV_PREFIX” environment variable.

setenv GCOV_PREFIX <>.gcov

# Generating the report
