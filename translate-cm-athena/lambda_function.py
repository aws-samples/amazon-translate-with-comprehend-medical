# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
import os
import cfnresponse
import logging

query = "CREATE EXTERNAL TABLE `results`(`file` string,`text` string,`category` string,`type` string,`score` decimal(20,12))\
                     ROW FORMAT DELIMITED FIELDS TERMINATED BY ','\
                     STORED AS INPUTFORMAT \'org.apache.hadoop.mapred.TextInputFormat\'\
                     OUTPUTFORMAT \'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat\'\
                     LOCATION \'"+os.environ['RESULTS_BUCKET']+"\'\
                     TBLPROPERTIES (\'has_encrypted_data\'=\'true\',\'skip.header.line.count\'=\'1\')"

def lambda_handler(event, context):
	status = cfnresponse.SUCCESS
	try:
		client = boto3.client('athena')
		config = {'OutputLocation':os.environ['ATHENA_BUCKET'],'EncryptionConfiguration':{'EncryptionOption':'SSE_S3'}}
		client.start_query_execution(
			QueryString = 'CREATE DATABASE translateCM',
			ResultConfiguration = config
		)
		dbcontext = {'Database': 'translateCM'}
		client.start_query_execution(
			QueryString=query,
			QueryExecutionContext=dbcontext,
			ResultConfiguration=config
		)
	except Exception as e:
		logging.error('Exception: %s' % e, exc_info=True)
		status = cfnresponse.FAILED
	finally:
		cfnresponse.send(event, context, status, {}, None)
