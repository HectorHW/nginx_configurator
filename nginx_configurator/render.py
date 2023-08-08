import jinja2
from nginx_configurator import config_types

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath="templates")
)

proxy_template = template_env.get_template("reverse_proxy.vhost.jinja2")
redirect_template = template_env.get_template("redirect.vhost.jinja2")


def render_configurations(config: config_types.WholeConfig) -> dict[str, str]:
    return {
        service.external_name: render_service(
            global_config=config.global_, service=service
        )
        for service in config.services
    }


def render_service(
    global_config: config_types.Global, service: config_types.AnyService
) -> str:
    match service:
        case config_types.Service():
            template = proxy_template
        case config_types.RedirectService():
            template = redirect_template
        case _:
            raise NotImplementedError(service)

    return template.render(**{"global": global_config, "service": service})
