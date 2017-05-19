This TestInputFiles is for files input by the UnitTests.

These files are maintained in SVN in synch with the corresponding test source code, located elsewhere in this UnitTesting project.

If you write a test that relies on a particular input file, place that file in this folder (carefully choosing a name that doesn't conflict with the ones already there), and check it into to SVN.

The exception to this rule is with huge input files. Those should be placed in ../TestDataFiles. You should NOT write tests that relies on huge files unless you also mark it [Explicit]. See BulkImportTesting.cs for examples. Generally, large files are more relevant to Stress Testing, than Unit Testing, so avoid writing unit tests that rely on huge files. If you want to mess with huge files or large numbers of them, rather go extend BulkFileImportTesting instead of the main unit tests.

For tests that compare outputs to known-good results, DO put the known-good files into ../TestInputFiles, as they're, well, inputs to your test. And any output files get created in ../TestOutputFiles. For an example, look at [Test]ImportExportTests.ImportExportImport.

SEE ALSO

../TestOutputFiles/README.txt -- the place for test-generated output files
../TestInputFiles/README.txt -- the place for specific input files
../TestDataFiles/README.txt -- the place for non-specific collections of input files