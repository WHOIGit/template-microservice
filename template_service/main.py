"""FastAPI entrypoint for a template stateless service."""

from stateless_microservice import ServiceConfig, create_app

from .processor import Processor

config = ServiceConfig(
    description="Template microservice framework.",
)

app = create_app(EchoProcessor(), config)
