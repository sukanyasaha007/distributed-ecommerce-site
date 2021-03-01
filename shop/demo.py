import cloudstorage as gcs

if __name__ == '__main__':
    storage_client = storage.Client.from_service_account_json('../onlineshopping-305417-6700bb4d6a86.json')
    bucket = storage_client.bucket("personal-nmk")
    blobs = list(bucket.list_blobs(prefix='data/'))