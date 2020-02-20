## Amazon Translate with Amazon Comprehend Medical 

This project contains sample code for using Amazon Translate in conjunction with Amazon Comprehend Medical to analyze
medical notes in multiple languages.  This repository contains the AWS Lambda function code for using these two services
together, an AWS CloudFormation custom resource for creating an Athena table to evaluate the results, and the AWS CloudFormation
template to deploy it all.  Use the steps below to deploy this code:

* Download the contents of this repository
* Run the makeZip.sh script in the root directory to create the zip packages for Lambda function deployment
    - NOTE: This is a bash script so ensure that you have the proper environment and permissions to run it
* For deployment instructions, review the blog post at *insert blog post location when posted* 

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

