from dataclasses import dataclass


@dataclass
class Error:
    message: str
    code: int

    def __str__(self) -> str:
        return f"{self.message} ({self.code})"
    
    def __repr__(self) -> str:
        return str(self)