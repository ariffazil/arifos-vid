"""Artifact model for the VID pipeline.

This module defines Pydantic models for artifact data structures.
"""

from pydantic import BaseModel


class ArtifactModel(BaseModel):
    """Model representing a governed artifact.

    Attributes:
        id: Unique identifier for the artifact.
        name: Name of the artifact.
        content: Content of the artifact.
    """

    id: str | None = None
    name: str | None = None
    content: str | None = None


class ArtifactMetadata(BaseModel):
    """Model representing artifact metadata.

    Attributes:
        version: Version of the artifact.
        created_at: Creation timestamp.
        tags: List of tags associated with the artifact.
    """

    version: str | None = None
    created_at: str | None = None
    tags: list[str] | None = None
