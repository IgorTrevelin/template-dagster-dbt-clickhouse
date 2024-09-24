from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource

from .dbt import dbt_project_assets, dbt_project
from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[dbt_project_assets, *all_assets],
    resources={"dbt": DbtCliResource(project_dir=dbt_project.project_dir)},
)
