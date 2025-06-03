# Create our bucket
```sh
aws s3 mb s3://prefixes-fun-ab-52387
```

# Create our folder
```sh
aws s3api put-object --bucket prefixes-fun-ab-52387 --key="hello/"
```

```
# prefixes can have up to 1024 bytes
```