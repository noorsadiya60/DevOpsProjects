terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-south-1"
  access_key = var.access_key
  secret_key = var.secret_key
}

#create S3 bucket
resource "aws_s3_bucket" "noor" {
  bucket = "noor-1234" # Bucket names must be globally unique
  acl    = "private" 
  tags = {
    Name       = var.num
    Environment = "Dev"
  }       
}
