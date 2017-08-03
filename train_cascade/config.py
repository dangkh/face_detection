import os


OPENCV_DIR = ""
BASE_DIR = "data/"

BATCH_FILE = os.path.join(BASE_DIR, "batch.txt")

FEATURE_TYPE = "LBP"
NUM_STAGES = "7"
EXTRA_PARAMS = "-precalcValBufSize 1000 -precalcIdxBufSize 1000"

SAMPLE_CREATOR = os.path.join(OPENCV_DIR, "opencv_createsamples")
CASCADE_TRAINER = os.path.join(OPENCV_DIR, "opencv_traincascade")

INPUT_NEGATIVE_DIR = os.path.join(BASE_DIR, "input_negative")
INPUT_POSITIVE_DIR = os.path.join(BASE_DIR, "input_positive")

OUTPUT_NEGATIVE_DIR = os.path.join(BASE_DIR, "output_negative")
OUTPUT_POSITIVE_DIR = os.path.join(BASE_DIR, "output_positive")

NEGATIVE_INFO_FILE = os.path.join(OUTPUT_NEGATIVE_DIR, "negative.txt")
NUM_NEG_FILE = os.path.join(OUTPUT_NEGATIVE_DIR, "numNeg.txt")
POSITIVE_INFO_FILE = os.path.join(OUTPUT_POSITIVE_DIR, "positive.txt")
NUM_POS_FILE = os.path.join(OUTPUT_POSITIVE_DIR, "numPos.txt")
VEC_FILE = os.path.join(OUTPUT_POSITIVE_DIR, "vecfile.vec")
