
import os
import pandas as pd
from azure.storage.blob import BlobServiceClient


CONTAINER_NAME = "projectdata123"
BLOB_NAME = "sales data.csv"
DOWNLOAD_FILE = "sales_data_local.csv"

def main():
    conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not conn:
        raise SystemExit("ERROR: set AZURE_STORAGE_CONNECTION_STRING in terminal and re-run.")

    try:
        
        client = BlobServiceClient.from_connection_string(conn)
        blob_client = client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        with open(DOWNLOAD_FILE, "wb") as f:
            f.write(blob_client.download_blob().readall())
        print(f" Downloaded '{BLOB_NAME}' to '{DOWNLOAD_FILE}'")
        df = pd.read_csv(DOWNLOAD_FILE, dtype=str)  
        print("\n Preview of data (first 10 rows):")
        print(df.head(10))

    except Exception as e:
        print(" Error:", e)

if __name__ == "__main__":
    main()





