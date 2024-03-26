import os

# Read photo_test_relative_path.txt to get photo paths
photo_test_paths_file = "/data/zj/SBIR/DLI-Net-main/Sketchy/photo_test_relative_path.txt"
with open(photo_test_paths_file, "r") as f:
    photo_test_paths = [line.strip() for line in f]

# Generate and store corresponding sketch paths with existing photos
sketch_test_file = "/data/zj/SBIR/DLI-Net-main/Sketchy/sketch_test_relative_path.txt"

# Define the range of sketch indices
sketch_indices = range(1, 11)

# Open the file in write mode (this will create a new file or overwrite an existing one)
with open(sketch_test_file, "w") as f:
    for photo_path in photo_test_paths:
        category, image_number = os.path.split(photo_path)
        image_number, _ = os.path.splitext(image_number)

        # Generate sketch file names for indices 1 to 10
        for i in sketch_indices:
            sketch_file_names = f"/data/zj/SBIR/DLI-Net-main/Sketchy/sketch_dataset/tx_000100000000/{category}/{image_number}-{i}.png"
            #print(sketch_file_names)
            # if any(os.path.exists(path) for path in sketch_file_names):
            #     print("yes" + str(sketch_file_names))
            #     f.write(f"{category}/{image_number}-{i}.png"+'\n')

            if os.path.exists(sketch_file_names):
                print("yes"+sketch_file_names)
                f.write(f"{category}/{image_number}-{i}.png" + "\n")
        # sketch_file_names = [f"/data/zj/SBIR/DLI-Net-main/Sketchy/sketch/{category}/{image_number}-{i}.png" for i in sketch_indices]
        #
        # # Check if at least one sketch file exists
        # existing_sketch_paths = [path for path in sketch_file_names if os.path.exists(path)]
        # print(existing_sketch_paths)
        #
        # # If at least one sketch exists, write the existing sketch file names to the file
        # if existing_sketch_paths:
        #     f.write("\n".join(existing_sketch_paths) + "\n")
