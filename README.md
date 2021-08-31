# mkdocs-multisite

Combine two folders of docs into a single site.

This plugin was written to support internationalization (i18n) and localization (l10n) on large mkdocs sites. It allows a translation to fall-back to the primary language of a site for documents that have not yet been translated.

## Setup

Install the plugin using pip:

`pip install mkdocs-multisite`

## Typical Use

We have our documentation structured like so:

* `/`
    * `en` - English language
        * `docs` - English language documents
        * `mkdocs.yml` - English site configuration
    * `fr` - French language
        * `docs` - French language documents
        * `mkdocs.yml` - French site configuration

Inside of `fr/mkdocs.yml` we configure our plugin like this:

```yaml
plugins:
  - multisite:
      fallback_dir: "../en/docs"
```

When our site is built the end result will be the same as if we had copied `en/docs/**` into `fr/docs` without overwriting any existing files.

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
