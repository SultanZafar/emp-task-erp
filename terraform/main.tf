terraform {
    required_providers {
        docker = {
            source = "kreuzwerker/docker"
            version = "~> 3.0"
            }
          }
        }

provider "docker" {}

resource "docker_image" "odoo" {
    name       = "odoo-erp:latest"
    keep_locally = true
   }

resource "docker_container" "odoo" {
    name = "odoo-erp-container"
    image = docker_image.odoo.image_id

    restart = "no"
    must_run = false

    ports {
        internal = 8069
        external = 8069
        }
    }
