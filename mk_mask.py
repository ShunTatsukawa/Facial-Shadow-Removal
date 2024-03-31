import os
import subprocess

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename[:-4] + "_segmented.png")
            # human_part_segmentation.pyの絶対パスを指定してください↓
            script_path = "D:\Documents\AILIA_trial_1.2.16/ailia_1_216_0_trial/python/ailia-models-master/image_segmentation/human_part_segmentation/human_part_segmentation.py"

            command = [
                "python",
                script_path,
                "--input",
                input_path,
                "--savepath",
                output_path,
                "--env_id",
                "3",
                "--benchmark_count",
                "5"
            ]

            env = os.environ.copy()
            env["PYTHONPATH"] = ""

            subprocess.run(command, env=env)

if __name__ == "__main__":
    input_folder = "D:/Documents/Facial-Shadow-Removal/data/mk_datasets/data_C"
    output_folder = "D:/Documents/Facial-Shadow-Removal/data/mk_datasets/segment_mask"

    process_images(input_folder, output_folder)