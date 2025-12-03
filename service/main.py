import os

from stateless_microservice import ServiceConfig, create_app

from .processor import IfcbRoiProcessor

config = ServiceConfig(
    description="Service for accessing IFCB ROI images and associated technical metadata.",
)

DATA_DIR = os.getenv("DATA_DIR", "/data")

app = create_app(IfcbRoiProcessor(), config)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
