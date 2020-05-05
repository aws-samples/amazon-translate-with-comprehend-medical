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

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

