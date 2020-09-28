from setuptools import setup

__version__ = "1.0"

setup(
    name="synapse-swift-storage-provider",
    version=__version__,
    zip_safe=False,
    url="https://github.com/iokiwi/synapse-swift-storage-provider",
    py_modules=["swift_storage_provider"],
    scripts=["scripts/swift_media_upload"],
    install_requires=[
        "openstacksdk",
        "humanize",
        "psycopg2",
        "PyYAML",
        "tqdm",
    ],
)
