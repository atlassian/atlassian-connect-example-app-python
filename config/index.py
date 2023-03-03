import os

connect_app_descriptor = {
    "name": "Sample Connect App Python",
    "description": "Atlassian Connect app - Python",
    "key": "com.atlassian.sample-app-python",
    "baseUrl": "<NGROK_URL>",
    "vendor": {
        "name": "Python connect app sample",
        "url": "https://github.com/atlassian/atlassian-connect-sample-app-python/"
    },
    "authentication": {
        "type": "none"
    },
    "apiVersion": 1,
    "modules": {
        "generalPages": [
            {
                "url": '/config',
                "key": 'acn-config',
                "location": "none",
                "name": {
                    'value': 'Connect Descriptor'
                }
            },
        ],
        "postInstallPage": {
            "url": "/",
            "key": "acn-index",
            "name": {
                "value": "Index"
            }
        },
    }
}