import os
import shutil
import random

def random_copy_images(source_folder, destination_folder, num_images):
    # Get a list of all image files in the source folder
    all_images = [f for f in os.listdir(source_folder)]

    # Ensure that the number of requested images is not more than the available images
    num_images = min(num_images, len(all_images))

    # Randomly choose 'num_images' images
    selected_images = random.sample(all_images, num_images)

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Copy selected images to the destination folder
    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy2(source_path, destination_path)

if __name__ == "__main__":
    # Replace 'source_folder' and 'destination_folder' with your actual folder paths
    source_folder = "landscape_images"
    destination_folder = "midjourney_sample"
    
    # Specify the number of images to randomly choose
    num_images_to_copy = 600

    # Call the function to copy the randomly selected images
    random_copy_images(source_folder, destination_folder, num_images_to_copy)
