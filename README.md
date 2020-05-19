## Amazon Translate with Amazon Comprehend Medical 

This project contains sample code for using Amazon Translate in conjunction with Amazon Comprehend Medical to analyze
medical notes in multiple languages.  This repository contains the AWS Lambda function code for using these two services
together, an AWS CloudFormation custom resource for creating an Amazon Athena table to evaluate the results, and the AWS CloudFormation
template to deploy it all.  Use the steps below to deploy this code:

* Download the contents of this repository
* Run the makeZip.sh script in the root directory to create the zip packages for Lambda function deployment
    - NOTE: This is a bash script so ensure that you have the proper environment and permissions to run it
* For deployment instructions, review the blog post at https://aws.amazon.com/blogs/industries/how-to-process-medical-text-in-multiple-languages-using-amazon-translate-and-amazon-comprehend-medical/

## Running the solution

The output section of the CloudFormation stack will provide you the URL for this solution.  There are three query string parameters supported:

* bucket: provide the name of the bucket containing clinical notes.  Only the root "folder" will have notes processed
* prefix: when adding prefix along with bucket, that specific "sub-folder" will have its notes processed
* recursive (no value required): when used in conjunction with bucket or bucket and prefix, it will process all notes recursively from the specified starting location

NOTE: This solution will make a high volume of calls to Amazon Translate.  Please check your Amazon Translate and request an increase to API limits if necessary.  Also,
this solution is a sample, and intended to run on a small number of notes.  If a large quantity of notes is translated, the 30 sec timeout of API Gateway may be hit.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

