import boto3
import io
from PIL import Image

rekognition = boto3.client('rekognition', region_name='us-west-1')
dynamodb = boto3.client('dynamodb', region_name='us-west-1')
    
image = Image.open("Swift.jpeg")
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(
        CollectionId='guest_collection',
        Image={'Bytes':image_binary}                                      
        )
    
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(
        TableName='family_collection',  
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print (face['Item']['FullName']['S'])
    else:
        print ('no match found in person lookup')
