# Happy Merchant

We're making merchants happy again.

## Commit standards

### Subject

* Feature: Introduces a new feature in the codebase.

* BugFix: Patches a bug in the codebase.

* Documentations: Changes in documentation.

* Refactor: Code change that does not fix a bug nor adds a new feature.

* CI: Change in our CI configuration files and scripts.

* Test: Adding missing test cases or corresponding existing test cases.

* Perf: A code change that improves performance.

### Body

[Description]  (in imperative, e.g. “change” not “changes / changed”  Fixes #[issue number]


## Test Standards

### Name

* [ClassName]Tests.java

### Version

* JUnit 4

### Method Names: 

* [unitOfWork_stateUnderTest_expectedBehavior]

* The unit of work can be as small as a single method, a class or as large as multiple classes. It should represent all the things that are to be tested in this test case and are under control.  Source. If the constructor is tested, use: ctor

* The state under test is the test input, for example validCoordinates, or nameIsNull

* expectedBehaviour is self explanatory. For example: throwsException, returnsNode

* Example: ctor_validCoordiantes_setsCoordinates
