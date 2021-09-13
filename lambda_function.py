import boto3 , requests

def lambda_handler(event, context):

    res = requests.get('http://s-proj.com/utils/checkHoliday.php?kind=h') #祝日かどうかをAPIで判定
    today = res.text #レスポンスボディをテキスト形式で取得

    region = event['Region']
    instances = event['Instances']

    rds = boto3.client('rds', region_name=region)

    if today != 'holiday':
        if event['Action'] == 'start':
            rds.start_db_instance(DBInstanceIdentifier=instances)
            print ('started your DBinstances: ' + ", ".join(instances))
        elif event['Action'] == 'stop':
            rds.stop_db_instance(DBInstanceIdentifier=instances)
            print ('stopped your DBinstances: ' + ", ".join(instances))
        else :
            print ('not found event')
    else:
        print("it's a holiday today.")