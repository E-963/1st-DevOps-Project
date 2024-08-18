resource "aws_instance" "demo" {
  ami                    = var.ami
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.allow_http_ssh.name]

  tags = {
    Name = "demo"
  }
}

resource "aws_instance" "test" {
  ami                    = var.ami
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.allow_http_ssh.name]

  tags = {
    Name = "test"
  }
}

resource "aws_instance" "inst" {
  ami                    = var.ami
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.allow_http_ssh.name]

  tags = {
    Name = "inst"
  }
}
