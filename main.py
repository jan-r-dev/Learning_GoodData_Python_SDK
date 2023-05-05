from gooddata_sdk import GoodDataSdk, GoodDataApiClient
from dotenv import load_dotenv
from os import getenv

load_dotenv('./.env', verbose=True)

GDC_TOKEN = getenv('GDC_TOKEN')
GDC_HOSTNAME = getenv('GDC_HOSTNAME')

if GDC_TOKEN is None or GDC_HOSTNAME is None:
    raise (ValueError(
        f"Failed to import vital env variables.\n\nGDC_TOKEN is: {GDC_TOKEN}\nGDC_HOSTNAME is: {GDC_HOSTNAME}\n\nExiting..."))

client = GoodDataApiClient(token=GDC_TOKEN, host=GDC_HOSTNAME)
sdk = GoodDataSdk(client)

workspaces = sdk.catalog_workspace.list_workspaces()

for workspace in workspaces:
    print(workspace.name)