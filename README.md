# Image-Processing-Practice

A repo to help me figure out how to use PyTesseract and Pillow with python. Intended as an addon to my other project, which was experimenting with OpenAI's public API. In the interest of not cluttering up that repo, I'm developing these features independently and will then merge them whenever.

## What you need
- A computer that can run an IDE (not optional, we're not writing code in notepad)
- PyCharm community or ultimate (optional only if you're crazy, yes I will fight you over this)
- The PyTesseract installer. I'm using this link since I'm developing on Windows: <https://github.com/UB-Mannheim/tesseract/wiki>
- Patience (optional, but preferred)

## What's here so far
(This list will grow)
- A simple program that takes images and extracts and prints text from them
- Your mum

## How to use this stuff
If you want to access code from on here, you may have to download or clone the entire repository so that you don't have any missing references. There will be a note in a comment at the top of each script that identifies which other files it requires. If nothing's mentioned, it's standalone and you're good to go!

You will also want to install tesseract to your PC before you get started. And make sure that you've double checked the install directory. I read in a couple of places that it's best not to change the base install directory when performing this installation (Which goes to `'C:/Program Files/Tesseract/...'`). I'm brave, but when it comes to randomly breaking breaking dependencies and then not being able to find them on the nightmare that is my code drive, I'd really rather not deal with that. If you want to install it somewhere else, go for it! (This tangent tho wtf)

Another error that I made (and one that you can avoid) is that when setting the tesseract_cmd, make sure to use:
`pytesseract.tesseract_cmd = path_to_tesseract_executable` instead of `pytesseract.tesseract_cmd(path_to_tesseract_executable)`, which is an error that took me far too long to identify.

More stuff to come as I add more content to this repo.

_Psst, there's also another project I'm working on right now! You can find it over here: <https://github.com/SamarthK1239/OpenAI-Api-Shenanigans>_
