"""Stateless template processor."""

from typing import List

from pydantic import BaseModel, Field

from stateless_microservice import BaseProcessor, StatelessAction


class RoiRequest(BaseModel):
    """Request payload for ROI service."""

    pid: str = Field(..., description="ROI pid")


class IfcbRoiProcessor(BaseProcessor):
    """Processor for accessing IFCB ROI images and associated technical metadata."""

    def __init__(self, data_dir: str = "/data/ifcb"):
        self.data_dir = data_dir

    @property
    def name(self) -> str:
        return "ifcb_roi"

    def get_stateless_actions(self) -> List[StatelessAction]:
        return [
            StatelessAction(
                name="roi-image",
                path="/roi-image",
                request_model=RoiRequest,
                handler=self.handle_roi_image,
                summary="Get ROI image.",
                description="Get ROI image.",
                tags=("roi",),
                media_type="application/json",
            ),
        ]

    async def handle_roi_image(self, payload: RoiRequest):
        """Get ROI image."""
        from ifcb import DataDirectory, Pid
        from ifcb.data.imageio import format_image
        import base64
        data_dir = DataDirectory(self.data_dir)
        pid = Pid(payload.pid)
        bin_lid = pid.bin_lid
        target_number = int(pid.target)
        b = data_dir[bin_lid]
        with b.as_single(target_number) as single_bin:
            image_array = single_bin.images[target_number]
            image_data = format_image(image_array, "image/png").getvalue()
            encoded_image_data = base64.b64encode(image_data).decode("utf-8")
        return {
            "pid": payload.pid,
            "bin-pid": bin_lid,
            "content-type": "image/png",
            "image": encoded_image_data
        }