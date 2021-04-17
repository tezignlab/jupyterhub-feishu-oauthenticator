# JupyterHub FeiShu Authenticator
JupyterHub FeiShu Authenticator is a FeiShu OAuth authenticator built on top of OAuthenticator

## Setup

First, you’ll need to create a FeiShu App at https://open.feishu.cn/document/uQjL04CN/ukzM04SOzQjL5MDN.

Then, add the following to your ``jupyterhub_config.py`` file:

```python
from feishuauthenticator.feishu import FeiShuOAuthenticator
c.JupyterHub.authenticator_class = FeiShuOAuthenticator

app_id = '[your-feishu-app-id]'
app_secret = '[your-feishu-app-secret]'
c.FeiShuOAuthenticator.authorize_url = 'https://open.feishu.cn/open-apis/authen/v1/index'
c.FeiShuOAuthenticator.extra_authorize_params = {'redirect_uri': 'http://[your-host]/hub/oauth_callback', 'app_id': app_id}
c.FeiShuOAuthenticator.client_id = app_id
c.FeiShuOAuthenticator.client_secret = app_secret
```
Note that you need to got to FeiShu Developer Console --> "Security Settings" --> "Redirect URL" to add http://[your-host]/hub/oauth_callback as shown in the `screenshot here <https://user-images.githubusercontent.com/595772/114486465-f675f200-9bdb-11eb-87cf-49eb1a13e60f.png>`__.


## Team

- Yuandong Yang, Tezign.com
- Qiang Ju, Tezign.com
- [Harry Wang](http://harrywang.me/)

