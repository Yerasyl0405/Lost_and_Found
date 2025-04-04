from minio_storage.storage import MinioMediaStorage

class MediaStorage(MinioMediaStorage):
    bucket_name = 'media'