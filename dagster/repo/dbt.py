from pathlib import Path

from dagster import AssetExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource, DbtProject

RELATIVE_PATH_TO_MY_DBT_PROJECT = "../dbt_project"

dbt_project = DbtProject(
    project_dir=Path(__file__)
    .joinpath("..", RELATIVE_PATH_TO_MY_DBT_PROJECT)
    .resolve(),
)

dbt_project.prepare_if_dev()


@dbt_assets(manifest=dbt_project.manifest_path)
def dbt_project_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
