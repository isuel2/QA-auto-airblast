from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    login: str = None
    password: str = None
    name: str = None
    description: str = None
    email: str = None
    phone: str = None
    telegram: str = None
    core_limit: int = None
    run_job_limit: int = None
    ram_limit: int = None
    total_core_limit: int = None
    total_ram_limit: int = None
