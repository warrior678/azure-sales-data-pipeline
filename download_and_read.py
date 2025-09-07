import os
import pandas as pd
import matplotlib.pyplot as plt
from azure.storage.blob import BlobServiceClient


conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "projectdata123"
blob_name = "sales data.csv"
download_file = "sales_data_local.csv"

try:
    client = BlobServiceClient.from_connection_string(conn)
    blob_client = client.get_blob_client(container=container_name, blob=blob_name)

    with open(download_file, "wb") as f:
        f.write(blob_client.download_blob().readall())
    print(f" Downloaded '{blob_name}' to '{download_file}'")

    
    df = pd.read_csv(download_file)
    print(" Preview of data:")
    print(df.head())

    
    df.iloc[:,1].plot(kind="bar", title="Sample Chart")
    plt.show()

except Exception as e:
    print(" Error:", e)
