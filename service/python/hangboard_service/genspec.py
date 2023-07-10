"""Generate the Open API spec from the registry

Run using
hangboard$ python -m service.python.hangboard_service.genspec > api.yml
"""
import yaml

from service.python.hangboard_service.hangboard_service import registry


if __name__ == "__main__":
    spec = registry.swagger_generator.generate(registry, sort_keys=False)
    print(yaml.safe_dump(spec))
