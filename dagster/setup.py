from setuptools import find_packages, setup

setup(
    name="template_dagster_dbt_clickhouse",
    packages=find_packages(exclude=["template_dagster_dbt_clickhouse_tests"]),
    package_data={"template_dagster_dbt_clickhouse": ["dbt-project/**/*"]},
    install_requires=[
        "dagster",
        "dagster-dbt",
        "pandas",
        "dbt-core",
        "dbt-clickhouse",
        # packaging v22 has build compatibility issues with dbt as of 2022-12-07
        "packaging<22.0",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)