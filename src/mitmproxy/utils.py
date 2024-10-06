# utils.py
import datetime
import subprocess
import logging

async def take_screenshot(index):
    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"C:\\screenshot_{timestamp}_{index}.png"

    # PowerShell command to take a screenshot
    powershell_command = f"""
    param (
        [string]$outputFile = "{output_file}"
    )

    Add-Type -AssemblyName System.Windows.Forms
    $width = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width
    $height = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height
    $bmp = New-Object Drawing.Bitmap($width, $height)
    $g = [Drawing.Graphics]::FromImage($bmp)
    $g.CopyFromScreen(0, 0, 0, 0, $bmp.Size)
    $g.Dispose()
    $bmp.Save($outputFile)
    $bmp.Dispose()
    """

    # Run the PowerShell command to take the screenshot
    subprocess.run(["powershell", "-Command", powershell_command])
    logging.info(f"Screenshot saved at: {output_file}")

    return output_file
