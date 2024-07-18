# Output the IDs of the created instances
output "instance_ids" {
  description = "The ID of EC2 instance"
  value       = aws_instance.tf-instance-1.id
}

# Output the public IP addresses of the created instances
output "instance_public_ips" {
  description = "The ID of EC2 instance"
  value       = aws_instance.tf-instance-2.public_ip
}

# Output the private IP addresses of the created instances
output "instance_private_ips" {
  description = "The ID of EC2 instance"
  value       = aws_instance.tf-instance-3.public_ip
}

