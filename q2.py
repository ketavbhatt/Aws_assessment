import boto3

# Input for bucket name and file name
bucket = input("Enter Bucket Name : ")
file = input("Enter the object name whose version is to be found : ")

# boto3 library to get s3 object 
s3 = boto3.resource('s3')

# Getting all versions of the file
versions = s3.Bucket(bucket).object_versions.filter(Prefix=file)

# List of all the versions
temp = []

# Getting second last version
for version in versions:
	temp.append(version.get().get('VersionId'))

# Downloading second last version of the specified file
try:
    s3.Bucket(bucket).download_file(file, 'copy.txt', ExtraArgs={'VersionId': temp[1]})

# In case of an error
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("Object not found")
    else:
        raise