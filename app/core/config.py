import os
import ee
import json

# Load credentials from environment variable
service_account_info = json.loads(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
credentials = ee.ServiceAccountCredentials('', service_account_info)
ee.Initialize(credentials)
