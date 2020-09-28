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
        "openstacksdk>=0.50.0,openstacksdk==0.47.0;python_version='3.5'",
        "humanize>=0.5.1<0.6",
        "psycopg2>=2.7.5<3.0",
        "PyYAML>=3.13<4.0",
        "tqdm>=4.26.0<5.0",
    ],
)
