# Vertex AI Feature Store

gcloud commands and process

### Create a Feature Store
```
gcloud beta ai featurestores create $FEATURESTORE_ID \
    --location=$REGION \
    --project=$PROJECT_ID \
    --featurestore-location=$REGION \
    --description="Feature Store for demo"
```

### Create a Feature Store entity type
```
gcloud beta ai featurestores entity-types create $ENTITY_TYPE_ID \
    --featurestore=$FEATURESTORE_ID \
    --location=$REGION \
    --project=$PROJECT_ID \
    --description="Entity type for demo"
```

### Create a Feature Store feature
```
gcloud beta ai featurestores features create $FEATURE_ID \
    --featurestore=$FEATURESTORE_ID \
    --entity-type=$ENTITY_TYPE_ID \
    --location=$REGION \
    --project=$PROJECT_ID \
    --description="Feature for demo" \
    --value-type=DOUBLE \
    --labels=feature_group=customer
```

### Create a Ingest job
```
gcloud beta ai featurestores ingest \
    --featurestore=$FEATURESTORE_ID \
    --entity-type=$ENTITY_TYPE_ID \
    --location=$REGION \
    --project=$PROJECT_ID \
    --feature-ids=$FEATURE_ID \
    --entity-id-file=$ENTITY_ID_FILE \
    --feature-value-file=$FEATURE_VALUE_FILE \
    --ingest-time-file=$INGEST_TIME_FILE
```

### Use Feature Store in a training job
```
gcloud beta ai model training-jobs submit training \
    --region=$REGION \
    --master-image-uri=$IMAGE_URI \
    --scale-tier=BASIC \
    --project=$PROJECT_ID \
    -- \
    --featurestore=$FEATURESTORE_ID \
    --entity-type=$ENTITY_TYPE_ID \
    --feature-ids=$FEATURE_ID \
    --entity-id-file=$ENTITY_ID_FILE \
    --feature-value-file=$FEATURE_VALUE_FILE \
    --ingest-time-file=$INGEST_TIME_FILE
```