## Create a bucket
aws s3 mb s3://bucket-policy-example-ab-15012

##

aws s3api put-bucket-policy --bucket bucket-policy-example-ab-15012 --policy file://policy.json