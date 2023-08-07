# Nginx Configurator

Nginx configuration genrator powered by jinja.

## Installation & Running

Poetry is used for dependency management. In order to install all requirements, issue `poetry install --only main`.

Use poetry to run the tool: `poetry run nginx_configurator <path to config>`.

## Configuration

generator is configured by supplying yaml file with following structure (**bold** indicates that field should be supplied):

### global

* **hostname** - base hostname shared by all services. Service with external_name set to service with hostname set to my.host will be available under service.my.host
* port_number (default 8080) - port number used by nginx
* ssl (not configured by default) - configuration for ssl. If set, expects path to certificate (as `ssl.certificate_path`) and key (as `ssl.key_path`)

Example global configuration:

```yaml
global:
  hostname: example.com
```

## services

This section describes each service that will be proxied. Services form a list, each service is described using following fields:

* **external_name** - added to hostname to form a service path (see global.hostname).
* **proxied** - describes where to route traffic internally. Nginx will be configured to proxy requests to `{proto}://{hostname}:{port}`
  * **port** - port to access the service
  * hostname (defaults to `localhost`)
  * proto (defaults to `http`)
* websocket_path (defaults to None) - if set, will add additional entry for websocket proxying (`Connection: Upgrade` and so on)

Example services configuration:

```yaml
services:
  - external_name: grafana
    proxied:
      port: 3000
    websocket_path: /api/live/
```
