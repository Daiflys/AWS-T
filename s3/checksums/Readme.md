### create a new s3 bucket

```md
aws s3 mb s3://checksums-examples-ab-2342555
```

## create a file that will we do a checksum on

```
echo "Hello Mars" > myfile.txt
```

## get a checksum of a file for md5

md5sum myfile.txt

## upload our file

aws s3 cp myfile.txt s3://checksums-examples-ab-2342555
aws s3api head-object --bucket checksums-examples-ab-2342555 --key myfile.txt

## let's upload a file with a different kind of checksum

```sh
sudo apt install rhash -y
rhash --crc32 --simple myfile.txt
```

```sh
aws s3api put-object \
--bucket="checksums-examples-ab-2342555" \
--key="myfile.txt" \
--body="myfile.txt" \
--checksum-algorithm="SHA1" \
--checksum-sha1="c28ccc2c5e214036806014df9fb43634f3e770b2"
```