# Creating a Subtemplate

## Goal

* Allow users to apply a subtemplate after they've used the base template to get access
to new features.
* Make applying one template after the other painless.

## Problem

copier does not support generating a diff when one `copier copy` overwrites an existing
file (see [#1485](https://github.com/orgs/copier-org/discussions/1485),
[#1738](https://github.com/copier-org/copier/issues/1738)).

## Solution

Use jinja's `include` in any files that are in both templates to include the contents of
the base template.

We keep this maintainable by including the base template as a git submodule in `bases/`,
and rely on [Renovate](https://docs.renovatebot.com/) to automatically
update the submodule reference whenever the base changes.

With this approach, a conflicting file in a sub template looks something like:

```jinja
# file: template/pyproject.toml.jinja

# reference the file in base that we would conflict with.
{% include 'bases/python-project-kickstarter/template/pyproject.toml.jinja' %}

# Our addition will end up at the end of the generated file.
[tool.poe.tasks.container-build-local]
cmd = "docker build ."
```

With this setup, users can run the following and get a functional template 
(e.g. for a subtemplate providing a docker image, in repository 
"python-docker"):

```bash
copier copy https://github.com/Bundesdruckerei-GmbH/python-project-kickstarter.git .
copier copy https://github.com/your_username/your_template_extension.git --data-file copier-answers/python-project-kickstarter.yml .
```
, where "your_template_extension" is another copier template designed to placed on top
of this basic template for additional or adjusted features.

The two templates remain independent in the eyes of copier and users have to update both
independently.

## Example

Currently not published.

## Possible Extensions

Currently, we're limited to adding to the end of files. If the base template is modified
to include [jinja
blocks](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance)
then we could add options to the middle as well.
