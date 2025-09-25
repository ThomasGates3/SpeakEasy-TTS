import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")
    
    cors_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST,OPTIONS',
        'Content-Type': 'application/json'
    }

    # Handle OPTIONS request
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': ''
        }
        
    try:
        print("Processing POST request...")
        
        # Check if body exists
        if not event.get('body'):
            print("No body in event")
            return {
                'statusCode': 400,
                'headers': cors_headers,
                'body': json.dumps({'message': 'No body provided'})
            }
        
        # Get text from the request body
        body = json.loads(event['body'])
        print(f"Parsed body: {body}")
        
        text_to_synthesize = body.get('text', '')
        print(f"Text to synthesize: {text_to_synthesize}")

        if not text_to_synthesize:
            return {
                'statusCode': 400,
                'headers': cors_headers,
                'body': json.dumps({'message': 'No text provided'})
            }

        # Check environment variable
        bucket_name = os.environ.get('S3_BUCKET_NAME')
        print(f"S3 bucket name: {bucket_name}")
        
        if not bucket_name:
            return {
                'statusCode': 500,
                'headers': cors_headers,
                'body': json.dumps({'message': 'S3_BUCKET_NAME environment variable not set'})
            }

        print("Initializing Polly client...")
        polly_client = boto3.client('polly')

        print("Synthesizing speech...")
        response = polly_client.synthesize_speech(
            OutputFormat='mp3',
            Text=text_to_synthesize,
            VoiceId='Joey'
        )

        print("Reading audio stream...")
        audio_stream = response['AudioStream'].read()

        print("Initializing S3 client...")
        s3_client = boto3.client('s3')
            
        file_name = f"audio-{uuid.uuid4()}.mp3"
        print(f"Uploading to S3: {file_name}")
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        print(f"Generated URL: {s3_url}")

        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({
                'message': 'Speech synthesized successfully',
                'audioUrl': s3_url
            })
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'message': f'An error occurred: {str(e)}'})
        }