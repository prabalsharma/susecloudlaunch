AZURE_AUTH_LOCATION = "/mercury/data/public-cloud/keys/azure/credentials.json"

AWS_INSTANCE_TYPES = [
    't3.micro',
    't3.small',
    'm4.large']

AZURE_INSTANCE_TYPES = [
    'B1s',
    'B1ms',
    'B2ms']

PROVIDERS = [
    'aws',
    'azure',
    'gcp']

SLES_VERSIONS = [
    'sles-12-sp1',
    'sles-12-sp2',
    'sles-12-sp3',
    'sles-12-sp4',
    'sles-12-sp5',
    'sles-15',
    'sles-15-sp1'
]

SLES_SAP_VERSIONS = [
    'sles-sap-12-sp1',
    'sles-sap-12-sp2',
    'sles-sap-12-sp3',
    'sles-sap-12-sp4',
    'sles-sap-12-sp5',
    'sles-sap-15',
    'sles-sap-15-sp1'
]

OS_TYPES = [
    'sles',
    'sles for sap'
]

TF_TEMPLATE_LOCATION = "tf_templates"
TF_APPLY_LOCATION = "tf_apply"
