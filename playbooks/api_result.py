#/usr/bin/python3

import json

result = """
{
    "msg": {
        "authenticationType": "RADIUS",
        "authorizationType": "RADIUS",
        "cookie": {
            "Domain": "",
            "Expires": "2021-11-20T08:22:07.17608597Z",
            "HttpOnly": false,
            "MaxAge": 86400,
            "Name": "access_token",
            "Path": "/",
            "Raw": "",
            "RawExpires": "",
            "SameSite": 2,
            "Secure": true,
            "Unparsed": null,
            "Value": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjE2LCJkc24iOiJhcmlzdGEiLCJkc3QiOiJ1c2VyIiwic2lkIjoiNTVlODE3YmNkYTFhMWMwMTFkZjBlNzU0Mjk2Y2I4ZmRlMTNmYzY4MDE3MjJjZjE1OWM1Zjc1MzUxYTk5YzIzZS1FYUFsSHo0bXc2MkZPdnA1aGZXMHNpb2ZxOTZLVy05bHZhZ3hHUWxaIn0.AIvZbc2q5-GotFSoymm9bRzq76XE4q_P_ZdodDE249xRDzZS6zJsUfQqmHEa3FvF2y5COmOHadoehX8s-sI6ZglSJWH6LDMQmjhvApuF7MPvRw955znXvuwoE0PzenlxQJeOD1BKfgtWKsFAQv-0KUamI5nT4LRrOHxBeQf8dzc1eSdMkA9OCcb2sOL41q3Jx6r-h4icjlEihF92Ux1wgQ4h5UCD-aRVI8L4zNu-CWavluNQ2nfr8aBSah6h6klblqOurwjIhDGC9i9dJwy5Y3pUP7g_oCs07d2XwEcJLND98VuPcT5zDXJek54DHjnuWm4ZoHBBq0VkF1Lt9TKVDElrC9R5uJuJBw0YV3m7EggLmtQK8RfeYsy00_TUkBmftyaCWAvtkqpKcCSrN7aw741VzIQ-Vm3BXHQfOqMjqalj8gMquXLbSGa0XfZEfQTtIswDXfP9djXQtQiSdKYMEIJjhbyxYnsFEiZ-y7K-OkH2QRUkq1OJnQgcHSNk2ysdOC1M0bu0_qR_LGbWMQcasuvdusVAe-KcwSQs68Uwjcw-wOjosYOVOKkhA-gfs3Iw9hhqfgCbSawOg1An6jcTtr14TcATsSCAKFCQJcgZ7uvvrHiGJ7Bsp2JnAnB2YOFUH8I4puI3oECdaz0e2lpx6DmLvCIao_Gxu2AIBsV4p-w"
        },
        "defaultUserFirstLogin": false,
        "permissionList": [
            {
                "mode": "rw",
                "name": "image"
            },
            {
                "mode": "rw",
                "name": "cvpTheme"
            },
            {
                "mode": "rw",
                "name": "networkProvisioning"
            },
            {
                "mode": "rw",
                "name": "configlet"
            },
            {
                "mode": "rw",
                "name": "eventNotification"
            },
            {
                "mode": "rw",
                "name": "eventConfiguration"
            },
            {
                "mode": "rw",
                "name": "label"
            },
            {
                "mode": "rw",
                "name": "purge"
            },
            {
                "mode": "rw",
                "name": "ccMgmt"
            },
            {
                "mode": "rw",
                "name": "inventory"
            },
            {
                "mode": "rw",
                "name": "snapshot"
            },
            {
                "mode": "rw",
                "name": "ztp"
            },
            {
                "mode": "rw",
                "name": "danz"
            },
            {
                "mode": "rw",
                "name": "cloudManager"
            },
            {
                "mode": "rw",
                "name": "task"
            },
            {
                "mode": "rw",
                "name": "aaa"
            },
            {
                "mode": "rw",
                "name": "account"
            },
            {
                "mode": "rw",
                "name": "ccApprove"
            },
            {
                "mode": "rw",
                "name": "metricDashboards"
            },
            {
                "mode": "rw",
                "name": "bugAlerts"
            },
            {
                "mode": "rw",
                "name": "enroll"
            },
            {
                "mode": "rw",
                "name": "msTapAgg"
            },
            {
                "mode": "rw",
                "name": "ssl"
            },
            {
                "mode": "rw",
                "name": "audit"
            },
            {
                "mode": "rw",
                "name": "workflow"
            },
            {
                "mode": "rw",
                "name": "publicCloudAccounts"
            },
            {
                "mode": "rw",
                "name": "licensing"
            },
            {
                "mode": "rw",
                "name": "eventAcknowledgment"
            }
        ],
        "roles": [
            {
                "Data": {
                    "createdBy": "cvp system",
                    "createdOn": 1608311710962,
                    "description": "",
                    "key": "network-admin",
                    "moduleList": [
                        {
                            "mode": "rw",
                            "name": "image"
                        },
                        {
                            "mode": "rw",
                            "name": "ztp"
                        },
                        {
                            "mode": "rw",
                            "name": "configlet"
                        },
                        {
                            "mode": "rw",
                            "name": "task"
                        },
                        {
                            "mode": "rw",
                            "name": "inventory"
                        },
                        {
                            "mode": "rw",
                            "name": "label"
                        },
                        {
                            "mode": "rw",
                            "name": "danz"
                        },
                        {
                            "mode": "rw",
                            "name": "aaa"
                        },
                        {
                            "mode": "rw",
                            "name": "account"
                        },
                        {
                            "mode": "rw",
                            "name": "snapshot"
                        },
                        {
                            "mode": "rw",
                            "name": "ssl"
                        },
                        {
                            "mode": "rw",
                            "name": "purge"
                        },
                        {
                            "mode": "rw",
                            "name": "cvpTheme"
                        },
                        {
                            "mode": "rw",
                            "name": "networkProvisioning"
                        },
                        {
                            "mode": "rw",
                            "name": "audit"
                        },
                        {
                            "mode": "rw",
                            "name": "workflow"
                        },
                        {
                            "mode": "rw",
                            "name": "cloudManager"
                        },
                        {
                            "mode": "rw",
                            "name": "publicCloudAccounts"
                        },
                        {
                            "mode": "rw",
                            "name": "enroll"
                        },
                        {
                            "mode": "rw",
                            "name": "ccMgmt"
                        },
                        {
                            "mode": "rw",
                            "name": "ccApprove"
                        },
                        {
                            "mode": "rw",
                            "name": "licensing"
                        },
                        {
                            "mode": "rw",
                            "name": "metricDashboards"
                        },
                        {
                            "mode": "rw",
                            "name": "eventNotification"
                        },
                        {
                            "mode": "rw",
                            "name": "eventConfiguration"
                        },
                        {
                            "mode": "rw",
                            "name": "eventAcknowledgment"
                        },
                        {
                            "mode": "rw",
                            "name": "bugAlerts"
                        },
                        {
                            "mode": "rw",
                            "name": "msTapAgg"
                        }
                    ],
                    "moduleListSize": 28,
                    "name": "network-admin"
                },
                "UserAssignmentMap": {
                    "arista": {
                        "AssignedBy": "",
                        "AssignedOn": 1634323392761
                    },
                    "cvpadmin": {
                        "AssignedBy": "cvp system",
                        "AssignedOn": 1608311740550
                    }
                }
            }
        ],
        "sessionId": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjE2LCJkc24iOiJhcmlzdGEiLCJkc3QiOiJ1c2VyIiwic2lkIjoiNTVlODE3YmNkYTFhMWMwMTFkZjBlNzU0Mjk2Y2I4ZmRlMTNmYzY4MDE3MjJjZjE1OWM1Zjc1MzUxYTk5YzIzZS1FYUFsSHo0bXc2MkZPdnA1aGZXMHNpb2ZxOTZLVy05bHZhZ3hHUWxaIn0.AIvZbc2q5-GotFSoymm9bRzq76XE4q_P_ZdodDE249xRDzZS6zJsUfQqmHEa3FvF2y5COmOHadoehX8s-sI6ZglSJWH6LDMQmjhvApuF7MPvRw955znXvuwoE0PzenlxQJeOD1BKfgtWKsFAQv-0KUamI5nT4LRrOHxBeQf8dzc1eSdMkA9OCcb2sOL41q3Jx6r-h4icjlEihF92Ux1wgQ4h5UCD-aRVI8L4zNu-CWavluNQ2nfr8aBSah6h6klblqOurwjIhDGC9i9dJwy5Y3pUP7g_oCs07d2XwEcJLND98VuPcT5zDXJek54DHjnuWm4ZoHBBq0VkF1Lt9TKVDElrC9R5uJuJBw0YV3m7EggLmtQK8RfeYsy00_TUkBmftyaCWAvtkqpKcCSrN7aw741VzIQ-Vm3BXHQfOqMjqalj8gMquXLbSGa0XfZEfQTtIswDXfP9djXQtQiSdKYMEIJjhbyxYnsFEiZ-y7K-OkH2QRUkq1OJnQgcHSNk2ysdOC1M0bu0_qR_LGbWMQcasuvdusVAe-KcwSQs68Uwjcw-wOjosYOVOKkhA-gfs3Iw9hhqfgCbSawOg1An6jcTtr14TcATsSCAKFCQJcgZ7uvvrHiGJ7Bsp2JnAnB2YOFUH8I4puI3oECdaz0e2lpx6DmLvCIao_Gxu2AIBsV4p-w",
        "user": {
            "addedByUser": "",
            "contactNumber": "",
            "currentStatus": "Online",
            "email": "",
            "firstName": "",
            "lastAccessed": 1637310127182,
            "lastName": "",
            "userId": "arista",
            "userStatus": "Enabled",
            "userType": "RADIUS"
        },
        "username": "arista"
    }
}
"""

result_dict = json.loads(result)

print(result_dict['msg']['sessionId'])