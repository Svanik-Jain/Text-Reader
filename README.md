<h3 align="center">Text Reader</h3>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project
We are a bunch of school students who wanted to make a project in our holidays. We decided to make this project. It is a very interesting project.
Text reader is a tool created for the purpose of the reading text out loud by a speech input. It has the ability to reread every individual line or even reread every pair of words for easy dictation.


## Built With

This is project is built with python. Various modules of python like pyttsx3, pypdf2, speechrecognition were used.

## Prerequisites
1) Python
2) Pyttsx3
3) PyPDF2
4) SpeechRecognition

### Installation

1. Install python from https://www.python.org/downloads/
2. Install pyttsx3
   ```sh
   pip install pyttsx3
   ```
3. Install PyPDF2
   ```sh
   pip install PyPDF2
   ```
4. Install SpeechRecognition
   ```sh
   pip install SpeechRecognition
   ```

## Usage

1. Select a ```PDF File``` from your computer though a window which the code will open for you itself. The text reader will dictate from the file selected.
2. Speak the page number you want the text reader to read. In case you do not want it to read any page, you can say ```stop``` or ```no``` or ```none```
3. The text reader will ask you if you want it to read a pair of words twice or just simply read out the text.
   i. In case you say yes, it will dictate two words twice as a pair and then move on to the next pair
        Eg: If the text is ```This is some text```, it will read ```This is```,```This is```, ```some text```, ```some text```
      This feature was added to make writing down text while dictation easy.
   ii.In case you say no, it will simply read out the words from the page selected line by line.
4. The text reader will read out the text based on your selection above.
5. After reading the text, It will ask you if anything is to be repeated
6. In case you say ```yes```, It will ask which line to be repeated
7. On specifying few words (incomplete line), the reader will find the line you are referring to and read out the entire line along with the next one.
8. After repeating, you can tell it to read further by saying ```yes``` so that it reads to more lines, or deny it.
9. In case you do not want text reader to repeat anything, say ```stop``` or ```no``` or ```none```
10. The text reader will say ```Thank you for using text dictator``` before closing

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments
Special thanks to our contributers:
Svanik Jain,
Aadi Nigam,
Sanidhya Gupta,
Maulik Gupta,
Supraj,
Vaibhav Sai,
Sidharth Ganguly
