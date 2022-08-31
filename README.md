`s3cache` is a utility package for easily downloading files from Amazon's S3 cloud
storage platform.

# Usage

The package provides a single class, `S3Cache` that takes in the bucket name, object
prefix, and storage location, e.g.,

```python
from s3cache import S3Cache

cache = S3Cache("my_bucket", "my_prefix", "/path/to/storage/location")
cache.sync()
```

Every object in `"my_bucket"` with the prefix `"my_prefix"` will be downloaded and
saved to `"/path/to/storage/location"`.

If no storage path is given, the default behavior is to save the files in a
temporary directory.

Additionally, the class can be used as a context manager, e.g.,

```python
from s3cache import S3Cache

with S3Cache("my_bucket", "my_prefix", "my_loc") as cache:
    cache.sync()
    # Do stuff with the files
```

After the `with` block exits, the cache directory is automatically deleted.
