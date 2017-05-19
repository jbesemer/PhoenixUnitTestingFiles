This TestDataFiles folder is for large numbers of files input by the UnitTests, some of them quite huge. It's more for stress testing than unit testing, per se.

The folder and this readme file are checked-into SVN, so they'll be created on check-out, but none of the huge files are nor ever should be added to SVN. What to do about saving/restoring them is TBD.

These tests originated from an attempt to try importing as many files as possible. Thus the tests themselves do NOT refer to any individual files by name. The tests are all in BulkFileImportTesting.cs, and you'll see that the tests themselves test all the files in particular sub-directories, without regard to individual file names.

You should NOT write tests that rely on huge files unless you also mark it [Explicit]. See BulkImportTesting.cs for examples. Generally, large files are more relevant to Stress Testing, than Unit Testing, so avoid writing unit tests that rely on huge files.

For tests that compare outputs to known-good results, put the known-good files into ../TestInputFiles, as they're, er... inputs. And the output files get created in this folder. For an example, look at [Test]ImportExportTests.ImportExportImport.

SEE ALSO

../TestOutputFiles/README.txt -- the place for test-generated output files
../TestInputFiles/README.txt -- the place for specific input files
../TestDataFiles/README.txt -- the place for non-specific collections of input files