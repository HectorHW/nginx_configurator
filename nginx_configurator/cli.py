import typer
from nginx_configurator.config_types import parse_yaml
from nginx_configurator.render import render_configurations
import os
import glob

app = typer.Typer()


def clear_output_directory(path: str):
    files = glob.glob(os.path.join(path, "*"))
    for f in files:
        os.remove(f)


@app.callback(invoke_without_command=True)
def generate_config_file(
    config_path: str,
    output_directory: str = "output",
):
    with open(config_path) as f:
        config_content = parse_yaml(f.read())

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    clear_output_directory(output_directory)

    for filename, content in render_configurations(config_content).items():
        result_path = os.path.join(output_directory, f"{filename}.vhost")
        with open(result_path, "w") as f:
            f.write(content)


if __name__ == "__main__":
    app()
