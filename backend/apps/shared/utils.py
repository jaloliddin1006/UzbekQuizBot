from enum import Enum


class UserStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'
    
    def __str__(self):
        return self.value
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def get(cls, value):
        return cls[value]
    
class Language(Enum):
    UZBEK = 'uz'
    ENGLISH = 'en'
    RUSSIAN = 'ru'
    
    def __str__(self):
        return self.value
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def get(cls, value):
        return cls[value]