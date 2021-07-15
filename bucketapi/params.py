# path of the file to upload to gcp (the path of the file should be absolute or should match the directory where the make command is run)
LOCAL_PATH='/home/soutobias/code/soutobias/datamodelapi/raw_data/*.csv'

# project id
PROJECT_ID='le-wagon-data-582'

# bucket name
BUCKET_NAME='wagon-data-582-finalproject'

# bucket directory in which to store the uploaded file (we choose to name this data as a convention)
BUCKET_FOLDER='data'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
BUCKET_DATA_PATH = f"{BUCKET_FOLDER}/"

