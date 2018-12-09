Python Travis Deploy
====================

A test project for deploying to PyPI from Travis

Deployment Strategy
-------------------

- Any user can create a new branch and commits that puts the package
  into a deployable state. (Updating changelog, putting release date, etc)
  The branch must be named ``release-x.x.x`` to trigger integration tests
- User creates a Pull Request to the repo as normal.
- Travis runs unit tests as normal.
- Travis runs integration tests due to the ``release-x.x.x`` branch name.
- Once merged any maintainer can tag the squashed commit and push tags to GitHub.
- Travis will build and deploy the tagged commit and upload to PyPI.
- Travis will prepare a GitHub release draft for the tag.
- Once you're satisfied with the release content (ie changelog entry info)
  you can publish the release.

Configuration Options
---------------------

- If your deployment uses universal wheels you can consolidate the
  two PyPI deployments into one and build both within ``_travis/deploy.sh``.
- If you're not a fan of GitHub releases you can remove that section
  within ``deploy:`` in ``.travis.yml``.
