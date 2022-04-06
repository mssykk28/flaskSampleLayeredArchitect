from src.infrastructure import Base


def entity_to_dict(entity: Base) -> dict:
    dict_ = entity.__dict__
    dict_.pop("_sa_instance_state")
    return {k: v for k, v in dict_.items() if v is not None}
