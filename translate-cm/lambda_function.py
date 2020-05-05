# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import os
import time

# Set up boto clients and environment variables
s3 = boto3.client('s3')
translate = boto3.client('translate')
comprehendmedical  = boto3.client(service_name='comprehendmedical')
outputBucket = os.environ['RESULTS_BUCKET']

def lambda_handler(event, context):
	bucket=event['queryStringParameters']['bucket']
	prefix = ""
	if "prefix" in event['queryStringParameters']:
		prefix = event['queryStringParameters']['prefix']
                if not prefix.endswith("/"):
                    prefix = prefix + "/"
	outputObj = 'results/cm_results_'+time.strftime("%Y%m%d-%H%M%S")+'.csv'
	content = "File,Text,Category,Type,Score\n"
	if "recursive" in event['queryStringParameters']:
            list=s3.list_objects(Bucket=bucket,Prefix=prefix)
        else:
            list=s3.list_objects(Bucket=bucket,Prefix=prefix,Delimiter="/")
	if "Contents" in list.keys():
		fileList = list['Contents']
		for s3_key in fileList:
			s3_object = str(s3_key['Key'])
			if not s3_object.endswith("/"):
				print('processing file : ' + s3_object)
				data = s3.get_object(Bucket=bucket, Key=s3_object)
				textToTranslate = data['Body'].read()
				english = translate.translate_text(Text=textToTranslate, SourceLanguageCode="auto", TargetLanguageCode="en")
				sourceLang = str(english['SourceLanguageCode'])
				entities = comprehendmedical.detect_entities(Text = str(english['TranslatedText']) )
				entity_str=entities['Entities']
				
				print('****************Following text was translated***************************')
				for row in entity_str:
					translated_text = translate.translate_text(Text=row['Text'] , SourceLanguageCode="en", TargetLanguageCode=sourceLang)
					print ('en: '+row['Text']+', '+sourceLang+': '+translated_text['TranslatedText'])
					text_to_write = translated_text['TranslatedText'].encode('utf8', 'replace')
					row['Text']=text_to_write
					line = s3_object+','+row['Text']+','+row['Category']+','+row['Type']+','+str(row['Score'])+'\n'
					content = content + line
					
		s3.put_object(Bucket=outputBucket, Key=outputObj, Body=content)
		preURL = s3.generate_presigned_url('get_object', Params = {'Bucket': outputBucket, 'Key': outputObj}, ExpiresIn = 300)
		textResponse = "Translation Complete. \n\nAccess translated file at: \n"+preURL
		results = {"statusCode": 200, "body": textResponse}
		return(results)
		
	else: 
		answer = "No objects present in bucket: "+bucket
		results = {"statusCode": 200, "body": answer}
		return(results)
