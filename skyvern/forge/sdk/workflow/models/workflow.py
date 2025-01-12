from datetime import datetime
from enum import StrEnum
from typing import Any, List

from pydantic import BaseModel

from skyvern.forge.sdk.schemas.tasks import ProxyLocation
from skyvern.forge.sdk.workflow.models.block import BlockTypeVar


class WorkflowRequestBody(BaseModel):
    data: dict[str, Any] | None = None
    proxy_location: ProxyLocation | None = None
    webhook_callback_url: str | None = None


class RunWorkflowResponse(BaseModel):
    workflow_id: str
    workflow_run_id: str


class WorkflowDefinition(BaseModel):
    blocks: List[BlockTypeVar]


class Workflow(BaseModel):
    workflow_id: str
    organization_id: str
    title: str
    description: str | None = None
    workflow_definition: WorkflowDefinition

    created_at: datetime
    modified_at: datetime
    deleted_at: datetime | None = None


class WorkflowRunStatus(StrEnum):
    created = "created"
    running = "running"
    failed = "failed"
    terminated = "terminated"
    completed = "completed"


class WorkflowRun(BaseModel):
    workflow_run_id: str
    workflow_id: str
    status: WorkflowRunStatus
    proxy_location: ProxyLocation | None = None
    webhook_callback_url: str | None = None

    created_at: datetime
    modified_at: datetime


class WorkflowRunParameter(BaseModel):
    workflow_run_id: str
    workflow_parameter_id: str
    value: bool | int | float | str | dict | list
    created_at: datetime


class WorkflowRunStatusResponse(BaseModel):
    workflow_id: str
    workflow_run_id: str
    status: WorkflowRunStatus
    proxy_location: ProxyLocation | None = None
    webhook_callback_url: str | None = None
    created_at: datetime
    modified_at: datetime
    parameters: dict[str, Any]
    screenshot_urls: list[str] | None = None
    recording_url: str | None = None
