import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Pratik Audio Player')

# Set up the screen
screen = pygame.display.set_mode((400, 400))

# Set up the colors
WHITE = (255, 255, 255)
PINK = (146, 5, 156)

# Set up the font
font = pygame.font.SysFont("Arial", 20)

# Set up the UI
root = tk.Tk()
root.withdraw()

# Define a function to open the file dialog
def open_file_dialog():
    # Set the file types to only allow selection of MP3 files
    filetypes = (("MP3 files", "*.mp3"), ("All files", "*.*"))

    # Get the file path using the file dialog
    filename = filedialog.askopenfilename(filetypes=filetypes)

    # Load the audio file
    if filename:
        pygame.mixer.music.load(filename)

        # Play the audio file
        pygame.mixer.music.play()

        # Display the file path on the Pygame screen
        text = font.render("Now Playing: " + filename.split('/')[-1], True, WHITE)
        screen.blit(text, (20, 20))
        # Update the screen
        pygame.display.flip()

# Create a button on the Pygame screen to open the file dialog
button = pygame.draw.rect(screen, PINK, (150, 320, 100, 50), 2, 3)
button_text = font.render("Select Audio", True, WHITE)
button_text_rect = button_text.get_rect(center=button.center)
screen.blit(button_text, button_text_rect)

# Update the screen
pygame.display.flip()

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            if button.collidepoint(event.pos):
                open_file_dialog()

# Quit Pygame
pygame.quit()
