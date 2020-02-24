import boto3, click

session = boto3.Session(profile_name='default')
s3=session.resource('s3')

@click.group()
def cli():
    "Webotron displays websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for b in s3.buckets.all():
        print(b)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List bucket objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
