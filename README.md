This was designed to be run with it's own stand alone python installation.  Git has file limits that is making it difficult to achieve this.  Python will have to be installed separately and will need the llama-cpp-python and pygame_ce libraries.

Put the Python folder in the root directory of the game, and use the launch.bat file to launch the game.

In it's final iteration this application will be designed to interface with ChatGPT's API to power the AI aspect of this game.  However, there will be a stand alone feature implemented as well.  So the user will have the power to decide which approach suits them best, since ChatGPT's API can get quite expensive.

Here is a link to a simple llama-2 model that can run on most people's systems:

https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q8_0.gguf

(Note: You will need access to huggingface to download this model)

As this is currently incomplete, the comments in the python code are fairly sparse.  The model interaction is not yet coded.

I am currently working on a fix to the issue with the text not wrapping in the text input box.  Should have this resolved soon.  Python's pygame library is a bit cumbersome because the GUI classes have to be manually coded.

Comments and documentation are sparse at the moment.  This will be resolved before the final iteration.

CURRENT BUGS IN PROGRESS:
When running this through the launch.bat ensure your cursor is in your primary monitor.  When this application launches, it will detect the resolution of your primary monitor and launch the game with that resolution.  If it opens on your secondary monitor and your secondary monitor has a lower resolution, then the game will not fit on the screen, and may have to be terminated from the console or from the windows manager.

Your GPU may spin up (a lot) when running this game.  This is because it is constantly redrawing the scene 60+ times a second (depending on your fps) even though it is a static scene.  I will address this issue in the final release.

As this project is incomplete, there are a multitude of bugs present.  They should all be identified and resolved upon a final release.