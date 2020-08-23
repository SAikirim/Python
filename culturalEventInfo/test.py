# TODO(developer): Uncomment and set the following variables
# project_id = 'PROJECT_ID_HERE'
# compute_region = 'COMPUTE_REGION_HERE'
# model_display_name = 'MODEL_DISPLAY_NAME_HERE'
# inputs = {'value': 3, ...}

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project="saiki-200813", region="us-central1")

if feature_importance:
    response = client.predict(
        model_display_name=model_display_name,
        inputs=inputs,
        feature_importance=True,
    )
else:
    response = client.predict(
        model_display_name=model_display_name, inputs=inputs
    )

print("Prediction results:")
for result in response.payload:
    print(
        "Predicted class name: {}".format(result.tables.value.string_value)
    )
    print("Predicted class score: {}".format(result.tables.score))

    if feature_importance:
        # get features of top importance
        feat_list = [
            (column.feature_importance, column.column_display_name)
            for column in result.tables.tables_model_column_info
        ]
        feat_list.sort(reverse=True)
        if len(feat_list) < 10:
            feat_to_show = len(feat_list)
        else:
            feat_to_show = 10

            print("Features of top importance:")
            for feat in feat_list[:feat_to_show]:
                print(feat)
