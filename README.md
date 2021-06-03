# poc-github-ci

This GitHub repository is intended to provide a small example config.
for both (GitHub Actions, GitLab CI), and to demonstrate the kind of
feedback we can get in the context of GitHub's Pull Requests.

Note that the GitLab CI workflow specifically relies on:

* a [GitLab CI mirror](https://gitlab.com/erikmd/poc-github-ci),
  created using the feature [GitLab CI/CD for external repositories](
  https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/github_integration.html#connect-with-personal-access-token),
* as well as [**@coqbot**](https://github.com/apps/coqbot-app),
  installed [as a GitHub app](
  https://github.com/coq/bot/#as-a-github-app).
