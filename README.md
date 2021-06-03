# poc-github-ci

[![GHA test][github-action-shield]][github-action-link]
[![GitLab pipeline][gitlab-ci-shield]][gitlab-ci-link]

[github-action-shield]: https://github.com/erikmd/poc-github-ci/workflows/test/badge.svg?branch=master
[github-action-link]: https://github.com/erikmd/poc-github-ci/actions?query=workflow:test "GitHub Action"
[gitlab-ci-shield]: https://gitlab.com/erikmd/poc-github-ci/badges/master/pipeline.svg
[gitlab-ci-link]: https://gitlab.com/erikmd/poc-github-ci/-/pipelines "GitLab CI"

This GitHub repository is intended to provide a small example
configuration for both [GitHub Actions](
https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
and [GitLab CI](https://docs.gitlab.com/ee/ci/yaml/), and to
demonstrate the kind of feedback we can get in the context of GitHub's
Pull Requests.

Note that the GitLab CI workflow specifically relies on:

* a [GitLab CI mirror](https://gitlab.com/erikmd/poc-github-ci),
  created using the feature [GitLab CI/CD for external repositories](
  https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html#connect-with-personal-access-token),
* as well as [**@coqbot**](https://github.com/apps/coqbot-app),
  installed [as a GitHub app](
  https://github.com/coq/bot/#as-a-github-app).
