# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Converted Travis to CircleCI.
- Updated dependencies.

## [1.1.0] - 2019-06-19
### Added
- Optional argument for passing STS credentials.
- Unit tests via pytest.
- Travis CI integration and build status.
- Requirements for local development.
### Changed
- Converted boto3auth to Class.
- Moved account_id, role to class properties.
- Updated README to reflect new structure.

## [1.0.2] - 2019-06-05
### Fixed
- Changed sample arguments to be easier to read.
- Mistype in README regarding setting a resource.
- Incorrect references to client/service instead of client/resource.

## [1.0.0] - 2019-06-05
### Added
- Auth function with support for AWS services.
- Package for PyPi.

[Unreleased]: https://github.com/mtslzr/boto3auth/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/mtslzr/boto3auth/compare/v1.0.2...v1.1.0
[1.0.2]: https://github.com/mtslzr/boto3auth/compare/v1.0.0...v1.0.2
[1.0.0]: https://github.com/mtslzr/boto3auth/releases/tag/v1.0.0