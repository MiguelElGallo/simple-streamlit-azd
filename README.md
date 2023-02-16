# Simple Flask AZD Template

The most basic Flask "hello world" application as an AZD template ready for Azure App Service

![system diagram](diagram.png)

## Usage

Install AZD and use the `azd up` command to clone and deploy this repository. Then make changes to app.py and run `azd deploy` again to update your changes. 

```console
$ azd up -t tonybaloney/simple-flask-azd

Initializing a new project (azd init)

...

Deploying services (azd deploy)

  (✓) Done: Deploying service web
  - Endpoint: https://web-example-12345.azurewebsites.net/

SUCCESS: Your Azure app has been deployed!
```

## Notes

This uses the F1 (free) SKU for app service, which has limited CPU and RAM resources.

See the [pricing calculator](https://azure.microsoft.com/en-au/pricing/calculator/) for details on paid SKUs replace the SKU option with a suitable choice.
