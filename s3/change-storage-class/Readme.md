## Create a bucket

aws s3 mb s3://class-fun-ab-6128953

## Create a file

echo "Hello World" > hello.txt
aws s3 cp hello.txt s3://class-fun-ab-6128953

## Cleanup

aws s3 rm s3://class-fun-ab-6128953 --force