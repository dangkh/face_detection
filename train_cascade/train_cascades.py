import os
import sys
from train_cascade.config import *
from datetime import datetime
import time


def create_vecfile(width, height, num):
    print("[INFO] Started collapsing the samples into a vector file...")
    exec_str = "{} -vec {} -w {} -h {} -info {} -num {}".format(
        SAMPLE_CREATOR, VEC_FILE, width, height, POSITIVE_INFO_FILE, num)
    # print(exec_str)
    os.system(exec_str)
    print("[INFO] Finished.")


def train_cascade(output_dir, width, height, num_pos, num_neg, max_far, num_stages=NUM_STAGES):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    print("[INFO] Started training cascade...")
    exec_str = "{} -data {} -vec {} -bg {} -w {} -h {} -numPos {} -numNeg {} \
                -maxFalseAlarmRate {} -featureType {} -numStages {} {}".format(
        CASCADE_TRAINER, output_dir, VEC_FILE, NEGATIVE_INFO_FILE, width,
        height, num_pos, num_neg, max_far, FEATURE_TYPE, num_stages,
        EXTRA_PARAMS)
    # print(exec_str)
    os.system(exec_str)
    print("[INFO] Finished.")


if __name__ == "__main__":
    with open(NUM_POS_FILE, "r") as f:
        default_num_pos = f.readline()

    with open(NUM_NEG_FILE, "r") as f:
        default_num_neg = f.readline()

    with open(BATCH_FILE, "r") as f:
        i = 0
        for line in f:
            if line.startswith("#"):
                continue

            params = line.split()
            if len(params) != 5:
                continue

            i += 1
            print("\n[INFO] #{}".format(i))

            # numPos == 0
            if params[2] == 0:
                params[2] = default_num_pos

            # numNeg == 0
            if params[3] == 0:
                params[3] = default_num_neg

            ts = time.time()
            dt = datetime.fromtimestamp(ts).strftime('_%Y%m%d_%H%M%S')

            params.append(dt)

            output_dir = os.path.join(BASE_DIR, "output", "_".join(params))
            os.makedirs(output_dir)

            create_vecfile(params[0], params[1], default_num_pos)
            train_cascade(output_dir, *params[:5])

        print("[INFO] Done.")
