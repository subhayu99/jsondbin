from dataclasses import dataclass


@dataclass
class CollectionCreated:
    record: str
    metadata: dict
    
    @property
    def id(self) -> str:
        return self.record
    
    @property
    def name(self) -> str:
        return self.metadata.get("name")
    
    @property
    def created_at(self) -> str | None:
        return self.metadata.get("createdAt")


@dataclass
class Collection:
    record: str
    collectionMeta: dict
    createdAt: str | None = None
    
    @property
    def id(self) -> str:
        return self.record
    
    @property
    def name(self) -> str:
        return self.collectionMeta.get("name")
    
    @classmethod
    def from_created(cls, created: CollectionCreated):
        return cls(
            record=created.record, 
            collectionMeta={"name": created.name}, 
            createdAt=created.created_at
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.createdAt
        }
        
@dataclass
class CollectionSchema:
    collectionName: str
    schemaDocId: str
    metadata: dict
    
    @property
    def id(self) -> str:
        return self.metadata.get("id")
    
    @property
    def created_at(self) -> str | None:
        return self.metadata.get("createdAt")
    