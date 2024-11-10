from fastapi import APIRouter, HTTPException

from ..config import Config, read_config, write_config

router = APIRouter()


@router.get("/config")
def get_config():
    return Config.get().to_dict()


@router.post("/config/{config_item}")
def update_config(config_item: str, value: str):
    config = read_config()
    if config_item not in config:
        raise HTTPException(status_code=404, detail="Config item not found")

    config[config_item] = value
    write_config(config)

    return {"message": f"{config_item} updated to {value} successfully"}
