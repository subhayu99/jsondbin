from dataclasses import dataclass


@dataclass
class Document:
    record: dict | list | str | int | float | bool | None
    metadata: dict
    
    @property
    def id(self) -> str:
        return self.metadata.get("id")
    
    @property
    def created_at(self) -> str:
        return self.metadata.get("createdAt")
    
    @property
    def private(self) -> bool:
        return self.metadata.get("private")
    
    @property
    def parent_id(self) -> str | None:
        return self.metadata.get("parentId")
    
    def to_dict(self):
        return {
            "id": self.id,
            "data": self.record,
            "created_at": self.created_at,
            "private": self.private,
            "parentId": self.parent_id,
        }
    
@dataclass
class DocumentOfList:
    record: str
    private: bool
    snippetMeta: dict
    createdAt: str

    @property
    def id(self) -> str:
        return self.record
    