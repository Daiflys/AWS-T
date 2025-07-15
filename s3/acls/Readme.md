## Create a new bucket

```sh
aws s3api create-bucket --bucket acl-example-ab-123507251 --region ap-southeast-2 --create-bucket-configuration LocationConstraint=ap-southeast-2
```


## Turn off Block Public Access for ACLs

```sh
aws s3api put-public-access-block \
--bucket acl-example-ab-123507251 \
--public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

```sh
aws s3api get-public-access-block --bucket acl-example-ab-123507251
```

## Change Bucket Ownership
```sh
aws s3api put-bucket-ownership-controls \
    --bucket acl-example-ab-123507251 \
    --ownership-controls="Rules=[{ObjectOwhership=BucketOwnerPreferred}]"
```

