import logging
import os
import sys
from glob import glob
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File

log = logging.getLogger(__name__)


def _sort_files(filenames):
    """ Always sort `index` or `README` as first filename in list. """

    def key(f):
        if os.path.splitext(f)[0].lower() in ['index', 'readme']:
            return (0,)
        return (1, f)

    return sorted(filenames, key=key)


class MultiSite(BasePlugin):
    config_scheme = (
        ('fallback_dir', config_options.Type(str, default=None)),
    )

    def __init__(self, **kwargs):
        self.enabled = True
        self.total_time = 0

    def on_serve(self, server, config, builder, **kwargs):
        """Add the fallback_dir to the list of watched directories.
        """
        server.watch(self.config['fallback_dir'])

        return server

    def on_files(self, files, config, **kwargs):
        """Walk the fallback_dir and add missing files to the collection.
        """
        fallback_dirname = os.path.relpath(self.config['fallback_dir'], config['docs_dir'])

        for source_dir, dirnames, filenames in os.walk(self.config['fallback_dir'], followlinks=True):
            relative_source = os.path.relpath(source_dir, self.config['fallback_dir'])
            relative_dir = os.path.relpath(source_dir, config['docs_dir'])

            for filename in _sort_files(filenames):
                if filename.startswith('.') or filename.endswith('.template'):
                    continue

                if filename.lower() == 'readme.md' and 'index.md' in filenames:
                    log.warning(f"Both index.md and readme.md found. Skipping readme.md from {source_dir}")
                    continue

                if os.path.normpath(os.path.join(relative_source, filename)) in files:
                    continue

                file = File(
                    os.path.normpath(os.path.join(relative_dir, filename)),
                    config['docs_dir'],
                    config['site_dir'],
                    config['use_directory_urls'],
                )

                url = file.dest_path.replace(os.path.sep, '/')

                if url.startswith(fallback_dirname):
                    url = url[len(fallback_dirname)+1:]

                file.url = url
                file.abs_dest_path = os.path.join(config['site_dir'], file.url)  # Fix the incorrectly detected absolute path
                print('hrm', file.src_path)

                files.append(file)

        return files
