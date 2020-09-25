# gcov

#GCOV 6.2.0 

GCov is a source code coverage analysis tool which can report line, function and branch coverage.

The GCov utility creates a temporary copy of the input source code, and instruments it so that a coverage data base will be produced when you run the resulting code.

# Step1: BUILDING THE EXEUTABLE 

Create a GCOV BUILD 

• Create an instrumented binary: use the gcc, g++ or gfortan compiler(s), with the “-fprofile-arcs -ftest-coverage” or “--coverage” flags.

• Run the instrumented binary; the coverage DB is written to a series of location where the object files reside.

• Run gcov to process the individual DB files and generate an overall line, function, and branch coverage report


# Step 2 : Running the executable

To avoid having to wait for locks to update a common database at the end of each run, you can create the coverage database on a per test case basis and merge the data in a separate step.

For each test, specify the location (with absolute path) where the gcov database will be created via the “GCOV_PREFIX” environment variable.

setenv GCOV_PREFIX <>.gcov


# Step 3 :  Generating the report

Use the following steps generate and view the lcov report of your gcov data

1. Set environment variable GCOV_PREFIX to point a directory in which you wish to store the .gcda (coverage data) files:

e.g.: setenv GCOV_PREFIX /foo/gcov

If the above directory already exists, the data in it will be accumulated for each new test that you run (i.e. run test1.tcl, then test2.tcl etc., and the data will cover both testcase runs)

2. Run your test(s) to exercise the required code with your gcov-enabled exe

3. Use the gcov post-process script to merge your individual gcov data files, apply your suppressions, etc.:

e.g.: <path>/gcov_post_process.py -src <your client root> -in $GCOV_PREFIX -out ./gcov_out -x <your suppression file> -lcov

• The above step will generate _GCOV_.gcov and _LCOV_.txt files under the specified ./gcov_out dir


• <path> above should be /depot/tools/code_coverage/utils/1.0 or any newer version that is available 

• Add option ‘-branch’ for report branch coverage

4. Use lcov’s genhtml tools to create your report (as html pages):

e.g.: <path>/genhtml –prefix <your client root> --ignore-errors source gcov_out/_LCOV_.txt --legend --title "your title” --output-directory ./lcov

Add option “--branch-coverage” for branch coverage

5. Use a browser to view ./lcov/index.html

#                    Hit         TOTAL           COVERAGE 
Line         
BRANCHES
TOTAL
