# azure-sales-data-pipeline
Cloud-based sales data pipeline using Azure Blob Storage, Python, and pandas for secure data access and analytics.
#  Azure Sales Data Pipeline (Python + Azure Blob Storage)

This project demonstrates how to build a **cloud-based data pipeline** using **Microsoft Azure** and **Python**.  
It connects to **Azure Blob Storage**, downloads CSV sales data, and processes it locally with **pandas** in VS Code.  
The project showcases **end-to-end Azure setup, cloud integration, and data analytics** skills.

---

##  Project Highlights

- **Azure Cloud Setup**
  - Created a **Resource Group** in Azure Portal
  - Provisioned a **Storage Account** (`cloudstorageproject123`)
  - Configured **Access Keys & Connection Strings**
  - Created a **Blob Container** (`projectdata123`)

- **Data Upload to Azure**
  - Uploaded `sales data.csv` into the Azure Blob Container
  - Used Azure Portal for blob management

- **Python + VS Code Integration**
  - Set up a **virtual environment** (`venv`) in VS Code
  - Installed required packages (`pandas`, `azure-storage-blob`, `matplotlib`)
  - Created `app.py` to connect to Azure and download data

- **Data Access & Processing**
  - Connected securely to Azure using environment variables (no secrets in code)
  - Downloaded `sales data.csv` from blob to local machine
  - Previewed data in pandas without altering its format

- **Data Sample**
```text
         Date      Product   Region   Sales
0  01-01-2025   Product A   North    1200
1  02-01-2025   Product B   South    1500
2  03-01-2025   Product C   East     1700
3  04-01-2025   Product A   West      800
4  05-01-2025   Product B   North     950
Project Structure
azure-sales-data-pipeline/
│-- app.py                # Main script: connect, download & preview CSV
│-- requirements.txt      # Dependencies (pandas, azure-storage-blob, matplotlib)
│-- README.md             # Documentation (this file)
│-- sales_data_local.csv  # Local copy of downloaded CSV (ignored in git)
│-- venv/                 # Virtual environment (not uploaded to GitHub)
<img width="881" height="664" alt="image" src="https://github.com/user-attachments/assets/d2fb82e7-95fe-44a9-9cf3-55deb60a57a5" />




