terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Define variables
variable "instance_type" {
  default = "t2.micro"
}
variable "ami" {
  default = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS AMI ID in us-east-1
}

# Create AWS instance-1
resource "aws_instance" "tf-instance-1" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"
  key_name      = file("~/.ssh/id_rsa.pub")

  tags = {
    Name = "test"
  }
}
# Create AWS instance-2
resource "aws_instance" "tf-instance-2" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"
  key_name      = aws_key_pair.ssh_key.key_name # Replace with your key pair name for SSH access

  tags = {
    Name = "test"
  }
}

# Create AWS instance-3
resource "aws_instance" "tf-instance-3" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"
  key_name      = aws_key_pair.ssh_key.key_name  # Replace with your key pair name for SSH access

  tags = {
    Name = "test"
  }
}

