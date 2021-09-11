import boto3 , requests

def lambda_handler(event, context):

    res = requests.get('http://s-proj.com/utils/checkHoliday.php?kind=h') #祝日かどうかをAPIで判定
    today = res.text #レスポンスボディをテキスト形式で取得

    region = event['Region']
    instances = event['Instances']

    ec2 = boto3.client('ec2', region_name=region)

    if today != 'holiday':
        if event['Action'] == 'start':
            ec2.start_instances(InstanceIds=instances)
            print ('started your instances: ' + ", ".join(instances))
        elif event['Action'] == 'stop':
            ec2.stop_instances(InstanceIds=instances)
            print ('stopped your instances: ' + ", ".join(instances))
        else :
            print ('not found event')
    else:
        print("it's a holiday today.")