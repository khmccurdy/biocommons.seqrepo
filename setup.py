from setuptools import setup, find_packages

package_name = "seqrepo"
short_description = "..."
long_description = "..."

setup(
    author = package_name + " Committers",
    description = short_description,
    license = "Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)",
    long_description = long_description,
    name = package_name,
    # namespace_packages = [namespace_package],
    package_data = {
        "seqrepo.fastadir": ["_data/migrations/*"],
        "seqrepo.seqaliasdb": ["_data/migrations/*"],
        },
    packages = find_packages(),
    use_scm_version = True,
    zip_safe = True,

    author_email = "biocommons-dev@googlegroups.com",
    url = "https://github.com/biocommons/" + package_name,

    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        ],

    keywords = [
    ],

    entry_points = {
        "console_scripts": [
            "seqrepo = seqrepo.cli:main",
        ],
    },

    install_requires = [
        "biopython>=1.66",
        "bioutils>=0.1.5",
        "pysam",
        "yoyo-migrations",
    ],

    setup_requires = [
        "pytest-runner",
        "setuptools_scm",
        "sphinx",
        "sphinx_rtd_theme",
        "sphinxcontrib-fulltoc",
        "wheel",
    ],

    tests_require = [
        "pytest",
        "pytest-cov",
    ],
)

## <LICENSE>
## Copyright 2016 Source Code Committers
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## </LICENSE>
