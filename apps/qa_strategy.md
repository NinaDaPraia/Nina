# QA Strategy

We are going to follow the [Test Pyramid](http://martinfowler.com/bliki/TestPyramid.html) approach.

![Bilby Stampede](http://sharkzp.github.io/images/test_pyramid_with_contract.png)


1. Unit tests: since it's an API, a lot of things won't make sense to test unitary, so we are going to use unit tests for auxiliary classes and methods.
1. Integration/API tests: we are going to use api tests for validations, happy paths, edge cases (when it's not possible use unit tests), we should try to do a black box testing approach.
1. Contract tests: we have contract tests to make sure that we do not break the contract with our consumers when change something in the API. We are going to use pacto as contract validator and json files to write the contracts.
1. UI/e2e tests: the e2etests are going to cover the full integration between the client and the server.

### Tools
1. [Pacto](https://github.com/thoughtworks/pacto): it is a framework for Integration Contract Testing.
2. [Flake8](https://pypi.python.org/pypi/flake8): Flake8 is a wrapper around [PyFlakes](https://pypi.python.org/pypi/pyflakes), [pep8](https://pypi.python.org/pypi/pep8), [Ned Batchelder’s McCabe script](https://pypi.python.org/pypi/mccabe). We are going to use flake8 to check error codes (like unused import, etc) and check the code against some of the style conventions in [PEP 8](https://www.python.org/dev/peps/pep-0008/).
3. [Factory boy](https://github.com/rbarrois/factory_boy): is a fixtures replacement based on thoughtbot's factory_girl. As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex object.

