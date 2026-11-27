provider "docker" {}

resource "docker_image" "app" {
  name         = var.image
  platform     = "linux/amd64"
  keep_locally = true
}

resource "docker_network" "app" {
  name = "inf345-net"
}

resource "docker_container" "app" {
  name  = "inf345-app"
  image = docker_image.app.image_id

  restart = var.restart_policy
  env     = ["PORT=${var.internal_port}"]

  platform = "linux/amd64"

  lifecycle {
    ignore_changes = [platform]
  }

  ports {
    internal = var.internal_port
    external = var.host_port
  }

  networks_advanced {
    name = docker_network.app.name
  }
}
