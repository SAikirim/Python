#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/root/ce.json"
curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d  @/root/test2.json https://automl.googleapis.com/v1beta1/projects/saiki-200813/locations/us-central1/models/TBL4476826519234150400:predict
