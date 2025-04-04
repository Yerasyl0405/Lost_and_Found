from minio import Minio
import socket

def ensure_media_bucket():
    try:
        client = Minio(
            "minio:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )
        if not client.bucket_exists("media"):
            client.make_bucket("media")
    except socket.gaierror:
        print("⚠️ Could not resolve 'minio' — skipping bucket creation.")
