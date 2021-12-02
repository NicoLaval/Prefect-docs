# Prefect docs

## Local setup

### Python

A good way to install `python` is to install [Anaconda](https://www.anaconda.com/products/individual) (including in particular `conda`) on your laptop.

Nevertheless, if you have access to the [Insee's Datalab](https://datalab.sspcloud.fr/), you can simply create a `VS Code` service (preconfigured regarding our needs).

### Prefect

Once you have your favorite environment, you can install `prefect`.

```
conda install -c conda-forge prefect
```

## Prefect script

You have a sample script at root, `sample.py`.

## Run locally

```script
git clone https://github.com/NicoLaval/Prefect-docs.git
cd Prefect-docs
```

Be sure that the `PUSH_TO_PREFECT_CLOUD_DASHBOARD` constant is equal to `False`.

```script
python sample.py
```

## Run on Prefect cloud

### Create an account

You have to create an account [here](https://cloud.prefect.io/).

In your user settings, create an `API key`. Keep it safe.

### Create a cloud project

Create a `sample` project [here](https://cloud.prefect.io/).

### Connect your local environment to Prefect cloud

```script
prefect auth login -k "YOU_API_KEY"
```

### Register the `run-sample` flow on Prefect cloud

Be sure that the `PUSH_TO_PREFECT_CLOUD_DASHBOARD` constant has been switched to `True`.

```script
python sample.py
```

You can check on `Prefect cloud` that your flow `run-sample` as been created in your `sample` project.

### Execute the flow

`Prefect cloud` will offer you dashboard, metrics but will not execute your pipeline itself. To run your flow, you have a `quick run` button on the flow screen. To make the execution possible, you have to provide a runtime environment.

### Start your local environment

```script
prefect agent local start
```

### Execute your flow from the Prefect cloud UI, and browse results

Click the `Quick run` button.

You can see a new `run` on the `flow page`.

You can browse it selecting the `runs` tab, and enjoy your dashboard, logs, schemas.

