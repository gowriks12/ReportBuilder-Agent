import os
import shutil
import datetime

def get_most_recent_image():
    folder_path = 'C:\\Users\\gowri\\Documents\\Projects\\ReportBuilder-Agent\\Plots'
    # dest_path = 'C:\\Users\\gowri\\Documents\\Projects\\ReportBuilder-Agent\\GeneratedPlots'

    # List all files in the directory
    files = os.listdir(folder_path)

    # Filter out non-image files (you can customize this for specific image types)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

    # Get the full path for each image file
    image_files = [os.path.join(folder_path, f) for f in image_files]

    # moved_images = [move_image_to_folder(image,dest_path) for image in image_files]
    most_recent_image = ''
    # # Find the most recently created image file
    try:
        most_recent_image = max(image_files, key=os.path.getctime)
    finally:
        return image_files, most_recent_image



def move_image_to_folder(image_path, destination_folder):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move the file to the destination folder
    shutil.move(image_path, destination_folder)

# Example usage:
def get_plots_for_report():
    folder_path = 'C:\\Users\\gowri\\Documents\\Projects\\ReportBuilder-Agent'
    plot_folder_path = 'C:\\Users\\gowri\\Documents\\Projects\\ReportBuilder-Agent\\GeneratedPlots'
    recent_images = get_most_recent_image(folder_path)
    print(recent_images)
    for image in recent_images:
        # Move the image to the destination folder
        move_image_to_folder(image, plot_folder_path)
    return recent_images

def get_report_name():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

    # Create the filename with the datetime included
    # report_name = f"report_{formatted_datetime}.txt"
    report_name = f"report_{formatted_datetime}.docx"
    print(report_name)
    return report_name
    # print(f"The most recently created image is: {recent_image}")


# def save_note(note):
#     if not os.path.exists(note_file):
#         open(note_file, "w")
#     with open(note_file, "a") as f:
#         f.writelines([note + "\n"])
#
#     return "note saved"
#
# report_name = get_report_name()
# note_file = os.path.join("Reports", report_name)