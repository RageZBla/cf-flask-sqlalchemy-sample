export VCAP_SERVICES='{
  "p.mysql": [
   {
    "credentials": {
     "uri": "sqlite:///books-collection.db"
    },
    "label": "p.mysql",
    "name": "database",
    "plan": "standard",
    "provider": null,
    "syslog_drain_url": null,
    "tags": [],
    "volume_mounts": []
   }
  ]
}'
export VCAP_APPLICATION='{
  "application_id": "fa05c1a9-0fc1-4fbd-bae1-139850dec7a3",
  "application_name": "my-app",
  "application_uris": [
    "my-app.example.com"
  ],
  "application_version": "fb8fbcc6-8d58-479e-bcc7-3b4ce5a7f0ca",
  "cf_api": "https://api.example.com",
  "limits": {
    "disk": 1024,
    "fds": 16384,
    "mem": 256
  },
  "name": "my-app",
  "organization_id": "c0134bad-97a9-468d-ab9d-e97547e3aed5",
  "organization_name": "my-org",
  "space_id": "06450c72-4669-4dc6-8096-45f9777db68a",
  "space_name": "my-space",
  "uris": [
    "my-app.example.com"
  ],
  "users": null,
  "version": "fb8fbcc6-8d58-479e-bcc7-3b4ce5a7f0ca"
  }
'