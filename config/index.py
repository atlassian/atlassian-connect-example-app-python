import os

connect_app_descriptor = {
    "name": "Sample Connect App Python",
    "description": "Atlassian Connect app - Python",
    "key": "com.atlassian.sample-app-python",
    "baseUrl": os.environ.get("APP_URL"),
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
                "url": "/templates/index.html",
                "key": "hello-world",
                "location": "system.top.navigation.bar",
                "name": {
                    "value": "Test"
                }
            }
        ],
        "postInstallPage": {
            "url": "index.html",
            "key": "acn-index",
            "name": {
                "value": "Index"
            }
        },
    }
}