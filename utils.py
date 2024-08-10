import os
import logging
import glob


def clean_folder(email_img, folder_path="images"):
    """
    Remove all image files in the specified folder except the one to attach in email.

    Args:
        folder_path (str): The path of the folder to clean.
        email_img (str): The path of the image to exclude from deletion.
    """
    images = glob.glob("images/*.png")
    images.sort()
    for image in images:
        if image != email_img:
            os.remove(image)

            logging.info("Cleaned image folder successfully!")
