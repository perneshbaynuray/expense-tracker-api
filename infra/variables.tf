variable "image" {
  description = "Docker image used to run my Expense Tracker API."
  type        = string
  default     = "ghcr.io/perneshbaynuray/expense-tracker-api:eb4843130afd6432db6af0fc384171546a8af7f0"
}

variable "internal_port" {
  description = "The port my service listens on inside the container - the contract's PORT"
  type        = number
  default     = 8080
}

variable "host_port" {
  description = "The port on my laptop used to access the service"
  type        = number
  default     = 8080
}

variable "restart_policy" {
  description = "What Docker does when my service exits: no, on-failure, always or unless-stopped"
  type        = string
  default     = "no"
}
