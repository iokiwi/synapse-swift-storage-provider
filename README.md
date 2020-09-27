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
    container: <OPENSTACK_SWIFT_CONTAINER_NAME>
    # All of the below options are optional, for use with non-AWS S3-like
    # services, or to specify access tokens here instead of some external method.
    os_region_name: <OPENSTACK_REGION_NAME>
    os_auth_url: <OPENSTACK_SWIFT_ENDPOINT_URL>
    os_project_id: <OPENSTACK_PROJECT_ID>

    # Note: Never use your own username and password. Create a standalone
    # user with minimal permissions to act as a service account.
    os_username: <OPENSTACK_USERNAME>
    os_password: <OPENSTACK_PASSWORD>

    # The object storage class used when uploading files to the bucket.
    # Default is STANDARD.
    #storage_class: "STANDARD_IA"

    # The maximum number of concurrent threads which will be used to connect
    # to S3. Each thread manages a single connection. Default is 40.
    #
    #threadpool_size: 20
```

This module uses `boto3`, and so the credentials should be specified as
described [here](https://boto3.readthedocs.io/en/latest/guide/configuration.html#guide-configuration).

Regular cleanup job
-------------------

There is additionally a script at `scripts/s3_media_upload` which can be used
in a regular job to upload content to s3, then delete that from local disk.
This script can be used in combination with configuration for the storage
provider to pull media from s3, but upload it asynchronously.

Once the package is installed, the script should be run somewhat like the
following. We suggest using `tmux` or `screen` as these can take a long time
on larger servers.

`database.yaml` should contain the keys that would be passed to psycopg2 to
connect to your database. They can be found in the contents of the
`database`.`args` parameter in your homeserver.yaml.

More options are available in the command help.

```
> cd s3_media_upload
# cache.db will be created if absent. database.yaml is required to
# contain PG credentials
> ls
cache.db database.yaml
# Update cache from /path/to/media/store looking for files not used
# within 2 months
> s3_media_upload update /path/to/media/store 2m
Syncing files that haven't been accessed since: 2018-10-18 11:06:21.520602
Synced 0 new rows
100%|█████████████████████████████████████████████████████████████| 1074/1074 [00:33<00:00, 25.97files/s]
Updated 0 as deleted

> s3_media_upload upload /path/to/media/store matrix_s3_bucket_name --storage-class STANDARD_IA --delete
# prepare to wait a long time
```