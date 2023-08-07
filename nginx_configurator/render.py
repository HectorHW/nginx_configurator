import jinja2
from nginx_configurator import config_types

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath="templates")
)

config_template = template_env.get_template("reverse_proxy.vhost.jinja2")


def render_configurations(config: config_types.WholeConfig) -> dict[str, str]:
    return {
        service.external_name: render_service(
            global_config=config.global_, service=service
        )
        for service in config.services
    }


def render_service(
    global_config: config_types.Global, service: config_types.Service
) -> str:
    return config_template.render(**{"global": global_config, "service": service})
