from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint
# Configure API key authorization: Apikey
configuration = cloudmersive_convert_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
input_file = '/test/api/16511 Iniciativa empresarial joven II.docx' # file | Input file to perform the operation on.
quality = 56 # int | Optional; Set the JPEG quality level; lowest quality is 1 (highest compression), highest quality (lowest compression) is 100; recommended value is 75. Default value is 75. (optional)
try:
    # Convert Word DOCX Document to JPG/JPEG image array
    api_response = api_instance.convert_document_docx_to_jpg(input_file, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDocumentApi->convert_document_docx_to_jpg: %s\n" % e)