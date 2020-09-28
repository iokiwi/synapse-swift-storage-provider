[WIP] Synapse Swift Storage Provider
===========================

.. warning::

  This storage provider is a work in progress and should not be used in
  production at this stage


This module can be used by synapse as a storage provider, allowing it to fetch
and store media in Openstack swift.


Usage
-----

The `swift_storage_provider.py` should be on the PYTHONPATH when starting
synapse.

Example of entry in synapse config:

```yaml
media_storage_providers:
- module: swift_storage_provider.SwiftStorageProviderBackend
  store_local: True
  store_remote: True
  store_synchronous: True
  config:
    # The cloud name to use from clouds.yml
    cloud: <OPENSTACK_CLOUD_NAME>
    # The openstack swift object containe to use. Analagous with an S3 Bucket
    container: <OPENSTACK_SWIFT_CONTAINER_NAME>
    # All of the below options are optional, for use with non-AWS S3-like
    # services, or to specify access tokens here instead of some external method.
    region_name: <OPENSTACK_REGION_NAME>
    # The maximum number of concurrent threads which will be used to connect
    # to swift. Each thread manages a single connection. Default is 40.
    #
    #threadpool_size: 20
```

This module uses `openstacksdk`, and so the credentials should be specified as
described [here](https://docs.openstack.org/openstacksdk/latest/user/guides/connect_from_config.html).

Regular cleanup job
-------------------

There is additionally a script at `scripts/swift_media_upload` which can be used
in a regular job to upload content to swift, then delete that from local disk.
This script can be used in combination with configuration for the storage
provider to pull media from swift, but upload it asynchronously.

Once the package is installed, the script should be run somewhat like the
following. We suggest using `tmux` or `screen` as these can take a long time
on larger servers.

`database.yaml` should contain the keys that would be passed to psycopg2 to
connect to your database. They can be found in the contents of the
`database`.`args` parameter in your homeserver.yaml.

More options are available in the command help.

```
> cd swift_media_upload
# cache.db will be created if absent. database.yaml is required to
# contain PG credentials
> ls
cache.db database.yaml
# Update cache from /path/to/media/store looking for files not used
# within 2 months
> swift_media_upload update /path/to/media/store 2m
Syncing files that haven't been accessed since: 2018-10-18 11:06:21.520602
Synced 0 new rows
100%|█████████████████████████████████████████████████████████████| 1074/1074 [00:33<00:00, 25.97files/s]
Updated 0 as deleted

> swift_media_upload upload /path/to/media/store matrix_swift_container_name --delete
# prepare to wait a long time
```
