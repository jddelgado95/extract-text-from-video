# extract-text-from-video

This program shows how to use the Speech Recognition and moviepy libraries to create a simple algorithm to extract text from video.


## Dependencies
pip install SpeechRecognition
pip install moviepy


### Google Speech Recognition API 
The Google Speech Recognition API key is specified by key. If not specified, it uses a generic key that works out of the box. This should generally be used for personal or testing purposes only, as it may be revoked by Google at any time.

To obtain your own API key, simply follow the steps on the API Keys page at the Chromium Developers site. In the Google Developers Console, Google Speech Recognition is listed as "Speech API". Note that the API quota for your own keys is 50 requests per day, and there is currently no way to raise this limit.